import tkinter
import random
from tkinter.font import ITALIC
import tkinter.messagebox



global user_point
user_point=0
global cpu_point
cpu_point=0
#................................press function...........................................
def press(player):
    possible_actions = ["سنگ","کاغذ","قیچی"]
    global user_point
    
    global cpu_point
    

    computer = random.choice(possible_actions)
    tkinter.messagebox.showinfo(message=f"\n تو {player} انتخاب کردی و کامپیوتر  {computer}  انتخاب کرد.\n")
    if player == computer :
        tkinter.messagebox.showinfo(message="مساوی شدی.")
    else:
        if player == "سنگ":
            if computer == "قیچی":
                tkinter.messagebox.showinfo(message="بردی")
                user_point=user_point+1
            else:
                tkinter.messagebox.showinfo(message="کامپیوتر برد")
                cpu_point+=1
        else:
            if player == "کاغذ":
                if computer ==  "قیچی":
                    tkinter.messagebox.showinfo(message="کامپیوتر برد")
                    cpu_point+=1

                else:
                    tkinter.messagebox.showinfo(message="بردی")
                    user_point+=1
            if player == "قیچی":
                if computer == "کاغذ":
                    tkinter.messagebox.showinfo(message="بردی")
                    user_point+=1
                else:
                    tkinter.messagebox.showinfo(message="کامپیوتر برد")
                    cpu_point+=1
    
    text_var.set(f""" 
     امتیاز بازیکن:{user_point}
     امتیاز کامپیوتر:{cpu_point}
     """)
#----------------------------end press function-------------------------------------------
def main():
    global user_point
    global cpu_point
    top = tkinter.Tk()
    top.title('سنگ کاغذ قیچی')
    top.geometry("320x600")
    sang_object = tkinter.PhotoImage(file='sang.gif')
    kaghaz_object = tkinter.PhotoImage(file='kaghaz.gif')
    gheychi_object = tkinter.PhotoImage(file='gheychi.gif')

    sang_btn = tkinter.Button(image=sang_object,command=lambda p="سنگ": press(p))
    sang_btn.pack()
    paper_btn = tkinter.Button(image=kaghaz_object,command=lambda p="کاغذ": press(p))
    paper_btn.pack()
    gheychi_btn = tkinter.Button(image=gheychi_object,command=lambda p="قیچی": press(p))
    gheychi_btn.pack()

    global text_var
    text_var=tkinter.StringVar()
    text_var.set(
     f""" 
     امتیاز بازیکن:{user_point}
     امتیاز کامپیوتر:{cpu_point}
    """      
    )
    point_label=tkinter.Label(textvariable=text_var,font=ITALIC)
    point_label.pack()
          
    top.mainloop()

main()