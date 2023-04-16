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
                    DaysSinceLastCompletion INTEGER, CurrentStreak INTEGER, LongestStreak INTEGER, 
                    NumberOfBreaks INTEGER)''')

    # Creating the HabitExecution table
    cursor.execute('''CREATE TABLE HabitExecution
                    (HabitID INTEGER, DateTime TEXT, FOREIGN KEY(HabitID) REFERENCES Habit(ID))''')

    # Setting up example data
    # Inserting sample data for two habits
    habits = [("Daily Exercise", "daily"), ("Weekly Meditation", "weekly"), ("Daily Reading", "daily"),
              ("Daily Breakfast", "daily"), ("Weekly Calling Mom", "weekly")]

    for habit in habits:
        cursor.execute('''INSERT INTO Habit (HabitName, Periodicity, 
                        DaysSinceLastCompletion, CurrentStreak, LongestStreak, 
                        NumberOfBreaks) VALUES (?, ?, 0, 0, 0, 0)''', (habit[0], habit[1]))
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


def sql_create_habit(habit_name, periodicity):
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Insert a new execution for habit
    cursor.execute(f'''INSERT INTO Habit (HabitName, Periodicity, DaysSinceLastCompletion, CurrentStreak,
                   LongestStreak, NumberOfBreaks) VALUES("{habit_name}", "{periodicity}", 0, 0, 0, 0)''')

    # Committing changes and closing the connection and cursor
    conn.commit()
    cursor.close()
    conn.close()


def sql_delete_habit(habit_name):
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Insert a new execution for habit
    cursor.execute(f'''DELETE FROM Habit WHERE HabitName = "{habit_name}"''')

    # Committing changes and closing the connection and cursor
    conn.commit()
    cursor.close()
    conn.close()


def sql_return_habit_list():
    # Connecting to database
    conn = sql.connect('habit_tracker.db')

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from Habit table
    cursor.execute('''SELECT HabitName FROM Habit''')
    habit_names_not_processed = cursor.fetchall()
    habit_names = [item[0] for item in habit_names_not_processed]

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    return habit_names


def sql_return_habit(name):
    # Connecting to database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from Habit table
    cursor.execute('''SELECT * FROM Habit WHERE HabitName = ?''', (name,))
    habit_data = cursor.fetchone()
    ID, name, periodicity, days_since_last_completion, current_streak, longest_streak, number_of_breaks = habit_data

    return ID, name, periodicity, days_since_last_completion, current_streak, longest_streak, number_of_breaks

    # Closing the cursor and the connection
    cursor.close()
    conn.close()


def sql_update_habit_data(days_since_last_completion, current_streak, longest_streak, name):
    # Connecting to database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Modifying data in Habit table
    cursor.execute("UPDATE Habit SET DaysSinceLastCompletion = ?, CurrentStreak = ?, LongestStreak = ? "
                   "WHERE HabitName = ?", (days_since_last_completion, current_streak, longest_streak, name))
    conn.commit()

    # Closing the cursor and the connection
    cursor.close()
    conn.close()


def sql_update_habit_execution_data(habit_name):
    # Storing current datetime in a variable
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving the habit ID corresponding to the given habit name
    cursor.execute(f"SELECT ID FROM Habit WHERE HabitName = '{habit_name}'")
    habit_ID = cursor.fetchone()[0]

    # Inserting a new execution for  a habit
    cursor.execute(f"INSERT INTO HabitExecution (HabitID, DateTime) VALUES ({habit_ID}, '{current_datetime}')")

    # Committing the changes and closing the cursor and the connection
    conn.commit()
    cursor.close()
    conn.close()


def sql_check_if_habit_already_completed(habit_name):
    # Storing current datetime in a variable
    current_datetime = datetime.datetime.now()

    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving the habit ID corresponding to the given habit name
    cursor.execute(f"SELECT ID FROM Habit WHERE HabitName = '{habit_name}'")
    habit_ID = cursor.fetchone()[0]

    # Retrieving latest habit execution date from HabitExecution table
    cursor.execute(f"SELECT DateTime FROM HabitExecution WHERE HabitID = '{habit_ID}'")
    rows = cursor.fetchall()

    # If previous executions exist, the latest date will be stored in latest_datetime, otherwise it will be set to None
    if rows:
        latest_datetime = rows[-1][0]
        latest_datetime = datetime.datetime.strptime(latest_datetime, '%Y-%m-%d %H:%M:%S')
    else:
        latest_datetime = None
        print("true")
        return True  # No executions for this habit so far, so first execution can be performed

    one_day = datetime.timedelta(days=1)

    if current_datetime >= latest_datetime + one_day:
        print("truer")
        return True  # Last execution is at least 1 day ago
    else:
        print(latest_datetime)
        print("false")
        return False  # Last execution was on the same day, new completion will not advance streak


def check_database():
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

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
    # try:
    #     setup_database()
    # except sql.OperationalError:  # If database already exists, it shouldn't be created again
    #     pass
    # finally:
    #     check_database()
    sql_check_if_habit_already_completed("blah")

