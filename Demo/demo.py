from tkinter import ttk, Tk, PhotoImage

root = Tk() #instanciate a window from class Tk

ttk.Label(root, text="This is a Label").pack() #use Label from ttk class, pass the window and the text to be displayed.It returns an Object. pack will stack the label on the window.

my_label_obj = ttk.Label(root, text="This is a second Label")
my_label_obj.pack()

print("This will be displayed on the console when the app runs")

def triggered_func():
    print("I was clicked")

ttk.Button(root, text="Click Me!", command = triggered_func).pack() #triggered_func is an userdefined function, it should be defined before calling it here.

logo = PhotoImage(file="python_logo.gif").subsample(5,5) #pass the image to PhotoImage function, it returns an image obj. subsample is used to set the size of the image
ttk.Label(root, image=logo).pack() #pass the image obj in label

root.mainloop() #open the window