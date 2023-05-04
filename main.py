import sqlite3 as sql
import controller


class Habit:
    def __init__(self, name, periodicity, days_since_last_completion=0, current_streak=0,
                 longest_streak=0, number_of_breaks=0):
        self.name = name
        self.periodicity = periodicity
        self.days_since_last_completion = days_since_last_completion
        self.current_streak = current_streak
        self.longest_streak = longest_streak
        self.number_of_breaks = number_of_breaks

    @classmethod    # Used to avoid that controller is calling the class itself without an instance having been created
    def create_habit(cls, name, periodicity):
        habit = cls(name, periodicity)  # Creating a new habit instance
        return habit.name, habit.periodicity

    # def complete_habit(self):
    #     self.days_since_last_completion = 0
    #     self.update_current_streak()
    #     self.update_longest_streak()
    #
    #     return self.days_since_last_completion, self.current_streak, self.longest_streak, self.name

    # def update_current_streak(self):
    #     self.current_streak = self.current_streak + 1
    #
    # def update_longest_streak(self):
    #     if self.longest_streak < self.current_streak:
    #         self.longest_streak = self.current_streak
    #     else:
    #         pass
    #
    # def break_streak(self):
    #     if self.periodicity == "weekly":
    #         if self.days_since_last_completion > 7:
    #             self.current_streak = 0
    #     elif self.days_since_last_completion > 1:
    #         self.current_streak = 0
    #     else:
    #         pass


if __name__ == '__main__':
    controller.run_GUI()
