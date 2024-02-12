@echo off

set IP=192.168.1.62
set risposta=

ping %IP%
timeout /t 3 > nul
echo.
echo.


:LOOP
if %errorlevel% equ 0 (
    echo "Il server non e attivo! Vuoi attivarlo? [Y/N]"
    set /p risposta=
    if /I "%risposta%"=="Y" (
        WakeMeOnLan.exe /wakeup %IP%
        timeout /t 3 > nul
        :LOOP2
        ping -n 1 %IP% > nul
        if %errorlevel% neq 0 (
            echo "Il ping ha dato esito positivo!"
            timeout /t 3 > nul
            echo "Apertura di VSB-server"
            timeout /t 1 > nul
            explorer "https://%IP%:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"
        ) else (
            echo "Qualcosa è andato storto! Eseguo nuovamente il ping"
            timeout /t 15 > nul
            goto :LOOP2
        )
    ) else if /I "%risposta%"=="N" (
        echo "Va bene! WOL si spegnera tra pochi secondi."
        timeout /t 3 > nul
        goto :EXIT
    ) else (
        echo "Risposta non valida. Per favore, inserisci Y per si o N per no."
        goto :LOOP
    )
) else if %errorlevel% neq 0 (
    echo "Il server e gia attivo! Desideri essere reindirizzato alla pagina?"
    set /p risposta=
    if /I "%risposta%"=="Y" (
        explorer "https://%IP%:8006/#v1:0:=node%2Fvsbserver:4:2::::7::"
    ) else if /I "%risposta%"=="N" (
        echo "Perfetto! WOL si chiudera tra pochi secondi"
        timeout /t 3 > nul
        GOTO :EXIT
    ) else (
        echo "Risposta non valida. Per favore, inserisci Y per si o N per no."
        goto :LOOP
    )
)
:EXIT
