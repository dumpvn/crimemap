@echo off

cd /d %~dp0

pipenv install --dev

echo flask run
start "" http://127.0.0.1:5000/
pipenv shell
