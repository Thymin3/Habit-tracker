import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")

        self.label = tk.Label(self, text="Hello, world!")
        self.label.pack(padx=20, pady=20)

        self.button = tk.Button(self, text="Click me!", command=self.on_button_click)
        self.button.pack(padx=20, pady=20)

    def on_button_click(self):
        self.label.config(text="Button clicked!")

if __name__ == '__main__':
    app = App()
    app.mainloop()