import sqlite3 as sql
import datetime
import random
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


def delete_random_executions(percentage):
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Counting the number of rows in the HabitExecution table
    cursor.execute("SELECT COUNT(*) FROM HabitExecution")
    total_rows = cursor.fetchone()[0]

    # Calculating the number of rows to delete
    num_rows_to_delete = int(total_rows * percentage / 100)

    # Selecting a random subset of rows to delete
    cursor.execute(f"SELECT HabitID, DateTime FROM HabitExecution ORDER BY RANDOM() LIMIT {num_rows_to_delete}")
    rows_to_delete = cursor.fetchall()

    # Deleting the selected rows
    for row in rows_to_delete:
        cursor.execute("DELETE FROM HabitExecution WHERE HabitID = ? AND DateTime = ?", row)

    # Closing the cursor and the connection
    conn.commit()
    cursor.close()
    conn.close()


def sql_get_latest_streak(habit_ID):
    # Connecting to database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving the periodicity corresponding to the given habit ID
    cursor.execute(f"SELECT Periodicity FROM Habit WHERE ID = {habit_ID}")
    periodicity = cursor.fetchone()[0]

    # Counting the total number of executions for the habit
    cursor.execute(f"SELECT COUNT(*) FROM HabitExecution WHERE HabitID = {habit_ID}")
    total_execution_count = cursor.fetchone()[0]

    # Getting the latest streak for the habit
    latest_streak = 0
    if periodicity == "daily":
        limit = 1
    else:
        limit = 7  # Periodicity is weekly
    cursor.execute(f"SELECT DateTime FROM HabitExecution WHERE HabitID = {habit_ID} ORDER BY DateTime DESC")
    execution_dates = cursor.fetchall()
    if len(execution_dates) > 0:
        current_date = datetime.datetime.strptime(execution_dates[0][0], "%Y-%m-%d %H:%M:%S")
        if (datetime.datetime.now() - current_date).days <= limit:  # Latest execution over 24h/ 1 week ago?
            latest_streak = 1
            for i in range(1, len(execution_dates)):
                previous_date = datetime.datetime.strptime(execution_dates[i][0], "%Y-%m-%d %H:%M:%S")
                if (current_date - previous_date).days <= limit:
                    latest_streak += 1
                    current_date = previous_date
                else:
                    break

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    return total_execution_count, latest_streak


def sql_get_longest_streak(habit_ID):
    # Connecting to database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving the periodicity corresponding to the given habit ID
    cursor.execute(f"SELECT Periodicity FROM Habit WHERE ID = {habit_ID}")
    periodicity = cursor.fetchone()[0]

    # Getting the longest streak for the habit
    current_streak = 0
    longest_streak = 0
    if periodicity == "daily":
        limit = 1
    else:
        limit = 7  # Periodicity is weekly
    cursor.execute(f"SELECT DateTime FROM HabitExecution WHERE HabitID = {habit_ID} ")
    execution_dates = cursor.fetchall()

    for i in range(len(execution_dates)):
        if i == 0:
            current_streak = 1
        else:
            delta = datetime.datetime.strptime(execution_dates[i][0], '%Y-%m-%d %H:%M:%S') \
                    - datetime.datetime.strptime(execution_dates[i-1][0], '%Y-%m-%d %H:%M:%S')
            if delta.days <= limit:
                current_streak += 1
            else:
                current_streak = 1
        if current_streak > longest_streak:
            longest_streak = current_streak

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    return longest_streak


def sql_get_days_since_completion(habit_ID):
    # Connecting to database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving the latest execution corresponding to the given habit ID
    cursor.execute(f"SELECT DateTime FROM HabitExecution WHERE HabitID = {habit_ID} ORDER BY DateTime DESC")
    execution_date = cursor.fetchone()[0]

    # Calculating how many full days passed since the last execution
    time_interval = datetime.datetime.now() - datetime.datetime.strptime(execution_date, '%Y-%m-%d %H:%M:%S')
    days_since_last_completion = time_interval.days

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    return days_since_last_completion


def sql_get_number_of_breaks(habit_ID):
    # Connecting to database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving the periodicity corresponding to the given habit ID
    cursor.execute(f"SELECT Periodicity FROM Habit WHERE ID = {habit_ID}")
    periodicity = cursor.fetchone()[0]

    # Retrieving the execution dates corresponding to the given habit ID
    cursor.execute(f"SELECT DateTime FROM HabitExecution WHERE HabitID = {habit_ID}")
    execution_dates = cursor.fetchall()

    # Calculating the break count
    break_count = 0
    if periodicity == "daily":
        limit = 1
    else:
        limit = 7  # Periodicity is weekly
    current_streak = 0
    for i in range(len(execution_dates)):
        current_date = datetime.datetime.strptime(execution_dates[i][0], '%Y-%m-%d %H:%M:%S')
        if i == 0:
            previous_date = current_date
            current_streak += 1
        else:
            delta = current_date - previous_date
            if delta.days > limit:
                break_count += 1
                current_streak = 1
            else:
                current_streak += 1
            previous_date = current_date

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    return break_count


def update_database():
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Get all habit IDs
    cursor.execute("SELECT ID FROM Habit")
    habit_IDs = cursor.fetchall()
    habit_IDs = [i[0] for i in habit_IDs]

    # Loop through each habit ID and update the stats
    for i in habit_IDs:
        total_execution_count, latest_streak = sql_get_latest_streak(i)
        longest_streak = sql_get_longest_streak(i)
        days_since_last_completion = sql_get_days_since_completion(i)
        break_count = sql_get_number_of_breaks(i)

        cursor.execute("UPDATE Habit SET DaysSinceLastCompletion=?, CurrentStreak=?, LongestStreak=?, NumberOfBreaks=? "
                       "WHERE ID=?", (days_since_last_completion, latest_streak, longest_streak, break_count, i))

        print(total_execution_count)

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
        return True  # No executions for this habit so far, so first execution can be performed

    one_day = datetime.timedelta(days=1)

    if current_datetime >= latest_datetime + one_day:
        return True  # Last execution is at least 1 day ago
    else:
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
    try:
        setup_database()
        delete_random_executions(50)
        update_database()
    except sql.OperationalError:  # If database already exists, it shouldn't be created again
        pass
    finally:
        check_database()


