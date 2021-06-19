from tkinter import ttk, Tk, PhotoImage, Canvas, filedialog

root = Tk() 

filename = filedialog.askopenfilename() #this will open the file. similarly we have asksave which will save the file
print(filename)


root.mainloop()