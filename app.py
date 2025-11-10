import streamlit as st
import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

# Load environment variables
load_dotenv()

# Initialize Firecrawl
@st.cache_resource
def init_firecrawl():
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        st.error("Please set FIRECRAWL_API_KEY in your .env file")
        return None
    return FirecrawlApp(api_key=api_key)

def main():
    st.title("🕷️ Web Crawler")
    st.markdown("Enter a URL to crawl and extract content using Firecrawl")
    
    # Initialize Firecrawl
    app = init_firecrawl()
    if not app:
        return
    
    # URL input
    url = st.text_input("Enter URL to crawl:", placeholder="https://example.com")
    
    # Crawl button
    if st.button("🚀 Crawl Website", type="primary"):
        if not url:
            st.warning("Please enter a URL")
            return
        
        if not url.startswith(('http://', 'https://')):
            st.warning("Please enter a valid URL starting with http:// or https://")
            return
        
        # Show loading spinner
        with st.spinner("Crawling website... This may take a few minutes."):
            try:
                # Scrape the URL
                result = app.scrape(url)
                
                # Handle Firecrawl Document object response
                content = None
                metadata = None
                
                if result:
                    # Firecrawl returns a Document object with attributes
                    if hasattr(result, 'markdown') and result.markdown:
                        content = result.markdown
                    elif hasattr(result, 'content') and result.content:
                        content = result.content
                    elif hasattr(result, 'html') and result.html:
                        content = result.html
                    
                    # Get metadata from Document object
                    if hasattr(result, 'metadata') and result.metadata:
                        metadata = result.metadata
                
                if content:
                    st.success("✅ Crawling completed!")
                    
                    # Display results
                    st.subheader("📄 Extracted Content")
                    
                    # Show metadata if available
                    if metadata:
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            if hasattr(metadata, 'title') and metadata.title:
                                st.metric("Title", metadata.title)
                        
                        with col2:
                            if hasattr(metadata, 'description') and metadata.description:
                                desc = metadata.description
                                st.metric("Description", desc[:100] + "..." if len(desc) > 100 else desc)
                    
                    # Display content
                    st.text_area("Content", content, height=400)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Content",
                        data=content,
                        file_name=f"crawled_content_{url.replace('https://', '').replace('http://', '').replace('/', '_')}.txt",
                        mime="text/plain"
                    )
                    
                else:
                    st.error("Failed to extract content from the URL")
                    if result:
                        st.write("Available attributes:", [attr for attr in dir(result) if not attr.startswith('_')])
                    
            except Exception as e:
                st.error(f"Error during crawling: {str(e)}")

if __name__ == "__main__":
    main()
