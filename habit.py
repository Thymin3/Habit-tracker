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
