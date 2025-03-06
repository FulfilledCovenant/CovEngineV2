@echo off
echo Creating system restore point...
powershell -Command "Checkpoint-Computer -Description 'CovEngineV2 Tweaks - %date% %time%' -RestorePointType 'APPLICATION_INSTALL'"
if %errorlevel% equ 0 (
    echo System restore point created successfully.
    exit /b 0
) else (
    echo Failed to create system restore point.
    exit /b 1
) 