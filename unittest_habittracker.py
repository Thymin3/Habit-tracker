import sqlite3 as sql
import datetime
import unittest


# Function for visualization of the Habit table and HabitExecution table records, NOT part of unittest.
# Kept only for troubleshooting.
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


# Assessing data stored in database
def get_habit_rows():
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from the Habit table
    cursor.execute('''SELECT * FROM Habit''')
    habit_rows = cursor.fetchall()

    return habit_rows


def get_execution_rows():
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from the HabitExecution table
    cursor.execute('''SELECT * FROM HabitExecution''')
    execution_rows = cursor.fetchall()

    return execution_rows


def get_execution_dates_per_ID(ID):
    execution_rows = get_execution_rows()
    new_execution_rows = [x for x in execution_rows if x[0] == ID]
    execution_dates = [x[1] for x in new_execution_rows]
    return execution_dates


def get_habit_record(ID):
    habit_record = get_habit_rows()[ID-1]
    return habit_record


def get_numbers_from_single_record(habit_record):
    days_since_last_execution = habit_record[3]
    current_streak = habit_record[4]
    longest_streak = habit_record[5]
    break_count = habit_record[6]

    return days_since_last_execution, current_streak, longest_streak, break_count


# Computing data anew from HabitExecution data (similar functions as the ones in the database)
def get_actual_days_since_last_execution(execution_dates):
    # Calculating how many full days passed since the last execution
    latest_execution_date = execution_dates[-1]
    time_interval = datetime.datetime.now() - datetime.datetime.strptime(latest_execution_date, '%Y-%m-%d %H:%M:%S')
    days_since_last_completion = time_interval.days

    return days_since_last_completion


def get_actual_current_streak(habit_record, execution_dates):
    execution_dates = execution_dates[::-1]  # function in database sorted by descending, therefore order flipped here
    latest_streak = 0
    if habit_record[2] == "daily":
        limit = 1
    else:
        limit = 7  # Periodicity is weekly
    if len(execution_dates) > 0:
        current_date = datetime.datetime.strptime(execution_dates[0], "%Y-%m-%d %H:%M:%S")
        if (datetime.datetime.now() - current_date).days <= limit:  # Latest execution over 24h/ 1 week ago?
            latest_streak = 1
            for i in range(1, len(execution_dates)):
                previous_date = datetime.datetime.strptime(execution_dates[i], "%Y-%m-%d %H:%M:%S")
                if (current_date - previous_date).days <= limit:
                    latest_streak += 1
                    current_date = previous_date
                else:
                    break

    return latest_streak


def get_actual_longest_streak(habit_record, execution_dates):
    current_streak = 0
    longest_streak = 0
    if habit_record[2] == "daily":
        limit = 1
    else:
        limit = 7  # Periodicity is weekly

    for i in range(len(execution_dates)):
        if i == 0:
            current_streak = 1
        else:
            try:
                delta = datetime.datetime.strptime(execution_dates[i], '%Y-%m-%d %H:%M:%S') \
                        - datetime.datetime.strptime(execution_dates[i - 1], '%Y-%m-%d %H:%M:%S')
                if delta.days <= limit:
                    current_streak += 1
                else:
                    current_streak = 1
            except ValueError:
                print((execution_dates[i][1]))

        if current_streak > longest_streak:
            longest_streak = current_streak

    return longest_streak


def get_actual_break_count(habit_record, execution_dates):
    break_count = 0
    if habit_record[2] == "daily":
        limit = 1
    else:
        limit = 7  # Periodicity is weekly
    for i in range(len(execution_dates)):
        current_date = datetime.datetime.strptime(execution_dates[i], '%Y-%m-%d %H:%M:%S')
        if i == 0:
            previous_date = current_date
        else:
            delta = current_date - previous_date
            if delta.days > limit:
                break_count += 1
            previous_date = current_date

    return break_count

class TestCase(unittest.TestCase):
    def setUp(self):
        self.one_execution_dates = get_execution_dates_per_ID(1)
        self.two_execution_dates = get_execution_dates_per_ID(2)
        self.three_execution_dates = get_execution_dates_per_ID(3)
        self.four_execution_dates = get_execution_dates_per_ID(4)
        self.five_execution_dates = get_execution_dates_per_ID(5)

        self.one_days_since_last_execution, self.one_current_streak, self.one_longest_streak, self.one_break_count \
            = get_numbers_from_single_record(get_habit_record(1))

        self.two_days_since_last_execution, self.two_current_streak, self.two_longest_streak, self.two_break_count \
            = get_numbers_from_single_record(get_habit_record(2))

        self.three_days_since_last_execution, self.three_current_streak, self.three_longest_streak, \
        self.three_break_count = get_numbers_from_single_record(get_habit_record(3))

        self.four_days_since_last_execution, self.four_current_streak, self.four_longest_streak, self.four_break_count \
            = get_numbers_from_single_record(get_habit_record(4))

        self.five_days_since_last_execution, self.five_current_streak, self.five_longest_streak, self.five_break_count \
            = get_numbers_from_single_record(get_habit_record(5))

    def test_days_since_last_execution(self):
        self.assertEqual(self.one_days_since_last_execution,
                         get_actual_days_since_last_execution(self.one_execution_dates))
        self.assertEqual(self.two_days_since_last_execution,
                         get_actual_days_since_last_execution(self.two_execution_dates))
        self.assertEqual(self.three_days_since_last_execution,
                         get_actual_days_since_last_execution(self.three_execution_dates))
        self.assertEqual(self.four_days_since_last_execution,
                         get_actual_days_since_last_execution(self.four_execution_dates))
        self.assertEqual(self.five_days_since_last_execution,
                         get_actual_days_since_last_execution(self.five_execution_dates))

    def test_current_streak(self):
        self.assertEqual(self.one_current_streak,
                         get_actual_current_streak(get_habit_record(1), self.one_execution_dates))
        self.assertEqual(self.two_current_streak,
                         get_actual_current_streak(get_habit_record(2), self.two_execution_dates))
        self.assertEqual(self.three_current_streak,
                         get_actual_current_streak(get_habit_record(3), self.three_execution_dates))
        self.assertEqual(self.four_current_streak,
                         get_actual_current_streak(get_habit_record(4), self.four_execution_dates))
        self.assertEqual(self.five_current_streak,
                         get_actual_current_streak(get_habit_record(5), self.five_execution_dates))

    def test_longest_streak(self):
        self.assertEqual(self.one_longest_streak,
                         get_actual_longest_streak(get_habit_record(1), self.one_execution_dates))
        self.assertEqual(self.two_longest_streak,
                         get_actual_longest_streak(get_habit_record(2), self.two_execution_dates))
        self.assertEqual(self.three_longest_streak,
                         get_actual_longest_streak(get_habit_record(3), self.three_execution_dates))
        self.assertEqual(self.four_longest_streak,
                         get_actual_longest_streak(get_habit_record(4), self.four_execution_dates))
        self.assertEqual(self.five_longest_streak,
                         get_actual_longest_streak(get_habit_record(5), self.five_execution_dates))

    def test_break_count(self):
        self.assertEqual(self.one_break_count,
                         get_actual_break_count(get_habit_record(1), self.one_execution_dates))
        self.assertEqual(self.two_break_count,
                         get_actual_break_count(get_habit_record(2), self.two_execution_dates))
        self.assertEqual(self.three_break_count,
                         get_actual_break_count(get_habit_record(3), self.three_execution_dates))
        self.assertEqual(self.four_break_count,
                         get_actual_break_count(get_habit_record(4), self.four_execution_dates))
        self.assertEqual(self.five_break_count,
                         get_actual_break_count(get_habit_record(5), self.five_execution_dates))

if __name__ == "__main__":
    unittest.main()


