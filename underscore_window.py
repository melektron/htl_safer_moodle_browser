import tkinter as tk
import tkinter.ttk as ttk
import random 
from tkinter import messagebox



def unknown_button(): 
    random_button_nr=random.randint(1,10)
    if random_button_nr == 7: 
        #öffnet Matteos Programm 
        messagebox.showinfo("!","Matteo")
    else: 
        messagebox.showinfo("!","Try again!!!")



def brain_test_color(): 
    messagebox.showinfo("!","WRONG!!!")


def weak_password(): 
    print(f)


#create window
window = tk.Tk()
window.title(':)')
window.geometry('1000x500')

label_heading_brain_test=tk.Label(window, text="How good is your brain?")
label_heading_brain_test.grid(row=0,column=0)

#Color test
label_color_question=tk.Label(window, text="What is 'Blue'?")
label_color_question.grid(row=2,column=0)

selected=tk.IntVar()
radiobutton_color_question_1=tk.Radiobutton(window,text='Red', value='1',command=brain_test_color, variable=selected)
radiobutton_color_question_2=tk.Radiobutton(window,text='Green', value='2', command=brain_test_color, variable=selected)
radiobutton_color_question_2.configure(background="blue")
radiobutton_color_question_3=tk.Radiobutton(window,text='Blue', value='3', command=brain_test_color, variable=selected)
radiobutton_color_question_1.grid(row=3,column=0)
radiobutton_color_question_2.grid(row=3,column=1)
radiobutton_color_question_3.grid(row=3,column=2)

#Password 
label_color_question=tk.Label(window, text="Choose a secure password:")
label_color_question.grid(row=4,column=0)
combobox_password = ttk.Combobox(window, command=weak_password)
combobox_password['values']= ("", "123456789", "gboquwbg48670OUHhughu#gq#", "abcdef", "Matteo")
combobox_password.current(0)
combobox_password.grid(row=5,column=1)



#Unknown button 
label_color_question=tk.Label(window, text="Choose a button:")
label_color_question.grid(row=6,column=0)
unknown_button_1=tk.Button(window,text="Click ME",command=unknown_button)
unknown_button_2=tk.Button(window,text="Click ME",command=unknown_button)
unknown_button_3=tk.Button(window,text="Click ME",command=unknown_button)
unknown_button_4=tk.Button(window,text="Click ME",command=unknown_button)
unknown_button_5=tk.Button(window,text="Click ME",command=unknown_button)
unknown_button_1.grid(row=7,column=0)
unknown_button_2.grid(row=7,column=1)
unknown_button_3.grid(row=7,column=2)
unknown_button_4.grid(row=7,column=3)
unknown_button_5.grid(row=7,column=4)





#launch gui
window.mainloop()