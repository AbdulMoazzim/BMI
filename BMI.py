from tkinter import Tk, Label, Button, Entry
def func():
    bmi = round((float(e2.get()))*703/((float(e1.get()))**2),2)
    if bmi < 18.5:
        msg= "Your bmi is {} (Underweight)".format(bmi)
    elif 18.5 <= bmi < 25:
        msg= "Your bmi is {} (Normal)".format(bmi)
    else:
        msg= "Your bmi is {} (Overweight)".format(bmi)
    l3 = Label(r, text=msg)
    l3.grid()


r = Tk()
r.title('BMI App')
r.geometry("300x200+50+0")
l1 = Label(r, text = 'Enter your height(inches):')
l1.grid(row=0,column=0)
e1 = Entry(r)
e1.grid(row=0,column=1)
l2 = Label(r, text = 'Enter your weight(pounds):')
l2.grid(row=1,column=0)
e2 = Entry(r)
e2.grid(row=1,column=1)
b = Button(r, text='Find BMI', command=func)
b.grid()
r.mainloop()