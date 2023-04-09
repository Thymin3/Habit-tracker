import main
from main import Habit
import GUI
import database

class Controller:


    def __init__(self):
        self.selected_option = None

    def update_selected_option(self, selected_option):
        self.selected_option = selected_option
        print(selected_option)


# Functions passed to main
def create_habit(name):
    # Pass user input to main logic
    Habit.create_habit(name)
    return name

def delete_habit(name):
    # Pass user input to main logic
    Habit.delete_habit(name)

def run_GUI():
    app = GUI.Menu()
    app.mainloop()

# Functions passed to GUI
