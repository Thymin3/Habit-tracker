import habit
import GUI
import database
import sqlite3 as sql


# Accessing habit.py to create habits

def create_daily_habit(name, periodicity="daily"):
    """
    Used for receiving a call from the GUI to create a habit + checking for duplicates in database +
    generating a new habit in the database in case no duplicates exist.

    Since the command was performed by the user over the daily button, the periodicity is set to daily by default.
    The habit name is defined by the user in the entry widget.
    A new habit will be generated in the habit_tracker.db database in case it does not exist yet.

    Args:
        name (str): The name of the habit to be created.
        periodicity (str, optional): The periodicity of the habit, defaults to "daily".

    Returns:
        bool: True if the habit already exists in the database, False otherwise.
    """

    # Passing user input to main logic
    new_habit_name, new_habit_periodicity = habit.Habit.create_habit(name, periodicity)

    # Checking habit names in database for duplicates
    current_habit_names = get_habit_list()
    current_habit_names = {name.upper() for name in current_habit_names}
    new_habit_names = current_habit_names.copy()  # Creating a copy of the set
    new_habit_names.add(new_habit_name.upper())  # Trying to add the new habit name to the set
    new_habit_names_len = len(new_habit_names)

    if len(current_habit_names) == new_habit_names_len:  # Comparing set lengths (before vs after addition of new habit)
        return True  # = Duplicate if name already exists in database, GUI will prompt the user to define another name
    else:
        database.sql_create_habit(new_habit_name, new_habit_periodicity)  # Adding habit to database (no duplicate)
        return False  # GUI will notify user of successfully created habit


def create_weekly_habit(name, periodicity="weekly"):
    """
    Used for receiving a call from the GUI to create a habit + checking for duplicates in database +
    generating a new habit in the database in case no duplicates exist.

    Since the command was performed by the user over the weekly button, the periodicity is set to weekly by default.
    The habit name is defined by the user in the entry widget.
    A new habit will be generated in the habit_tracker.db database in case it does not exist yet.

    Args:
        name (str): The name of the habit to be created.
        periodicity (str, optional): The periodicity of the habit, defaults to "daily".

    Returns:
        bool: True if the habit already exists in the database, False otherwise.
    """

    # Passing user input to main logic
    new_habit_name, new_habit_periodicity = habit.Habit.create_habit(name, periodicity)

    # Checking habit names in database for duplicates
    current_habit_names = get_habit_list()
    current_habit_names = {name.upper() for name in current_habit_names}
    new_habit_names = current_habit_names.copy()  # Creating a copy of the set
    new_habit_names.add(new_habit_name.upper())  # Trying to add the new habit name to the set
    new_habit_names_len = len(new_habit_names)

    if len(current_habit_names) == new_habit_names_len:  # Comparing set lengths (before vs after addition of new habit)
        return True  # = Duplicate if name already exists in database, GUI will prompt the user to define another name
    else:
        database.sql_create_habit(new_habit_name, new_habit_periodicity)  # Adding habit to database (no duplicate)
        return False  # GUI will notify user of successfully created habit


# From GUI to database

def complete_habit(name):
    """
    Marks the habit with the given name as completed for today and updates its data in the habit tracker database.

    This function is called when the user completes a habit for the day. It retrieves the habit's data from the
    database, checks whether it has already been completed today, and updates the habit's data in the database
    accordingly. If the habit has not already been completed today, the function updates its data in the database and
    returns True. If the habit has already been completed today, the function does not update its data and returns
    False. Returning False prompts the GUI to inform the User that the habit cannot be completed a second time
    on the same day.

    Args:
        name (str): The name of the habit to be marked as completed.

    Returns:
        bool: True if the habit was successfully marked as completed, False if it had already been completed today.
    """
    # Retrieving data from database
    ID, name, periodicity, days_since_last_completion, current_streak, \
    longest_streak, number_of_breaks = database.sql_return_habit(name)

    # Checking if habit was already completed today
    if database.sql_check_if_habit_already_completed(name):
        # Accessing main logic to modify habit data
        # habit = main.Habit(name, periodicity, days_since_last_completion, current_streak, longest_streak,
        #                    number_of_breaks)
        # days_since_last_completion, current_streak, longest_streak, name = main.Habit.complete_habit(habit)

        # Passing completed data back to database
        database.sql_update_habit_data(days_since_last_completion, current_streak, longest_streak, name)
        database.sql_update_habit_execution_data(name)
        return True
    else:
        return False


def delete_habit(name):
    """
    This function is called when the user wants to delete a habit from the habit tracker.
    It deletes the habit's data from the database, so that the habit will no longer appear
    in the habit tracker's list of habits.

    Args:
        name (str): The name of the habit to be deleted.

    Returns:
        None
    """
    database.sql_delete_habit(name)


# From Database to GUI

# Habit completion
def get_habit_list():
    """
    This function is called when the habit tracker GUI needs to display the dropdown-list of all habits.
    It retrieves the list of all habit names from the database and returns it as a list of strings.

    Returns:
        habit_names (list): A list of all habit names in the habit tracker database.
    """
    habit_names = database.sql_return_habit_list()
    # Passing Habit IDs and habit names
    return habit_names

# Data Analysis
def give_habit_list_by_ID():
    """
    Calls the function "sql_get_habit_list_by_ID" from the database module which in turn retrieves a list of
    habit data from the Habit table in the habit tracker database, sorted by HabitName.
    Prior to that the data in the database is updated.

    Returns:
        List of tuples: Each tuple represents a row from the Habit table, with the data in the following order:
                - ID (int): The unique ID of the habit.
                - HabitName (str): The name of the habit.
                - Periodicity (str): The periodicity of the habit.
                - DaysSinceLastCompletion (int): The number of days since the habit was last completed.
                - CurrentStreak (int): The current streak of days on which the habit has been completed.
                - LongestStreak (int): The longest streak of days on which the habit has been completed.
                - NumberOfBreaks (int): The number of times the habit has been broken.
    """
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_ID()


# Data Analysis
def give_habit_list_daily():
    """
    Calls the function "sql_get_habit_list_daily" from the database module which in turn retrieves a list of
    habit data from the Habit table in the habit tracker database. It hereby only retrieves habits with
    the periodicity "daily".
    Prior to that the data in the database is updated.

    Returns:
        List of tuples: Each tuple represents a row from the Habit table, with the data in the following order:
                - ID (int): The unique ID of the habit.
                - HabitName (str): The name of the habit.
                - Periodicity (str): The periodicity of the habit.
                - DaysSinceLastCompletion (int): The number of days since the habit was last completed.
                - CurrentStreak (int): The current streak of days on which the habit has been completed.
                - LongestStreak (int): The longest streak of days on which the habit has been completed.
                - NumberOfBreaks (int): The number of times the habit has been broken.
    """
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_daily()


# Data Analysis
def give_habit_list_weekly():
    """
    Calls the function "sql_get_habit_list_weekly" from the database module which in turn retrieves a list of
    habit data from the Habit table in the habit tracker database. It hereby only retrieves habits with
    the periodicity "weekly".
    Prior to that the data in the database is updated.

    Returns:
        List of tuples: Each tuple represents a row from the Habit table, with the data in the following order:
                - ID (int): The unique ID of the habit.
                - HabitName (str): The name of the habit.
                - Periodicity (str): The periodicity of the habit.
                - DaysSinceLastCompletion (int): The number of days since the habit was last completed.
                - CurrentStreak (int): The current streak of days on which the habit has been completed.
                - LongestStreak (int): The longest streak of days on which the habit has been completed.
                - NumberOfBreaks (int): The number of times the habit has been broken.
    """
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_weekly()


# Data Analysis
def give_habit_list_by_break_count():
    """
    Calls the function "sql_get_habit_list_by_break_count" from the database module which in turn retrieves a list of
    habit data from the Habit table in the habit tracker database, sorted by the number of breaks in descending order.
    Prior to that the data in the database is updated.

    Returns:
        List of tuples: Each tuple represents a row from the Habit table, with the data in the following order:
                - ID (int): The unique ID of the habit.
                - HabitName (str): The name of the habit.
                - Periodicity (str): The periodicity of the habit.
                - DaysSinceLastCompletion (int): The number of days since the habit was last completed.
                - CurrentStreak (int): The current streak of days on which the habit has been completed.
                - LongestStreak (int): The longest streak of days on which the habit has been completed.
                - NumberOfBreaks (int): The number of times the habit has been broken.
    """
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_break_count()


# Data Analysis
def give_habit_list_by_current_streak():
    """
    Calls the function "sql_get_habit_list_by_current_streak" from the database module which in turn retrieves a list of
    habit data from the Habit table in the habit tracker database, sorted by the current streak in descending order.
    Prior to that the data in the database is updated.

    Returns:
        List of tuples: Each tuple represents a row from the Habit table, with the data in the following order:
                - ID (int): The unique ID of the habit.
                - HabitName (str): The name of the habit.
                - Periodicity (str): The periodicity of the habit.
                - DaysSinceLastCompletion (int): The number of days since the habit was last completed.
                - CurrentStreak (int): The current streak of days on which the habit has been completed.
                - LongestStreak (int): The longest streak of days on which the habit has been completed.
                - NumberOfBreaks (int): The number of times the habit has been broken.
    """
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_current_streak()


# Data Analysis
def give_habit_list_by_longest_streak():
    """
    Calls the function "sql_get_habit_list_by_longest_streak" from the database module which in turn retrieves a list of
    habit data from the Habit table in the habit tracker database, sorted by the longest streak in descending order.
    Prior to that the data in the database is updated.

    Returns:
        List of tuples: Each tuple represents a row from the Habit table, with the data in the following order:
                - ID (int): The unique ID of the habit.
                - HabitName (str): The name of the habit.
                - Periodicity (str): The periodicity of the habit.
                - DaysSinceLastCompletion (int): The number of days since the habit was last completed.
                - CurrentStreak (int): The current streak of days on which the habit has been completed.
                - LongestStreak (int): The longest streak of days on which the habit has been completed.
                - NumberOfBreaks (int): The number of times the habit has been broken.
    """
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_longest_streak()


def run_GUI():
    app = GUI.Menu()
    app.mainloop()


def create_database(percentage):
    try:
        database.setup_database()
        database.delete_random_executions(percentage)
        database.update_database()
    except sql.OperationalError:  # If database already exists, it shouldn't be created again
        pass


if __name__ == '__main__':
    create_database(10)
    run_GUI()
