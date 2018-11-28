import tkinter as tk

window = tk.Tk()
window.title("Image Signature Prorame")

#Button
button = tk.Button(name= 'click me')
button.grid(row=1,column=0)

label= tk.Label("Welcome to ISP").grid(row=0,column=0)

window.mainLoop()
