import tkinter as tk

window = tk.Tk()
window.title("Test Tkinter")
window.geometry("200x100")
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()
window.mainloop()

