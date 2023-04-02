import tkinter as tk
from tkinter import messagebox


class StartMenu(tk.Tk):
    def __init__(self):
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

    def on_button_create_click(self):
        self.destroy()
        create = CreateMenu()
        create.mainloop()

    def on_button_delete_click(self):
        pass

    def on_button_complete_click(self):
        pass

    def on_button_analyze_click(self):
        pass

    def on_button_exit_click(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

class CreateMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Habit Tracker")
        self.geometry("400x300")

        # Create label widget
        self.label = tk.Label(self, text="Creation Menu", font=30)

        # Create buttons
        self.button_daily = tk.Button(self, text="Create daily habit", command=self.daily_click)
        self.button_weekly = tk.Button(self, text="Create weekly habit", command=self.weekly_click)
        self.button_back = tk.Button(self, text="Back", command=self.back_click)

        # Pack widgets
        self.label.pack()
        self.button_daily.pack()
        self.button_weekly.pack()
        self.button_back.pack()


    def daily_click(self):
        pass

    def weekly_click(self):
        pass

    def back_click(self):
        self.destroy()
        start = StartMenu()
        start.mainloop()



if __name__ == "__main__":
    app = StartMenu()
    app.mainloop()
