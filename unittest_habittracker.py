import sqlite3 as sql
import unittest
from database import sql_get_days_since_completion
from database import sql_get_latest_streak
from database import sql_get_longest_streak
from database import sql_get_number_of_breaks


def check_database():
    """
    Retrieves and displays data from the Habit and HabitExecution tables in the habit_tracker database.

    This function connects to the database, retrieves all the rows from the Habit table, and prints them.
    It then retrieves all the rows from the HabitExecution table and prints them as well.
    Finally, it closes the cursor and the database connection.

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
    cursor.execute("SELECT * FROM Habit")
    habit_rows = cursor.fetchall()
    print("Habit table (HabitID, Name, Periodicity, DaysSinceLastExecution, CurrentStreak, LongestSteak, BreakCount):")
    for row in habit_rows:
        print(row)

    # Retrieving data from the HabitExecution table
    cursor.execute("SELECT * FROM HabitExecution")
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
    cursor.execute("SELECT * FROM Habit")
    habit_rows = cursor.fetchall()

    return habit_rows


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


class TestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by initializing the necessary variables.

        This method is called before each test method in the TestCase class. It sets up the required variables for
        performing the tests.

        The method initializes the following variables:

        - one_days_since_last_execution, one_current_streak, one_longest_streak, one_break_count: The numbers extracted
          from the habit record for habit ID 1 using the function get_numbers_from_single_record and get_habit_record.
          These numbers represent DaysSinceLastExecution, CurrentStreak, LongestStreak, and BreakCount.

        - two_days_since_last_execution, two_current_streak, two_longest_streak, two_break_count: The numbers extracted
          from the habit record for habit ID 2 using the function get_numbers_from_single_record and get_habit_record.
          These numbers represent DaysSinceLastExecution, CurrentStreak, LongestStreak, and BreakCount.

        - three_days_since_last_execution, three_current_streak, three_longest_streak, three_break_count: The numbers
          extracted from the habit record for habit ID 3 using the function get_numbers_from_single_record and
          get_habit_record.
          These numbers represent DaysSinceLastExecution, CurrentStreak, LongestStreak, and BreakCount.

        - four_days_since_last_execution, four_current_streak, four_longest_streak, four_break_count: The numbers
          extracted from the habit record for habit ID 4 using the function get_numbers_from_single_record and
          get_habit_record.
          These numbers represent DaysSinceLastExecution, CurrentStreak, LongestStreak, and BreakCount.

        - five_days_since_last_execution, five_current_streak, five_longest_streak, five_break_count: The numbers
          extracted from the habit record for habit ID 5 using the function get_numbers_from_single_record and
          get_habit_record.
          These numbers represent DaysSinceLastExecution, CurrentStreak, LongestStreak, and BreakCount.
        """

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
        """
        Test case for the "sql_get_days_since_completion" function from the database module.

        This test case verifies that the "sql_get_days_since_completion" function returns the correct number of days
        since the last execution for each habit. It compares the returned value with the expected value obtained from
        the database.

        The test is performed for the following habits:
        - Habit ID 1: The expected days since last execution is compared with the result of
        "sql_get_days_since_completion" using the habit ID 1.
        - Habit ID 2: The expected days since last execution is compared with the result of
        "sql_get_days_since_completion" using the habit ID 2.
        - Habit ID 3: The expected days since last execution is compared with the result of
        "sql_get_days_since_completion" using the habit ID 3.
        - Habit ID 4: The expected days since last execution is compared with the result of
        "sql_get_days_since_completion" using the habit ID 4.
        - Habit ID 5: The expected days since last execution is compared with the result of
        "sql_get_days_since_completion" using the habit ID 5.

        If all the assertions pass, it indicates that the "sql_get_days_since_completion" function returns the correct
        number of days since the last execution for each habit.
        """
        self.assertEqual(self.one_days_since_last_execution,
                         sql_get_days_since_completion(1))
        self.assertEqual(self.two_days_since_last_execution,
                         sql_get_days_since_completion(2))
        self.assertEqual(self.three_days_since_last_execution,
                         sql_get_days_since_completion(3))
        self.assertEqual(self.four_days_since_last_execution,
                         sql_get_days_since_completion(4))
        self.assertEqual(self.five_days_since_last_execution,
                         sql_get_days_since_completion(5))

    def test_current_streak(self):
        """
        Test case for the "sql_get_latest_streak" function from the database module.

        This test case verifies that the "sql_get_latest_streak" function returns the correct current streak value for each
        habit. It compares the returned value with the expected value obtained from the database.

        The test is performed for the following habits:
        - Habit ID 1: The expected current streak is compared with the result of "sql_get_latest_streak"
        using the habit ID 1.
        - Habit ID 2: The expected current streak is compared with the result of "sql_get_latest_streak"
        using the habit ID 2.
        - Habit ID 3: The expected current streak is compared with the result of "sql_get_latest_streak"
        using the habit ID 3.
        - Habit ID 4: The expected current streak is compared with the result of "sql_get_latest_streak"
        using the habit ID 4.
        - Habit ID 5: The expected current streak is compared with the result of "sql_get_latest_streak"
        using the habit ID 5.

        If all the assertions pass, it indicates that the "sql_get_latest_streak" function returns the correct current
        streak value for each habit.
        """
        # sql_get_latest_streak returns two variables in a tuple. Second entry = current streak. Therefore "[1]"
        self.assertEqual(self.one_current_streak,
                         sql_get_latest_streak(1)[1])
        self.assertEqual(self.two_current_streak,
                         sql_get_latest_streak(2)[1])
        self.assertEqual(self.three_current_streak,
                         sql_get_latest_streak(3)[1])
        self.assertEqual(self.four_current_streak,
                         sql_get_latest_streak(4)[1])
        self.assertEqual(self.five_current_streak,
                         sql_get_latest_streak(5)[1])

    def test_longest_streak(self):
        """
        Test case for the "sql_get_longest_streak" function from the database module.

        This test case verifies that the "sql_get_longest_streak" function returns the correct longest streak value for each
        habit. It compares the returned value with the expected value obtained from the database.

        The test is performed for the following habits:
        - Habit ID 1: The expected longest streak is compared with the result of "sql_get_longest_streak"
        using the habit ID 1.
        - Habit ID 2: The expected longest streak is compared with the result of "sql_get_longest_streak"
        using the habit ID 2.
        - Habit ID 3: The expected longest streak is compared with the result of "sql_get_longest_streak"
        using the habit ID 3.
        - Habit ID 4: The expected longest streak is compared with the result of "sql_get_longest_streak"
        using the habit ID 4.
        - Habit ID 5: The expected longest streak is compared with the result of "sql_get_longest_streak"
        using the habit ID 5.

        If all the assertions pass, it indicates that the "sql_get_longest_streak" function returns the correct longest
        streak value for each habit.
        """
        self.assertEqual(self.one_longest_streak,
                         sql_get_longest_streak(1))
        self.assertEqual(self.two_longest_streak,
                         sql_get_longest_streak(2))
        self.assertEqual(self.three_longest_streak,
                         sql_get_longest_streak(3))
        self.assertEqual(self.four_longest_streak,
                         sql_get_longest_streak(4))
        self.assertEqual(self.five_longest_streak,
                         sql_get_longest_streak(5))

    def test_break_count(self):
        """
        Test case for the "sql_get_number_of_breaks" function from the database module.

        This test case verifies that the "sql_get_number_of_breaks" function returns the correct number of breaks for
        each habit. It compares the returned value with the expected value obtained from the database.

        The test is performed for the following habits:
        - Habit ID 1: The expected number of breaks is compared with the result of "sql_get_number_of_breaks"
        using the habit ID 1.
        - Habit ID 2: The expected number of breaks is compared with the result of "sql_get_number_of_breaks"
        using the habit ID 2.
        - Habit ID 3: The expected number of breaks is compared with the result of "sql_get_number_of_breaks"
        using the habit ID 3.
        - Habit ID 4: The expected number of breaks is compared with the result of "sql_get_number_of_breaks"
        using the habit ID 4.
        - Habit ID 5: The expected number of breaks is compared with the result of "sql_get_number_of_breaks"
        using the habit ID 5.

        If all the assertions pass, it indicates that the "sql_get_number_of_breaks" function returns the correct
        number of breaks for each habit.
        """
        self.assertEqual(self.one_break_count,
                         sql_get_number_of_breaks(1))
        self.assertEqual(self.two_break_count,
                         sql_get_number_of_breaks(2))
        self.assertEqual(self.three_break_count,
                         sql_get_number_of_breaks(3))
        self.assertEqual(self.four_break_count,
                         sql_get_number_of_breaks(4))
        self.assertEqual(self.five_break_count,
                         sql_get_number_of_breaks(5))

if __name__ == "__main__":
    unittest.main()


