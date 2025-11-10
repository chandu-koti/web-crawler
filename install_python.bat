@echo off
echo Downloading Python 3.12...
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe' -OutFile 'python-installer.exe'"

echo Installing Python...
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Cleaning up...
del python-installer.exe

echo Python installation completed!
echo Please restart your command prompt and try running: python --version
pause
