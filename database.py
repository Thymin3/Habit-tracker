import sqlite3 as sql
import datetime
import controller


def setup_database():
    # Connecting to the database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Creating the Habit table
    cursor.execute('''CREATE TABLE Habit
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT, HabitName TEXT, Periodicity TEXT,
                    CurrentStreak INTEGER, LongestStreak INTEGER, NumberOfBreaks INTEGER)''')

    # Creating the HabitExecution table
    cursor.execute('''CREATE TABLE HabitExecution
                    (HabitID INTEGER, DateTime TEXT, FOREIGN KEY(HabitID) REFERENCES Habit(ID))''')

    # Closing the cursor and the connection
    cursor.close()
    conn.close()


def sql_complete_habit():
    # Storing current datetime in a variable
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    selected_habit = None
    # Connecting to the database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Insert a new execution for habit 1
    cursor.execute(f"INSERT INTO HabitExecution (HabitID, DateTime) VALUES (1, {current_datetime})")

    # Commit the changes and close the cursor and the connection
    conn.commit()
    cursor.close()
    conn.close()

def sql_create_habit():
    # Connecting to the database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Insert a new execution for habit 1
    cursor.execute('''INSERT INTO Habit (HabitName, Periodicity, CurrentStreak,
                   LongestStreak, NumberOfBreaks) VALUES())''')
