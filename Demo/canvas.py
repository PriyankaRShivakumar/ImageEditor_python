from tkinter import ttk, Tk, PhotoImage, Canvas

root = Tk() 

ttk.Label(root, text="This is a Label").pack() 

canvas = Canvas(root, bg="grey", width=300, height=400)
canvas.pack()

logo = PhotoImage(file="python_logo.gif")

canvas.create_image(300/2,400/2,image=logo) #width/2, height/2, image


root.mainloop()