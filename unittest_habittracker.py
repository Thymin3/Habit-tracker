import sqlite3 as sql


# Returning all rows from habit tracker database in order to test data analysis functions from database module
def check_database():
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from the Habit table
    cursor.execute('''SELECT * FROM Habit''')
    habit_rows = cursor.fetchall()
    print("Habit table (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount):")
    for row in habit_rows:
        print(row)

    # Retrieving data from the HabitExecution table
    cursor.execute('''SELECT * FROM HabitExecution''')
    execution_rows = cursor.fetchall()
    print("\nHabitExecution table (HabitID, ExecutionDateTime):")
    for row in execution_rows:
        print(row)

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    return habit_rows, execution_rows


if __name__ == "__main__":
    check_database()

