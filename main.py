import sqlite3 as sql
import controller


class Habit:
    def __init__(self, name, periodicity, current_streak=0, longest_streak=0, number_of_brakes=0):
        self.name = name
        self.periodicity = periodicity
        self.current_streak = current_streak
        self.longest_streak = longest_streak
        self.number_of_brakes = number_of_brakes

    @classmethod    # Used to avoid that controller is calling the class itself without an instance having been created
    def create_habit(cls, name, periodicity):
        habit = cls(name, periodicity)  # Creating a new habit instance
        return habit.name, habit.periodicity

    def delete_habit(self, name):
        pass

    def complete_task(self):
        pass

    def update_current_streak(self):
        pass

    def update_longest_streak(self):
        pass

    def break_streak(self):
        pass

    def check_for_breaks(self):
        pass

if __name__ == '__main__':
    controller.run_GUI()
