   #importing all libraries and packages
from tkinter import *
from tkinter import messagebox 
from tkinter import Image
#import webbrowser
























#user-defined functions
def login():
        c=a.get()
        d=b.get()
        if d == "1234":
                top=Toplevel()
                top.title(a)
                top.geometry('1000x1000')
                act=Button(top,text="Cultural Activities")
                act.place(x=50,y=50)
                grades=Button(top,text="Grades")
                grades.place(x=100,y=100)
                marks=Button(top,text="Marks")
                marks.place(x=100,y=150)
                sub=Label(top,text="List of Optional Subjects Selected By Candiadate",fg="Red")
                sub.place(x=100,y=200)
                op_sub=Listbox(top)
                op_sub.insert(1,"Astrophysics")
                op_sub.insert(2,"Quantum Physics")
                op_sub.insert(3,"Operations Research")
                op_sub.insert(4,"Cybersecurity Management")
                op_sub.place(x=100,y=250)
                def callback(url):
                    webbrowser.open_new(url)
                
                link1=Label(top,text="Linkedin",fg="blue",cursor="hand2")
                link1.place(x=100,y=400)
                link1.bind("<Button-1>",lambda e:callback("https://www.linkedin.com/in/akunuri-a-267841198/"))
                
                link2=Label(top,text="Personal Website",fg='green',cursor="hand2")
                link2.place(x=100,y=450)
                link2.bind("<Button-2>",lambda e:callback("https://sites.google.com/view/akunuri-arun-deepak"))
                
                
                def sel():
                    select=str(var.get())
                    new_window=Tk()
                    new_window.title(select+"Payment")
                    new_window.geometry('500x500')
                    
                    a=Label(new_window,text="Enter Your Card Number/Account Number:")
                    a.place(x=50,y=250)
                    
                    
    
                    a=Entry(new_window,width=35)
                    a.place(x=200,y=250)


                    b1=Label(new_window,text="Enter the Amount")
                    b1.place(x=50,y=300)
                    b=Entry(new_window,width=35)
                    b.place(x=200,y=300)

                    




                
                
                var = IntVar()
                sep1 =ttk.Separator(top,orient='horizontal')
                sep1.pack(fill='x')
                
                R1 = Radiobutton(top, text="Cash", variable=var, value=1,command=sel)
                R1.pack()
                
                R2 = Radiobutton(top, text="Credit\Debit", variable=var, value=2,command=sel)
                R2.pack()

                R3 = Radiobutton(top, text="Net Banking", variable=var, value=3,command=sel)
                R3.pack()
                

                
                
                
                
                
                
                
                
                
                
                
        else :
                messagebox.showerror("Error","Wrong Password")
                
def register():
                l1=l.get()
                new=Toplevel()
                new.title(l1)
                messagebox.showinfo("Welcome😊😊😊", "You have been successfully registered🎉🎉")

#main screen
a=Tk()
a.title('Login Page')
a.geometry('500x500')


lab1=Label(text='CMR Global University',fg='red',font="Roman")
lab1.place(x=100,y=100)

lab2=Label(text='Student Portal',fg='black',font='Italic')
lab2.place(x=100,y=150)


#sign in for already registered students 
lab3=Label(text="Sign In",fg='black',font='Roman')
lab3.place(x=100,y=200)


a1=Label(text="Enter Your Username:")
a1.place(x=50,y=250)

a=Entry(width=35)
a.place(x=200,y=250)


b1=Label(text="Enter Your Password")
b1.place(x=50,y=300)
b=Entry(width=35)
b.place(x=200,y=300)



but1=Button(text="Login",fg='blue',command=login)
but1.place(x=100,y=350)




lab3=Label(text="***************************************************************************************************************************************")
lab3.place(x=100,y=400)


reg=Label(text="REGISTER HERE!!!!!")
reg.place(x=100,y=450)


lab4=Label(text="Enter Your Name:")
lab4.place(x=50,y=550)
l=Entry(width=35)
l.place(x=200,y=550)



lab5=Label(text="Enter Your Mobile Number:")
lab5.place(x=50,y=600)
m=Entry(width=35)
m.place(x=200,y=600)


lab6=Label(text="Choose Your Password")
lab6.place(x=50,y=650)
n=Entry(width=35)
n.place(x=200,y=650)


but2=Button(text="Register",fg='blue',command=register)
but2.place(x=200,y=700)

a.mainloop()