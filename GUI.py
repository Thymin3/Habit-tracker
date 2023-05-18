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

    ### Main menu methods
    def create_click(self):
        """
        This method is triggered when the create button is clicked in the GUI.
        It removes all existing widgets, sets the label to "Creation Menu", and packs the necessary widgets for the
        Creation menu.
        It is part of the main menu methods.
        """
        # Remove widgets and set label to creation menu
        self.remove_all_widgets()
        self.label.configure(text="Creation Menu")

        # Pack widgets
        self.label.pack()
        self.button_daily.pack()
        self.button_weekly.pack()
        self.button_back.pack()

    def delete_click(self):
        """
        This method is triggered when the delete button is clicked in the GUI.
        It removes all existing widgets, sets the label to "Which habit would you like to delete?",
        and packs the necessary widgets for the Deletion menu.
        It is part of the main menu methods.
        """
        # Remove widgets and adjust label
        self.remove_all_widgets()
        self.label.configure(text="Which habit would you like to delete?")

        # Pack widgets
        self.label.pack()
        self.dropdown_habit_list.pack()
        self.delete_button.pack()
        self.button_back.pack()

    def complete_click(self):
        """
        This method is triggered when the complete button is clicked in the GUI.
        It removes all existing widgets, sets the label to "Which habit did you complete today?",
        and packs the necessary widgets for the Completion menu.
        It is part of the main menu methods.
        """
        # Remove widgets and adjust label
        self.remove_all_widgets()
        self.label.configure(text="Which habit did you complete today?")

        # Pack widgets
        self.label.pack()
        self.dropdown_habit_list.pack()
        self.complete_button.pack()
        self.button_back.pack()

    def analyze_click(self):
        """
        This method is triggered when the analyze button is clicked in the GUI.
        It removes all existing widgets, sets the label to "Data analysis Menu",
        and packs the necessary widgets for the Data analysis menu.
        It is part of the main menu methods.
        """
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
        """
        This method is triggered when the exit button is clicked in the GUI.
        It displays a message box asking the user if they want to quit.
        If the user confirms the request, the application is destroyed and closed.

        Note:
        - This method is the only one relying on the "messagebox" module from tkinter.
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    ### Creation menu methods
    def daily_click(self):
        """
        This method is triggered when the daily button is clicked in the Creation menu.
        It removes the creation menu buttons, adjusts the label to prompt for a new daily habit name,
        and packs the necessary widgets for inputting the habit name and creating the daily habit.
        """
        # Remove creation menu buttons and adjusting label
        self.remove_all_widgets()
        self.label.configure(text="Please type in the name of your new daily habit:")

        # Pack widget
        self.label.pack()
        self.input_field_daily.pack()
        self.create_habit_daily.pack()
        self.button_back.pack()

    def weekly_click(self):
        """
        This method is triggered when the weekly button is clicked in the Creation menu.
        It removes the creation menu buttons, adjusts the label to prompt for a new daily habit name,
        and packs the necessary widgets for inputting the habit name and creating the daily habit.
        """
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
        """
        Gets user input for the daily habit name and passes it to the controller.

        This method retrieves the user input from the input field for the daily habit name.
        It then calls the "create_daily_habit" function from the controller module,
        passing the new habit name as an argument.
        If the habit name already exists in the database, it updates the label to display an error message.
        Otherwise, it removes the input field and create habit button, and updates the label to indicate
        that the daily habit has been successfully created.

        Additionally, this method updates the habit dropdown menu by creating a new ttk.Combobox widget
        with the updated habit list from the controller module.
        """
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
        """
        Gets user input for the weekly habit name and passes it to the controller.

        This method retrieves the user input from the input field for the weekly habit name.
        It then calls the "create_daily_habit" function from the controller module,
        passing the new habit name as an argument.
        If the habit name already exists in the database, it updates the label to display an error message.
        Otherwise, it removes the input field and create habit button, and updates the label to indicate
        that the daily habit has been successfully created.

        Additionally, this method updates the habit dropdown menu by creating a new ttk.Combobox widget
        with the updated habit list from the controller module.
        """
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

    ### Deletion menu methods
    def delete_habit(self):
        """
        This method retrieves the selected habit to delete from the habit dropdown menu.
        It then removes existing widgets, updates the label to indicate the habit has been deleted,
        and repacks the label and back button.

        Additionally, this method calls the "delete_habit" function in the controller module,
        passing the habit name to be deleted as an argument.

        Lastly, it updates the habit dropdown menu by creating a new "ttk.Combobox" widget
        with the updated habit list from the controller module.
        """
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

    ### Completion menu methods
    def complete_habit(self):
        """
        This method retrieves the selected habit to mark as completed from the habit dropdown menu.
        It then removes existing widgets, updates the label to indicate the habit has been completed,
        and repacks the label and back button.

        Additionally, this method calls the "complete_habit" function in the controller module,
        passing the habit name to be marked as completed as an argument.

        If the completion is successful, nothing further is done.
        If the completion cannot be recorded due to multiple completions in one day for the habit,
        it triggers the `several_completions_one_day` method to handle the situation.
        Whether the completion is successful is determined in the complete_habit function in the controller module.
        """
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
        """
        This method updates the label to display a message indicating that the habit has already been completed
        within the last 24 hours and advises the user to wait until the next day to complete it again.
        """
        self.label.configure(text="Habit already completed today. \nPlease wait until tomorrow to complete it again.")
        self.label.pack()

    ### Data analysis menu methods
    def show_habit_table(self):
        """
        Displays a habit table in the data analysis menu.

        This method removes all existing widgets, deletes any potential rows from the habit table,
        retrieves habit data from the controller module, and populates the habit table accordingly.

        The habit table is populated by iterating over the retrieved habit data and inserting each row
        into the table with the corresponding values.

        After populating the habit table, the method packs the habit table widget along with the back buttons.
        """
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
        """
        Displays a habit table of habits with periodicity "daily" in the data analysis menu.

        This method removes all existing widgets, deletes any potential rows from the habit table,
        retrieves habit data from the controller module, and populates the habit table accordingly.

        The habit table is populated by iterating over the retrieved habit data and inserting each row
        into the table with the corresponding values.

        After populating the habit table, the method packs the habit table widget along with the back buttons.
        """
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
        """
        Displays a habit table of habits with periodicity "weekly" in the data analysis menu.

        This method removes all existing widgets, deletes any potential rows from the habit table,
        retrieves habit data from the controller module, and populates the habit table accordingly.

        The habit table is populated by iterating over the retrieved habit data and inserting each row
        into the table with the corresponding values.

        After populating the habit table, the method packs the habit table widget along with the back buttons.
        """
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
        """
        Displays a habit table of all habits, sorted by break count in the data analysis menu in descending order.

        This method removes all existing widgets, deletes any potential rows from the habit table,
        retrieves habit data from the controller module, and populates the habit table accordingly.

        The habit table is populated by iterating over the retrieved habit data and inserting each row
        into the table with the corresponding values.

        After populating the habit table, the method packs the habit table widget along with the back buttons.
        """
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
        """
        Displays a habit table of all habits, sorted by current streak count in the data analysis menu in
        descending order.

        This method removes all existing widgets, deletes any potential rows from the habit table,
        retrieves habit data from the controller module, and populates the habit table accordingly.

        The habit table is populated by iterating over the retrieved habit data and inserting each row
        into the table with the corresponding values.

        After populating the habit table, the method packs the habit table widget along with the back buttons.
        """
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
        """
        Displays a habit table of all habits, sorted by the longest overall streak count in the data analysis menu in
        descending order.

        This method removes all existing widgets, deletes any potential rows from the habit table,
        retrieves habit data from the controller module, and populates the habit table accordingly.

        The habit table is populated by iterating over the retrieved habit data and inserting each row
        into the table with the corresponding values.

        After populating the habit table, the method packs the habit table widget along with the back buttons.
        """
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

    ### General methods
    def back_click(self):
        """
        Performs actions to navigate back to the start menu.

        This method removes all existing widgets, updates the label to "Start Menu" with a specified font,
        and repacks the start menu widgets.
        """
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
        """
        This method unpacks all existing widgets currently displayed.
        """
        for widget in self.winfo_children():
            widget.pack_forget()

    def update_habit_list_dropdown(self):
        """
        This method updates the dropdown habit list by requesting the list of currently existing habits stored in
        the database. It therefore accesses the function "get_habit_list" in the controller module.
        """
        self.dropdown_habit_list.config(values=controller.get_habit_list())
