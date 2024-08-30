import tkinter as tk

#create window
root = tk.Tk()
root.title("Rob")

label_1 = tk.Label(root,text ="Bye Felis" )
label_1.grid(column=0, row=0)

button_1 = tk.Button(root,text = "bob")
button_1.grid(column=1, row=0)

root.mainloop()