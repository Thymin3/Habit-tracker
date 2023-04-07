import GUI

habit_list = ("a", "b", "c", "d")

def create_habit():
    print("Doing something...")


if __name__ == '__main__':
    app = GUI.Menu()

    # Link button click to a function in main script
    #app.button_create_habit.config(command=do_something)
    app.mainloop()
