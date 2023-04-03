import tkinter as tk
from tkinter import messagebox


class Menu(tk.Tk):
    def __init__(self):  # Setting up main menu
        super().__init__()
        self.title("Habit Tracker")
        self.geometry("400x300")

        # Create label widget
        self.label = tk.Label(self, text="Start menu", font=30)

        # Create buttons
        self.button_create_habit = tk.Button(self, text="Create habit", command=self.on_button_create_click)
        self.button_delete_habit = tk.Button(self, text="Delete habit", command=self.on_button_delete_click)
        self.button_complete_habit = tk.Button(self, text="Complete habit", command=self.on_button_complete_click)
        self.button_analyze_habits = tk.Button(self, text="Analyze habits", command=self.on_button_analyze_click)
        self.button_exit = tk.Button(self, text="Exit", command=self.on_button_exit_click)

        # Pack widgets
        self.label.pack()
        self.button_create_habit.pack()
        self.button_delete_habit.pack()
        self.button_complete_habit.pack()
        self.button_analyze_habits.pack()
        self.button_exit.pack()

    def on_button_create_click(self):  # Setting up creation menu

        def daily_click():

            # Remove creation menu buttons and adjusting label
            self.label.configure(text="Please type in the name of your new daily habit:")
            self.button_daily.pack_forget()
            self.button_weekly.pack_forget()
            self.button_back.pack_forget()

            # Create Entry widget
            input_field = tk.Entry(self)

            # Pack widget
            input_field.pack()

        def weekly_click():
            pass

        def back_click():

            # Remove creation menu buttons and setting label to start menu
            self.label.configure(text="Start Menu", font=30)
            self.button_daily.pack_forget()
            self.button_weekly.pack_forget()
            self.button_back.pack_forget()

            # Pack start menu widgets
            self.label.pack()
            self.button_create_habit.pack()
            self.button_delete_habit.pack()
            self.button_complete_habit.pack()
            self.button_analyze_habits.pack()
            self.button_exit.pack()

        # Remove start menu buttons and setting label to creation menu

        self.label.configure(text="Create Menu", font=30)
        self.button_create_habit.pack_forget()
        self.button_delete_habit.pack_forget()
        self.button_complete_habit.pack_forget()
        self.button_analyze_habits.pack_forget()
        self.button_exit.pack_forget()

        # Create creation menu buttons
        self.button_daily = tk.Button(self, text="Create daily habit", command=daily_click)
        self.button_weekly = tk.Button(self, text="Create weekly habit", command=weekly_click)
        self.button_back = tk.Button(self, text="Back", command=back_click)

        # Pack widgets
        self.label.pack()
        self.button_daily.pack()
        self.button_weekly.pack()
        self.button_back.pack()

    def on_button_delete_click(self):
        pass

    def on_button_complete_click(self):
        pass

    def on_button_analyze_click(self):
        pass

    def on_button_exit_click(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    app = Menu()
    app.mainloop()
