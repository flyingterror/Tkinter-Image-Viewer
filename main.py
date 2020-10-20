from tkinter import *
from PIL import ImageTk,Image
 
root = Tk(className ='Photos')
//removed icon
 

myimage1 = ImageTk.PhotoImage(Image.open('image/1.jpg'))
myimage2 = ImageTk.PhotoImage(Image.open('image/2.jpg'))
myimage3 = ImageTk.PhotoImage(Image.open('image/3.jpg'))
myimage4 = ImageTk.PhotoImage(Image.open('image/4.jpg'))
myimage5 = ImageTk.PhotoImage(Image.open('image/5.jpeg'))

image_list = [myimage1, myimage2,myimage3,myimage4,myimage5]


my_label = Label(image =myimage1)
my_label.grid(row = 0, column = 0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image =image_list[image_num - 1])
    my_label.grid(row =0, column= 0, columnspan=3)
    button_forward= Button(root , text='>>', command = lambda:forward(image_num+1))
    
    if image_num == 5:
        button_forward = Button(root, text = ">>", state = DISABLED) 

    button_back = Button(root, text='<<',command= lambda:back(image_num-1)) 
    my_label.grid(row= 0, column = 0, columnspan= 3)
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row = 1, column= 0)

def back(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image =image_list[image_num - 1])
    my_label.grid(row =0, column= 0, columnspan=3)
    button_forward= Button(root , text='>>', command = lambda:forward(image_num+1))
    
  
    button_back = Button(root, text='<<',command= lambda:back(image_num-1)) 
    my_label.grid(row= 0, column = 0, columnspan= 3)
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row = 1, column= 0)
    
    
button_back = Button(root, text = '<<', command= back , state= DISABLED)
button_exit = Button(root, text = 'EXIT', command =root.quit)
button_forward = Button(root, text= '>>', command =lambda:forward(2))
 
button_forward.grid(row = 1, column = 2)
button_exit.grid(row = 1 ,column = 1)
button_back.grid(row = 1, column= 0)

root.mainloop()
