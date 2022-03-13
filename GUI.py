main_screen=Tk()
main_screen.title('DATA ANALYTICS')
main_screen.geometry('5000x5000')

frame=Frame(main_screen)
frame.pack()


label= Label(frame,text="DASHBOARD FOR VARIOUS GENERAL LIFE PURPOSES",justify=LEFT,bg='blue',font='1100')
label.pack(side=LEFT)


sep =ttk.Separator(main_screen,orient='horizontal')
sep.pack(fill='x')


labelframe = LabelFrame(main_screen, text="DATA ANALYTICS DASHBOARD")
labelframe.pack(fill="both", expand="yes")




button1=Button(labelframe,text="LIFE EXPECTANCY DASHBOARD",font='1400',command=Life)
button1.pack()

button2=Button(labelframe,text="BILL AND TIP",font='1400',command=bt)
button2.pack()



main_screen.mainloop()
