@echo off

cd /d %~dp0

pipenv install --dev
pipenv shell
