import GUI

def do_something():
    print("Doing something...")

if __name__ == '__main__':
    app = tkinter_file.App()

    # Link button click to a function in main script
    app.button.config(command=do_something)

    app.mainloop()
