from tkinter import *

window =Tk()
window.title("exam prepration")
window.minsize(width=300, height=300)
k = Label(text="this is alter")
k.pack()

def action():
    print(" this is button")
button=Button(text="click here!")
button.pack() 

entry =Entry()
entry.pack()

text =Text(height =5)
text.insert(END,"chhavi" )
text.pack()

spinbox =Spinbox(from_=-2, to=5,width =5 )
spinbox.pack()

scale = Scale(from_=0, to=100, orient="horizontal", width=20)
scale.pack()

checkbutton =Checkbutton(text ="click !!!!!!!")
checkbutton.pack()

radio =Radiobutton(text="1")
radio.pack()


list =Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for fruit in fruits :
    list.insert(END,fruit)

list.pack()
window.mainloop()