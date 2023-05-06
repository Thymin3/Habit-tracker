import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import controller


class Menu(tk.Tk):

    def __init__(self):
        super().__init__()

        # Setting up window
        self.title("Habit Tracker")
        self.geometry("1400x400")

        # Defining widgets
        # General widgets
        self.button_back = tk.Button(self, text="Back to main menu", command=self.back_click)
        self.confirm_button = tk.Button(self, text="confirm")
        self.dropdown_habit_list = ttk.Combobox(self, values=controller.get_habit_list())

        # Main menu
        self.label = tk.Label(self, text="Main menu", font=30)
        self.button_create_habit = tk.Button(self, text="Create habit", command=self.create_click)
        self.button_delete_habit = tk.Button(self, text="Delete habit", command=self.delete_click)
        self.button_complete_habit = tk.Button(self, text="Complete habit", command=self.complete_click)
        self.button_analyze_habits = tk.Button(self, text="Analyze habits", command=self.analyze_click)
        self.button_exit = tk.Button(self, text="Exit", command=self.exit_click)

        # Creation menu
        self.button_daily = tk.Button(self, text="Create daily habit", command=self.daily_click)
        self.button_weekly = tk.Button(self, text="Create weekly habit", command=self.weekly_click)
        self.create_habit_daily = tk.Button(self, text="Create habit", command=self.create_daily_habit)
        self.create_habit_weekly = tk.Button(self, text="Create habit", command=self.create_weekly_habit)
        self.input_field_daily = tk.Entry(self)
        self.input_field_weekly = tk.Entry(self)

        # Deletion menu
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_habit)

        # Completion menu
        self.complete_button = tk.Button(self, text="Complete for today", command=self.complete_habit)

        # Data analysis menu
        # Buttons
        self.show_habit_table_button = tk.Button(self, text="Show habit table", command=self.show_habit_table)
        self.show_habits_daily_button = tk.Button(self, text="Show daily habits", command=self.show_habit_table_daily)
        self.show_habits_weekly_button = tk.Button(self, text="Show weekly habits",
                                                   command=self.show_habit_table_weekly)
        self.show_habits_with_most_breaks = tk.Button(self, text="Show habits that are hardest to keep up with",
                                                      command=self.show_habits_with_most_breaks)
        self.show_habits_with_longest_current_streak = tk.Button(self, text="Show habits with currently longest streak",
                                                                 command=self.show_habits_with_longest_current_streak)
        self.show_habit_with_longest_streak_overall = tk.Button(self, text="Show habits with longest streak overall",
                                                                command=self.show_habits_with_longest_longest_streak)
        self.back_to_analyze_menu_button = tk.Button(self, text="Back to data analysis menu",
                                                     command=self.analyze_click)
        # Habit Table
        self.habit_table = ttk.Treeview(self, columns=("habit_name", "periodicity", "days_since_last_execution",
                                                       "current_streak", "longest_streak", "number_of_breaks"))

        # Defining column headings for habit table
        self.habit_table.heading("habit_name", text="Habit name")
        self.habit_table.heading("periodicity", text="Periodicity")
        self.habit_table.heading("days_since_last_execution", text="Days since last execution")
        self.habit_table.heading("current_streak", text="Current streak")
        self.habit_table.heading("longest_streak", text="Longest streak")
        self.habit_table.heading("number_of_breaks", text="Number of breaks")

        # Packing widgets of main menu
        self.label.pack()
        self.button_create_habit.pack()
        self.button_delete_habit.pack()
        self.button_complete_habit.pack()
        self.button_analyze_habits.pack()
        self.button_exit.pack()

    # Main menu methods
    def create_click(self):
        # Remove widgets and set label to creation menu
        self.remove_all_widgets()
        self.label.configure(text="Creation Menu")

        # Pack widgets
        self.label.pack()
        self.button_daily.pack()
        self.button_weekly.pack()
        self.button_back.pack()

    def delete_click(self):
        # Remove widgets and adjust label
        self.remove_all_widgets()
        self.label.configure(text="Which habit would you like to delete?")

        # Pack widgets
        self.label.pack()
        self.dropdown_habit_list.pack()
        self.delete_button.pack()
        self.button_back.pack()

    def complete_click(self):
        # Remove widgets and adjust label
        self.remove_all_widgets()
        self.label.configure(text="Which habit did you complete today?")

        # Pack widgets
        self.label.pack()
        self.dropdown_habit_list.pack()
        self.complete_button.pack()
        self.button_back.pack()

    def analyze_click(self):
        # Remove widgets and adjust label
        self.remove_all_widgets()
        self.label.configure(text="Data analysis Menu")

        # Pack widgets
        self.label.pack()
        self.show_habit_table_button.pack()
        self.show_habits_daily_button.pack()
        self.show_habits_weekly_button.pack()
        self.show_habits_with_most_breaks.pack()
        self.show_habits_with_longest_current_streak.pack()
        self.show_habit_with_longest_streak_overall.pack()
        self.button_back.pack()

    def exit_click(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    # Creation menu methods
    def daily_click(self):
        # Remove creation menu buttons and adjusting label
        self.remove_all_widgets()
        self.label.configure(text="Please type in the name of your new daily habit:")

        # Pack widget
        self.label.pack()
        self.input_field_daily.pack()
        self.create_habit_daily.pack()
        self.button_back.pack()

    def weekly_click(self):
        # Remove creation menu buttons and adjusting label
        self.remove_all_widgets()
        self.label.configure(text="Please type in the name of your new weekly habit:")

        # Pack widgets
        self.label.pack()
        self.input_field_weekly.pack()
        self.create_habit_weekly.pack()
        self.button_back.pack()

    # Getting user input for habit name and passing it to controller
    def create_daily_habit(self):
        new_habit = self.input_field_daily.get()

        # Calling the create_habit function in the controller module and checking for unique name in database
        if controller.create_daily_habit(new_habit):
            self.label.configure(text="Habit already exists. Please use another name.")
        else:
            # Removing widgets and adjusting label
            self.input_field_daily.pack_forget()
            self.create_habit_daily.pack_forget()
            self.label.configure(text="Daily habit created!")

        # Updating habit dropdown menu
        self.dropdown_habit_list = ttk.Combobox(self, values=controller.get_habit_list())

    def create_weekly_habit(self):
        new_habit = self.input_field_weekly.get()

        # Calling the create_habit function in the controller module and checking for unique name in database
        if controller.create_weekly_habit(new_habit):
            self.label.configure(text="Habit already exists. Please use another name.")
        else:
            # Removing widgets and adjusting label
            self.input_field_weekly.pack_forget()
            self.create_habit_weekly.pack_forget()
            self.label.configure(text="Weekly habit created!")

        # Updating habit dropdown menu
        self.dropdown_habit_list = ttk.Combobox(self, values=controller.get_habit_list())

    # Deletion menu methods
    def delete_habit(self):
        habit_to_delete = self.dropdown_habit_list.get()
        # Removing widgets and adjusting label
        self.remove_all_widgets()
        self.label.configure(text="Habit deleted.")
        self.label.pack()
        self.button_back.pack()

        # Letting controller delete the selected habit
        controller.delete_habit(habit_to_delete)

        # Updating habit dropdown menu
        self.dropdown_habit_list = ttk.Combobox(self, values=controller.get_habit_list())

    # Completion menu methods
    def complete_habit(self):
        habit_to_complete = self.dropdown_habit_list.get()

        # Removing widgets, adjusting label and packing back button
        self.remove_all_widgets()
        self.label.configure(text="Habit completed.")
        self.label.pack()
        self.button_back.pack()

        # Letting controller update the selected habit
        if controller.complete_habit(habit_to_complete):
            pass
        else:
            self.several_completions_one_day()

    # Message prompted when habit has already been fulfilled on the same day
    def several_completions_one_day(self):
        self.label.configure(text="Habit already completed today. \nPlease wait until tomorrow to complete it again.")
        self.label.pack()

    # Data analysis menu methods
    def show_habit_table(self):
        # Removing all widgets
        self.remove_all_widgets()

        # Deleting all potentially existing rows from habit table
        self.habit_table.delete(*self.habit_table.get_children())

        # Adding data to the habit table
        for i, row in enumerate(controller.give_habit_list_by_ID()):
            self.habit_table.insert(parent='', index='end', iid=i, text=str(i + 1), values=row[1:])

        # Packing the table + back buttons
        self.habit_table.pack()
        self.back_to_analyze_menu_button.pack()
        self.button_back.pack()

    def show_habit_table_daily(self):
        # Removing all widgets
        self.remove_all_widgets()

        # Deleting all potentially existing rows from habit table
        self.habit_table.delete(*self.habit_table.get_children())

        # Adding data to the habit table
        for i, row in enumerate(controller.give_habit_list_daily()):
            self.habit_table.insert(parent='', index='end', iid=i, text=str(i + 1), values=row[1:])

        # Packing the table + back buttons
        self.habit_table.pack()
        self.back_to_analyze_menu_button.pack()
        self.button_back.pack()

    def show_habit_table_weekly(self):
        # Removing all widgets
        self.remove_all_widgets()

        # Deleting all potentially existing rows from habit table
        self.habit_table.delete(*self.habit_table.get_children())

        # Adding data to the habit table
        for i, row in enumerate(controller.give_habit_list_weekly()):
            self.habit_table.insert(parent='', index='end', iid=i, text=str(i + 1), values=row[1:])

        # Packing the table + back buttons
        self.habit_table.pack()
        self.back_to_analyze_menu_button.pack()
        self.button_back.pack()

    def show_habits_with_most_breaks(self):
        # Removing all widgets
        self.remove_all_widgets()

        # Deleting all potentially existing rows from habit table
        self.habit_table.delete(*self.habit_table.get_children())

        # Adding data to the habit table
        for i, row in enumerate(controller.give_habit_list_by_break_count()):
            self.habit_table.insert(parent='', index='end', iid=i, text=str(i + 1), values=row[1:])

        # Packing the table + back buttons
        self.habit_table.pack()
        self.back_to_analyze_menu_button.pack()
        self.button_back.pack()

    def show_habits_with_longest_current_streak(self):
        # Removing all widgets
        self.remove_all_widgets()

        # Deleting all potentially existing rows from habit table
        self.habit_table.delete(*self.habit_table.get_children())

        # Adding data to the habit table
        for i, row in enumerate(controller.give_habit_list_by_current_streak()):
            self.habit_table.insert(parent='', index='end', iid=i, text=str(i + 1), values=row[1:])

        # Packing the table + back buttons
        self.habit_table.pack()
        self.back_to_analyze_menu_button.pack()
        self.button_back.pack()

    def show_habits_with_longest_longest_streak(self):
        # Removing all widgets
        self.remove_all_widgets()

        # Deleting all potentially existing rows from habit table
        self.habit_table.delete(*self.habit_table.get_children())

        # Adding data to the habit table
        for i, row in enumerate(controller.give_habit_list_by_longest_streak()):
            self.habit_table.insert(parent='', index='end', iid=i, text=str(i + 1), values=row[1:])

        # Packing the table + back buttons
        self.habit_table.pack()
        self.back_to_analyze_menu_button.pack()
        self.button_back.pack()

    # General methods
    def back_click(self):
        # Remove widgets and setting label to start menu
        self.remove_all_widgets()
        self.label.configure(text="Start Menu", font=30)

        # Pack start menu widgets
        self.label.pack()
        self.button_create_habit.pack()
        self.button_delete_habit.pack()
        self.button_complete_habit.pack()
        self.button_analyze_habits.pack()
        self.button_exit.pack()

    def remove_all_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()

    def update_habit_list_dropdown(self):
        self.dropdown_habit_list.config(values=controller.get_habit_list())
