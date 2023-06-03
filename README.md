# Habit-tracker

## General Info

This Habit Tracker is part of a project for the module OOFPP (Object Oriented and Functional Programming with Python) at IU Internationale Hochschule.
It is designed to help with tracking and managing daily and weekly habits. 
Running the application for the first time will trigger the creation of the habit tracker database, which will be populated with examplary habit data for 5 different habits for the last 4 months.
Note that the directory also includes a unittest file (unittest_habittracker.py) which is used for testing the data analysis parts of the application.
Unit testing requires the application to be executed at least once before conducting tests, as the script relies on the habit tracker database, which is created during the initial execution.

**Features:**
- Creating and Deleting habits
- Marking Habits complete for the day*
- Analyzing habit data (e.g. showing a table with the habits ordered by longest streak)

*Note, that habits can only be completed once a day, irrelevant if daily or weekly habits. Further completions on the same day will neither advance streaks, nor be saved in the database.

## Getting Started

**Git and Python 3 distribution (e.g. Python 3.11.3) required**  
**If you don't have a Python distribution installed, please download and install it from the Python website https://www.python.org**

Insert following commands into the command-line:

<ins>Clone this repository:</ins>

git clone https://github.com/Thymin3/Habit-tracker.git

<ins>Navigate to the project directory:</ins>

cd Habit-tracker

<ins>Create a new virtual environment (optional):</ins>

python -m venv env

alternatively: py -m venv env

<ins>Activate the virtual environment (optional):</ins>

source env/bin/activate     on macOS or Linux

env\Scripts\activate.bat    on Windows

<ins>Install project dependencies:</ins>

pip install -r requirements.txt

<ins>Start the application:</ins>

python controller.py

alternatively: py controller.py

<ins>Test the application:</ins>

python unittest_habittracker.py

alternatively: py unittest_habittracker.py
