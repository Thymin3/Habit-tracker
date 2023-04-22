import main
import GUI
import database


# Functions passed to main

def create_daily_habit(name, periodicity="daily"):
    """Used for receiving a call from the GUI to create a habit + checking for duplicates in database +
     generating a new habit in the database in case no duplicates exist.

        Since the command was performed by the user over the daily button, the periodicity is set to daily by default.
        The habit name is defined by the user in the entry widget.
        A new habit will be generated in the habit_tracker database in case it does not exist yet."""

    # Passing user input to main logic
    new_habit_name, new_habit_periodicity = main.Habit.create_habit(name, periodicity)

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
        A new habit will be generated in the habit_tracker database in case it does not exist yet."""

    # Passing user input to main logic
    new_habit_name, new_habit_periodicity = main.Habit.create_habit(name, periodicity)

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


def get_habit_list():
    """Receiving habit_names list from database and returning it for the GUI"""
    habit_names = database.sql_return_habit_list()
    # Passing Habit IDs and habit names
    return habit_names


def complete_habit(name):
    # Retrieving data from database
    ID, name, periodicity, days_since_last_completion, current_streak, \
    longest_streak, number_of_breaks = database.sql_return_habit(name)

    # Checking if habit was already completed today
    if database.sql_check_if_habit_already_completed(name):
        # Accessing main logic to modify habit data
        habit = main.Habit(name, periodicity, days_since_last_completion, current_streak, longest_streak,
                           number_of_breaks)
        days_since_last_completion, current_streak, longest_streak, name = main.Habit.complete_habit(habit)

        # Passing completed data back to database
        database.sql_update_habit_data(days_since_last_completion, current_streak, longest_streak, name)
        database.sql_update_habit_execution_data(name)
        return True
    else:
        return False


def pass_streak_data():
    # Retrieving data from database
    total_execution_count, latest_streak = database.sql_get_latest_streak()
    longest_streak = database.sql_get_longest_streak()


# Functions passed to database


def delete_habit(name):
    # Passing user input to main logic
    database.sql_delete_habit(name)


# Show a list of habits
def get_habits():
    pass


def run_GUI():
    app = GUI.Menu()
    app.mainloop()


if __name__ == '__main__':
    run_GUI()
