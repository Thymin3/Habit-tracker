import GUI


def do_something():
    print("Doing something...")


if __name__ == '__main__':
    app = GUI.Menu()

    # Link button click to a function in main script
    #app.button_create_habit.config(command=do_something)
    app.mainloop()
