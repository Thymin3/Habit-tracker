import sqlite3 as sql
import datetime
import controller


def setup_database():
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Creating the Habit table
    cursor.execute('''CREATE TABLE Habit
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT, HabitName TEXT, Periodicity TEXT,
                    CurrentStreak INTEGER, LongestStreak INTEGER, NumberOfBreaks INTEGER)''')

    # Creating the HabitExecution table
    cursor.execute('''CREATE TABLE HabitExecution
                    (HabitID INTEGER, DateTime TEXT, FOREIGN KEY(HabitID) REFERENCES Habit(ID))''')

    # Setting up example data
    # Inserting sample data for two habits
    habits = [("Daily Exercise", "daily"), ("Weekly Meditation", "weekly"), ("Daily Reading", "daily"),
              ("Daily Breakfast", "daily"), ("Weekly Calling Mom", "weekly")]

    for habit in habits:
        cursor.execute('''INSERT INTO Habit (HabitName, Periodicity, CurrentStreak, LongestStreak, NumberOfBreaks)
                            VALUES (?, ?, 0, 0, 0)''', (habit[0], habit[1]))
        habit_id = cursor.lastrowid  # Get the ID of the newly inserted habit

        # Inserting execution data for the last 4 months
        today = datetime.date.today()
        four_months_ago = today - datetime.timedelta(days=120)
        current_date = four_months_ago
        while current_date <= today:
            if habit[1] == "daily":
                cursor.execute('''INSERT INTO HabitExecution (HabitID, DateTime) VALUES (?, ?)''',
                               (habit_id, current_date.strftime('%Y-%m-%d %H:%M:%S')))
                current_date += datetime.timedelta(days=1)
            elif habit[1] == "weekly":
                if current_date.weekday() == 4:  # Friday
                    cursor.execute('''INSERT INTO HabitExecution (HabitID, DateTime) VALUES (?, ?)''',
                                   (habit_id, current_date.strftime('%Y-%m-%d %H:%M:%S')))
                current_date += datetime.timedelta(days=1)
            else:
                current_date += datetime.timedelta(days=1)

    # Closing the cursor and the connection
    conn.commit()
    cursor.close()
    conn.close()


def sql_complete_habit(habit_ID):
    # Storing current datetime in a variable
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    selected_habit = None  # Implement Connection from controller

    # Connecting to the database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Inserting a new execution for  a habit
    cursor.execute(f"INSERT INTO HabitExecution (HabitID, DateTime) VALUES ({habit_ID}, {current_datetime})")

    # Commit the changes and close the cursor and the connection
    conn.commit()
    cursor.close()
    conn.close()

def sql_create_habit(habit_name, periodicity):
    # Connecting to the database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Insert a new execution for habit
    cursor.execute(f'''INSERT INTO Habit (HabitName, Periodicity, CurrentStreak,
                   LongestStreak, NumberOfBreaks) VALUES({habit_name}, {periodicity}, 0, 0, 0)''')

def check_database():
    # Connecting to the database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from the Habit table
    cursor.execute('''SELECT * FROM Habit''')
    habit_rows = cursor.fetchall()
    print("Habit table:")
    for row in habit_rows:
        print(row)

    # Retrieving data from the HabitExecution table
    cursor.execute('''SELECT * FROM HabitExecution''')
    execution_rows = cursor.fetchall()
    print("\nHabitExecution table:")
    for row in execution_rows:
        print(row)

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    try:
        setup_database()
    except sql.OperationalError:
        pass
    finally:
        check_database()
