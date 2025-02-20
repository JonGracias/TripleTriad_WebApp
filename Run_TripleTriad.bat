@echo off
echo Starting TripleTriad Web App...

:: Step 1: Activate the virtual environment
call venv\Scripts\activate.bat

:: Step 2: Run the Flask app
python wsgi.py

:: Keep the command window open
pause
