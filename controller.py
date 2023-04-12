import main
import GUI
import database

# Functions passed to main

def create_daily_habit(name, periodicity="daily"):
    """Used for receiving a call from the GUI to create a habit + generating a new habit in the database.

        Since the command was performed by the user over the daily button, the periodicity is set to daily by default.
        The habit name is defined by the user in the entry widget.
        A new habit will be generated in the habit_tracker database"""

    # Passing user input to main logic
    new_habit_name, new_habit_periodicity = main.Habit.create_habit(name, periodicity)
    database.sql_create_habit(new_habit_name, new_habit_periodicity)


def create_weekly_habit(name, periodicity="weekly"):
    """Used for receiving a call from the GUI to create a habit + generating a new habit in the database.

        Since the command was performed by the user over the weekly button, the periodicity is set to weekly by default.
        The habit name is defined by the user in the entry widget.
        A new habit will be generated in the habit_tracker database"""

    # Passing user input to main logic
    new_habit_name, new_habit_periodicity = main.Habit.create_habit(name, periodicity)
    database.sql_create_habit(new_habit_name, new_habit_periodicity)


def get_habit_list():
    """Receiving habit_names list from database and returning it for the GUI"""
    habit_names = database.sql_return_habit_list()
    # Passing Habit IDs and habit names
    return habit_names


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
