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
    """Used for receiving a call from the GUI to create a habit + checking for duplicates in database +
     generating a new habit in the database in case no duplicates exist.

        Since the command was performed by the user over the weekly button, the periodicity is set to weekly by default.
        The habit name is defined by the user in the entry widget.
        A new habit will be generated in the habit_tracker.db database in case it does not exist yet."""

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
    # Deleting habit data from database
    database.sql_delete_habit(name)


# From Database to GUI

# Habit completion
def get_habit_list():
    """Receiving habit_names list from database and returning it for the GUI"""
    habit_names = database.sql_return_habit_list()
    # Passing Habit IDs and habit names
    return habit_names

# Data Analysis
def give_habit_list_by_ID():
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_ID()


# Data Analysis
def give_habit_list_daily():
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_daily()


# Data Analysis
def give_habit_list_weekly():
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_weekly()


# Data Analysis
def give_habit_list_by_break_count():
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_break_count()


# Data Analysis
def give_habit_list_by_current_streak():
    # Updating streak and break data in database
    database.update_database()

    return database.sql_get_habit_list_by_current_streak()


# Data Analysis
def give_habit_list_by_longest_streak():
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
