from tkinter import ttk, Tk, PhotoImage

root = Tk() 

frame_header = ttk.Frame(root)
frame_header.pack()

ttk.Label(frame_header, text="This is a Label inside Frame").pack() 


root.mainloop()