# Fetch API Tkinter.
# James Webb Telescope (JWT).
# Yara ElSakka.
# 03.01.22
# code done at the class time.

from tkinter import *
from requests import *

programWindow = Tk()
programWindow.title("Tracking JWT App, By Yara")
programWindow.geometry("600x500")
programWindow.resizable(0, 0)
programWindow.configure(bg="#DB6B97")

hourInput = Entry()
hourInput.pack(pady=20)

minuteInput = Entry()
minuteInput.pack(pady=20)

secondInput = Entry()
secondInput.pack(pady=20)

BeginCountdown = Button(text="Let's Begin!!")
BeginCountdown.pack(pady=20)

mainloop()

# end of code.
# 03.01.22