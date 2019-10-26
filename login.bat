    @echo off

ping -n 1 172.16.1.1 > nul
if not ERRORLEVEL 1 (
    ping -n 1 8.8.8.8 > nul
    if ERRORLEVEL 1 (
        set pingresult=true
        goto done
    )
)

set pingresult=false

:done
if %pingresult% == true (
 python D:\Projects\login\login.py > nul
    echo Successfully Logged In
    pause
)