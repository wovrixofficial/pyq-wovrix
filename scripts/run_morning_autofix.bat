@echo off
title Wovrix PYQ Morning Auto-Resolution Engine
echo ========================================================
echo   Wovrix PYQ Morning Auto-Resolution Engine
echo   Auditing questions, marks, KaTeX formulas and cache...
echo ========================================================
cd /d "%~dp0\.."
python scripts\morning_autofix.py
echo.
echo Process finished. Press any key to exit.
pause >nul
