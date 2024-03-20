import tkinter as tk
 
root = tk.Tk()
root.title("root")

heading = tk.Label(root, text="Heading")

textbox = tk.Text(root, height=3, width=18)


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

openWndBtn = tk.Button(command=exit)
openWndBtn.grid(row=0, column=0,)

root.mainloop()