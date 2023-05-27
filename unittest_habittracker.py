import sqlite3 as sql
import datetime
import unittest


def check_database():
    """
    Retrieves and displays data from the Habit and HabitExecution tables in the habit_tracker database.

    This function connects to the database, retrieves all the rows from the Habit table, and prints them.
    It then retrieves all the rows from the HabitExecution table and prints them as well.
    Finally, it closes the cursor and the database connection.
    It basically combines the functions get_habit_rows and get_execution_rows but directly prints the rows instead of
    returning them in a variable.

    Note:
    - The function assumes that the database file "habit_tracker.db" exists in the current directory. If there is no
    database, it is required to run the habit tracker application for the first time. This will create the database.
    - This function was used during the development process and is not part of the unittests. It is only kept for
    the sake of troubleshooting. It can be used to quickly get an overview of the database without relying on the
    habit tracker application itself.
    """
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
    """
    Retrieves all rows from the Habit table in the habit_tracker.db database.

    This function connects to the database, executes a query to retrieve all the rows from the Habit table,
    and returns the result.

    Note:
    The function assumes that the database file "habit_tracker.db" exists in the current directory. If there is no
    database, it is required to run the habit tracker application for the first time. This will create the database.

    Returns:
    list: A list of tuples representing the rows retrieved from the Habit table.
          Each tuple contains the following columns: (HabitID, Name, Periodicity, DaysSinceLastExecution,
          CurrentStreak, LongestSteak, BreakCount).
    """
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from the Habit table
    cursor.execute('''SELECT * FROM Habit''')
    habit_rows = cursor.fetchall()

    return habit_rows


def get_execution_rows():
    """
    Retrieves all rows from the HabitExecution table in the habit_tracker.db database.

    This function connects to the database, executes a query to retrieve all the rows from the HabitExecution table,
    and returns the result.

    Note:
    The function assumes that the database file "habit_tracker.db" exists in the current directory. If there is no
    database, it is required to run the habit tracker application for the first time. This will create the database.

    Returns:
    list: A list of tuples representing the rows retrieved from the HabitExecution table.
         Each tuple contains the following columns: (HabitID, ExecutionDateTime).
    """
    # Connecting to the database
    conn = sql.connect("habit_tracker.db")

    # Creating a cursor
    cursor = conn.cursor()

    # Retrieving data from the HabitExecution table
    cursor.execute('''SELECT * FROM HabitExecution''')
    execution_rows = cursor.fetchall()

    return execution_rows


def get_execution_dates_per_ID(ID):
    """
    Retrieves the execution dates associated with a specific ID from the HabitExecution table.

    This function calls the "get_execution_rows" function to retrieve all the rows from the HabitExecution table.
    It filters the rows based on the given ID and extracts the corresponding execution dates.
    The extracted execution dates are returned as a list.

    Args:
    - ID (int): The ID for which execution dates are to be retrieved.

    Returns:
    list: A list of execution dates associated with the given ID.
    """
    execution_rows = get_execution_rows()
    new_execution_rows = [x for x in execution_rows if x[0] == ID]
    execution_dates = [x[1] for x in new_execution_rows]
    return execution_dates


def get_habit_record(ID):
    """
    Retrieves the habit record associated with a specific ID from the Habit table.

    This function calls the "get_habit_rows" function to retrieve all the rows from the Habit table.
    It retrieves the habit record based on the given ID by indexing the list of habit rows.
    The habit record is returned as a tuple containing the columns: (HabitID, Name, Periodicity,
    DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount).

    Args:
    - ID (int): The ID of the habit for which the record is to be retrieved.

    Returns:
    tuple: The habit record associated with the given ID. The record contains the following columns:
           (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount).
    """
    habit_record = get_habit_rows()[ID-1]
    return habit_record


def get_numbers_from_single_record(habit_record):
    """
    Retrieves specific numbers from a single habit record.

    This function takes a habit record as input, which is a tuple containing the columns: (HabitID, Name,
    Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount). It extracts and returns
    specific numbers from the habit record, including the days since the last execution, the current streak,
    the longest streak, and the break count.

    Args:
    - habit_record (tuple): A habit record containing the following columns:
        (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount). This tuple can be
        provided through the "get_habit_record" function.

    Returns:
    tuple: A tuple containing the following numbers extracted from the habit record:
           (days_since_last_execution, current_streak, longest_streak, break_count).
    """
    days_since_last_execution = habit_record[3]
    current_streak = habit_record[4]
    longest_streak = habit_record[5]
    break_count = habit_record[6]

    return days_since_last_execution, current_streak, longest_streak, break_count


# Computing data anew from HabitExecution data (similar functions as the ones used in the database module)
def get_actual_days_since_last_execution(execution_dates):
    """
    Calculates the actual number of days that have passed since the last execution.

    This function takes a list of execution dates as input and calculates the number of full days that
    have passed since the last execution. It uses the latest execution date from the list and the current
    date and time to calculate the time interval. The calculated number of days since the last completion
    is returned as an integer.
    It is similar to the function "sql_get_days_since_completion" from the database module.

    Args:
    - execution_dates (list): A list of execution dates in the format '%Y-%m-%d %H:%M:%S'
    The list will be provided by the function "get_execution_dates_per_ID" which in turn takes the ID of a habit as
    argument.

    Returns:
    int: The actual number of days that have passed since the last execution.
    """
    # Calculating how many full days passed since the last execution
    latest_execution_date = execution_dates[-1]
    time_interval = datetime.datetime.now() - datetime.datetime.strptime(latest_execution_date, '%Y-%m-%d %H:%M:%S')
    days_since_last_completion = time_interval.days

    return days_since_last_completion


def get_actual_current_streak(habit_record, execution_dates):
    """
    Calculates the actual current streak for a habit.

    This function takes a habit record and a list of execution dates as input and calculates the actual
    current streak for the habit.
    The habit record is expected to contain the columns: (HabitID, Name,
    Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount) and is provided by the function
    "get_habit_record". It is needed for the periodicity value.
    The execution dates list is provided by the function "get_execution_dates_per_ID" and represents the dates on which
    the habit was executed, in the format "%Y-%m-%d %H:%M:%S".

    The function first reverses the order of the execution dates since the similar database module
    function "get_latest_streak" sorts them in descending order. It then initializes the latest streak count to 0.
    The limit for a streak is determined based on the periodicity of the habit.
    If the periodicity is "daily", the limit is set to 1,
    otherwise, if the periodicity is "weekly", the limit is set to 7.

    The function then checks if there are any execution dates available. If there are, it compares the difference
    between the current date and the first execution date to the limit. If the difference is within the limit,
    indicating that the habit was executed within the allowed time range, the latest streak count is set to 1.

    The function iterates through the remaining execution dates and checks if the difference between the current
    date and the previous date is within the limit. If it is, the latest streak count is incremented, and the
    current date is updated. If the difference exceeds the limit, the loop breaks.

    Finally, the latest streak count, representing the actual current streak for the habit, is returned as an integer.

    The function mimics the database module function "sql_get_latest_streak".

    Args:
    - habit_record (tuple): A habit record containing the following columns:
                          (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount).
                          This list is provided by the function "get_habit_record" which takes the ID of a habit as an
                          argument.
    - execution_dates (list): A list of execution dates in the format "%Y-%m-%d %H:%M:%S". This list is provided by
                            the function "get_execution_dates_per_ID" which takes the ID of a habit as an argument.

    Returns:
    int: The actual current streak for the habit.
    """
    # Function in database sorted by descending, therefore order flipped here.
    # This will also make sure that the latest loop is tracked, not the first.
    execution_dates = execution_dates[::-1]
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
    """
    Calculates the actual longest streak for a habit.

    This function takes a habit record and a list of execution dates as input and calculates the actual longest streak
    for the habit. The habit record is expected to contain the columns: (HabitID, Name, Periodicity,
    DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount) and is provided by the function
    "get_habit_record". It is needed for the periodicity value.
    The execution dates list is provided by the function "get_execution_dates_per_ID" and represents the dates
    on which the habit was executed, in the format "%Y-%m-%d %H:%M:%S".

    The function first initializes the current streak and longest streak counts to 0.
    The limit for a streak is determined based on the periodicity of the habit.
    If the periodicity is "daily", the limit is set to 1; otherwise, if the periodicity is "weekly",
    the limit is set to 7.

    The function then iterates through the execution dates. For the first date, the current streak is set to 1. For
    subsequent dates, the function calculates the time difference between the current date and the previous date using
    the "datetime.strptime" function. If the difference in days is within the limit, indicating that the habit was
    executed within the allowed time range, the current streak is incremented. Otherwise, the current streak is reset
    to 1.

    The function keeps track of the longest streak encountered so far by comparing the current streak to the longest
    streak. If the current streak is greater than the longest streak, the longest streak is updated.
    It mimics the database module function "sql_get_longest_streak"

    Finally, the longest streak count, representing the actual longest streak for the habit, is returned as an integer.

    Args:
    - habit_record (tuple): A habit record containing the following columns:
                            (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak,
                            BreakCount).
                            This record is provided by the function "get_habit_record" which takes the ID of a habit as
                            an argument.
    - execution_dates (list): A list of execution dates in the format '%Y-%m-%d %H:%M:%S'. This list is provided by
                              the function "get_execution_dates_per_ID" which takes the ID of a habit as an argument.

    Returns:
    longest_streak (int): The actual longest streak for the habit.
    """
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
            delta = datetime.datetime.strptime(execution_dates[i], '%Y-%m-%d %H:%M:%S') \
                    - datetime.datetime.strptime(execution_dates[i - 1], '%Y-%m-%d %H:%M:%S')
            if delta.days <= limit:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 1
        if current_streak > longest_streak:  # Necessary if there have not been any breaks, otherwise longest stays 0
            longest_streak = current_streak

    return longest_streak


def get_actual_break_count(habit_record, execution_dates):
    """
    Calculates the actual break count for a habit.

    This function takes a habit record and a list of execution dates as input and calculates the actual break count
    for the habit. The habit record is expected to contain the columns: (HabitID, Name, Periodicity,
    DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount) and is provided by the function
    "get_habit_record". It is needed for the periodicity value.
    The execution dates list is provided by the function
    "get_execution_dates_per_ID" and represents the dates on which the habit was executed, in the format
    "%Y-%m-%d %H:%M:%S".

    The function initializes the break count to 0. The limit for a break is determined based on the periodicity of the
    habit. If the periodicity is "daily", the limit is set to 1; otherwise, if the periodicity is "weekly", the limit
    is set to 7.

    The function iterates through the execution dates. For the first date, the previous date is set to the current
    date. For subsequent dates, the function calculates the time difference (delta) between the current date and the
    previous date. If the difference in days is greater than the limit, indicating a break in habit execution, the
    break count is incremented. The previous date is updated to the current date.

    Finally, the break count, representing the actual number of breaks in habit execution, is returned as an integer.

    The function mimics the database module function "sql_get_longest_streak".

    Args:
    - habit_record (tuple): A habit record containing the following columns:
                            (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestStreak,
                            BreakCount).
                            This record is provided by the function "get_habit_record" which takes the ID of a habit as
                            an argument.
    - execution_dates (list): A list of execution dates in the format '%Y-%m-%d %H:%M:%S'. This list is provided by
                              the function "get_execution_dates_per_ID" which takes the ID of a habit as an argument.

    Returns:
    break_count (int): The actual break count for the habit.
    """
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


