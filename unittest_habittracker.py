import unittest
import sqlite3 as sql
from datetime import datetime, timedelta
from database import sql_get_latest_streak

# Define a helper function to insert HabitExecution rows
def insert_habit_execution(habit_ID, date_string):
    conn = sql.connect("habit_tracker.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO HabitExecution (HabitID, DateTime) VALUES ({habit_ID}, '{date_string}')")
    conn.commit()
    cursor.close()
    conn.close()

class TestSQLGetStreakData(unittest.TestCase):
    def setUp(self):
        # Create a new database and insert test data
        conn = sql.connect("habit_tracker.db")
        cursor = conn.cursor()

        # Create Habit table
        cursor.execute("""
            CREATE TABLE Habit (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                HabitName TEXT NOT NULL,
                Periodicity TEXT NOT NULL
            )
        """)

        # Create HabitExecution table
        cursor.execute("""
            CREATE TABLE HabitExecution (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                HabitID INTEGER NOT NULL,
                DateTime TEXT NOT NULL,
                FOREIGN KEY (HabitID) REFERENCES Habit(ID)
            )
        """)

        # Insert test data
        cursor.execute("INSERT INTO Habit (HabitName, Periodicity) VALUES ('daily_habit', 'daily')")
        habit_ID = cursor.lastrowid
        insert_habit_execution(habit_ID, "2023-04-20 10:00:00")
        insert_habit_execution(habit_ID, "2023-04-21 10:00:00")

        cursor.execute("INSERT INTO Habit (HabitName, Periodicity) VALUES ('weekly_habit', 'weekly')")
        habit_ID = cursor.lastrowid
        insert_habit_execution(habit_ID, "2023-04-15 10:00:00")
        insert_habit_execution(habit_ID, "2023-04-22 10:00:00")

        conn.commit()
        cursor.close()
        conn.close()

    def test_daily_habit_streak(self):
        streak = sql_get_streak_data("test_habit")
        self.assertEqual(streak, 2)

    def test_weekly_habit_streak(self):
        streak = sql_get_streak_data("weekly_habit")
        self.assertEqual(streak, 1)

    def tearDown(self):
        # Delete the test database
        import os
        os.remove("habit_tracker.db")

if __name__ == '__main__':
    unittest.main()
