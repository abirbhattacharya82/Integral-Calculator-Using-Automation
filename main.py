#The Intrgral Calculator with the help of Integral Calculator
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By

def integrate():
    s=e1.get()
    d=webdriver.Chrome("D:/Python/Automation/files/driver_1.exe")
    d.get("https://www.integral-calculator.com/")
    
    d.find_element(By.ID,'expression').send_keys(s)
    
    button=d.find_element(By.ID,'go')
    button.click()

window=Tk()
window.title("Integration Calculator")
window.resizable(0,0)

l1=Label(window,text="Enter the value")
l1.grid(row=0,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

l2=Label(window,text="Use '^' for Square")
l2.grid(row=1,column=0,columnspan=2)

b1=Button(window,text="Integrate",width=40,command=integrate)
b1.grid(row=2,column=0,columnspan=2)

window.mainloop()

