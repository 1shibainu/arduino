import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.label = tk.Label(self, text="pick a number from 1 to 10:")
        self.label.pack()
        vcmd = (self.register(self.validate), '%P')
        self.entrythingy = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.show_loading_bar)

    def validate(self, new_text):
        if not new_text:
            return True
        try:
            if 1 <= int(new_text) <= 10:
                return True
            else:
                return False
        except ValueError:
            return False

    def show_loading_bar(self, event):
        if self.validate(self.contents.get()):
            loading_window = tk.Toplevel(self)
            loading_window.title("reading mind...")
            progress = ttk.Progressbar(loading_window, orient="horizontal", length=300, mode="indeterminate")
            progress.pack(padx=20, pady=20)
            progress.start()
            self.after(4500, lambda: self.on_loading_complete(loading_window, progress))
        else:
            messagebox.showwarning("Invalid Input", "Please enter a number from 1 to 10.")

    def on_loading_complete(self, loading_window, progress):
        progress.stop()
        loading_window.destroy()
        messagebox.showinfo("mind reading complete", "mind reading is complete.\nnumber im thinking of is: {}".format(self.contents.get()))

root = tk.Tk()
root.geometry("250x100")
myapp = App(root)
root.title("mind reader")
myapp.mainloop()