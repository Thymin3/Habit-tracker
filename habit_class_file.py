class Habit:
    # basic functionality
    def __init__(self, habit_name, periodicity):
        self.habit_name = habit_name
        self.periodicity = periodicity
        self.highest_streak = 0
        self.current_streak = 0

    def mark_complete(self):
        self.current_streak += 1

    def break_streak(self):
        if self.highest_streak < self.current_streak:
            self.highest_streak = self.current_streak
        self.current_streak = 0

    # analytics module
    def show_habit_name(self):
        print(f"Habit: {self.habit_name}")
    
    def show_current_streak(self):
        print(f"Current streak: {self.current_streak}")

    def show_highest_streak(self):
        if self.highest_streak < self.current_streak:
            print(f"Highest streak: {self.current_streak}. This is your current streak. Keep going!")
        print(f"Highest streak: {self.highest_streak}")
