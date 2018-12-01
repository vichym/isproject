import tkinter as tk


class Window1:
    def __init__(self):
        self.mainWin = tk.Tk()
        label1 = tk.Label(self.mainWin, text="+", font="Arial 32 bold",height = 5, width = 10, borderwidth = 50)
        label1.grid(row=0, column=0)

        label2 = tk.Label(self.mainWin, text = "+", font="Arial 18 bold", image = tk.Image.open(source o.))
        label2.grid(row=1, column=0)
        #
        # label1 = tk.Label(self.mainWin, text="Type a phrase to be reversed", font="Arial 18 bold")
        # label1.grid(row=0, column=0)
        #
        # label1 = tk.Label(self.mainWin, text="Type a phrase to be reversed", font="Arial 18 bold")
        # label1.grid(row=0, column=0)
        #
        # label1 = tk.Label(self.mainWin, text="Type a phrase to be reversed", font="Arial 18 bold")
        # label1.grid(row=0, column=0)
        #
        # label1 = tk.Label(self.mainWin, text="Type a phrase to be reversed", font="Arial 18 bold")
        # label1.grid(row=0, column=0)
    def run(self):
        self.mainWin.mainloop()


myGui = Window1()
myGui.run()