poetry run python manage.py runserver@echo off
cd C:\adrian\project\latihandjango\DjangoTutorials
if "%1"=="" (
    echo Please provide a command. Available commands: runserver, makemigrations, migrate
) else (
    if "%1"=="runserver" (
        poetry run python manage.py runserver
    ) else if "%1"=="makemigrations" (
        poetry run python manage.py makemigrations
    ) else if "%1"=="migrate" (
        poetry run python manage.py migrate
    ) else (
        echo Invalid command. Available commands: runserver, makemigrations, migrate
    )
)
pause
