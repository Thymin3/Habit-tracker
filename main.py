
import GUI
import sqlite3 as sql
import sql_python_interface as sqlint


class Habit:
    habit_list = ("a", "b", "c", "d")
    def __init__(self):
        self.habit_list = ("a", "b", "c", "d")

   # def create_daily_habit(self):
    #    input_daily = Menu.get_input_daily()
     #   return input_daily


if __name__ == '__main__':

    app = GUI.Menu()

    # Link button click to a function in main script
    #app.button_create_habit.config(command=do_something)
    app.mainloop()
