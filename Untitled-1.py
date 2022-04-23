
from tkinter import *
window = Tk()
window.title("toi la khanh")
def dung_an_vao_day():
    dung_an_vao_day = Button(window,text="oh noooo...")
    dung_an_vao_day.pack()
mybutton = Button(window, text="đừng ấn vào đây", command=dung_an_vao_day)
mybutton.pack()
window.mainloop()