@echo off
echo Setting up the TripleTriad Web App...

:: Step 1: Create a virtual environment
echo Creating virtual environment...
python -m venv venv

:: Step 2: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Step 3: Install dependencies
echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

:: Step 4: Start the Flask app
echo Launching the application...
python wsgi.py

:: Keep the command window open
pause
