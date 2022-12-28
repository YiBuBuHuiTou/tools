@echo off
rem echo 开始设置开机启动

rem 系统启动目录 C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
rem 用户启动目录 C:\Users\YiBuBuHuiTou\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup


rem 设置开机启动文件夹
set dest=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
rem set dest=C:\Users\YiBuBuHuiTou\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup


%~d0
cd %~dp0
cd ..
set now=%cd%
echo %cd%\monitor.exe back > monitor.bat

mklink  "%dest%\monitor" %now%\monitor.bat


pause