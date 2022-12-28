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
rem 生成新的批处理，用于自启动
echo %~d0 > monitor.bat
echo cd %cd%  >> monitor.bat
echo start monitor.exe back  >> monitor.bat
rem 批处理移动到开机启动目录
move  "%now%\monitor.bat"  "%dest%"
rem 手动执行程序
start monitor.exe

pause