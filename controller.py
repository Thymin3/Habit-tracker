import main
import GUI
import database

# Functions passed to main
def create_daily_habit(name, periodicity="daily"):
    print(name)
    # Pass user input to main logic
    main.Habit.create_habit(name, periodicity)

def create_weekly_habit(name, periodicity="weekly"):
    name = GUI.Menu.create_weekly_habit()
    # Pass user input to main logic
    main.Habit.create_habit(name, periodicity)

def delete_habit(name):
    # Pass user input to main logic
    main.Habit.delete_habit(name)

# Show a list of habits
def get_habits():
    pass

def run_GUI():
    app = GUI.Menu()
    app.mainloop()

if __name__ == '__main__':
    run_GUI()
