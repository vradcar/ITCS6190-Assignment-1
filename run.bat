@echo off
REM Windows batch script for running docker compose commands

IF "%1"=="build" (
    docker compose build app
    EXIT /B
)

IF "%1"=="up" (
    docker compose up --build
    EXIT /B
)

IF "%1"=="down" (
    docker compose down -v
    EXIT /B
)

IF "%1"=="clean" (
    docker compose down -v
    IF EXIST out (
        RD /S /Q out
    )
    MKDIR out
    ECHO Cleaned output directory
    EXIT /B
)

REM Default: show help
ECHO Usage: run.bat [command]
ECHO.
ECHO Commands:
ECHO   build   Build the app container
ECHO   up      Start all services
ECHO   down    Stop all services
ECHO   clean   Remove output files and stop services
ECHO.
