from tkinter import *
from tkinter import PhotoImage
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Dark Mode Calculator")
        self.btnState = False
        master.e = Entry(master, font="none 10", width=35, borderwidth=5)
        master.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        master.my_menu = Menu(master)
        master.config(menu=master.my_menu)


        master.file_menu = Menu(master.my_menu)
        master.my_menu.add_cascade(label="DarkMode", menu=master.file_menu)
        master.file_menu.add_command(label="On", command=self.on)
        master.file_menu.add_command(label="Off", command=self.off)



        #master.file_menu.add_command(label="Exit", command=self.our_command)




        self.button_1 = Button(master, text="1", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(1))
        self.button_2 = Button(master, text="2", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(2))
        self.button_3 = Button(master, text="3", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(3))
        self.button_4 = Button(master, text="4", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(4))
        self.button_5 = Button(master, text="5", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(5))
        self.button_6 = Button(master, text="6", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(6))
        self.button_7 = Button(master, text="7", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(7))
        self.button_8 = Button(master, text="8", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(8))
        self.button_9 = Button(master, text="9", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(9))
        self.button_0 = Button(master, text="0", font="none 14", padx=40, pady=20, command=lambda: self.button_calc(0))
        self.button_add = Button(master, text="+", font="none 14", padx=40, pady=20, command=self.button_add)
        self.button_equal = Button(master, text="=", font="none 14", padx=93, pady=20, command=self.button_equal)
        self.button_clear = Button(master, text="C", font="none 14", padx=38, pady=20, command=self.button_clear)
        self.button_subtract = Button(master, text="-", font="none 14", padx=43, pady=20, command=self.button_subtract)
        self.button_multiply = Button(master, text="x", font="none 14", padx=42, pady=20, command=self.button_multiply)
        self.button_divide = Button(master, text="/", font="none 14", padx=42, pady=20, command=self.button_divide)
        self.button_percentage = Button(master, text="%", font="none 14", padx=37, pady=20, command=self.button_percentage)
        #self.Button_DarkMode = Button(master, text="DarkMode: ON", font="none 14", padx=40, pady=20, command=self.switch, bg="#CECCBE", activebackground="#CECCBE")
        
        self.button_1.grid(row=3,column=0)
        self.button_2.grid(row=3,column=1)
        self.button_3.grid(row=3,column=2)

        self.button_4.grid(row=2,column=0)
        self.button_5.grid(row=2,column=1)
        self.button_6.grid(row=2,column=2)

        self.button_7.grid(row=1,column=0)
        self.button_8.grid(row=1,column=1)
        self.button_9.grid(row=1,column=2)

        self.button_0.grid(row=4,column=0)

        self.button_clear.grid(row=4, column=2, columnspan=2)
        self.button_add.grid(row=5, column=0)
        self.button_equal.grid(row=5, column=1, columnspan=2)

        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)
        self.button_percentage.grid(row=4, column=1)

        #self.Button_DarkMode.grid(row=7, column=0, columnspan=3)

    def button_calc(self, number):
        self.number = number      
        self.current = self.master.e.get()
        self.master.e.delete(0, END)
        self.master.e.insert(0, str(self.current) + str(self.number))
    def button_clear(self):
        self.master.e.delete(0, END)
    def button_add(self):
        self.first_number = self.master.e.get()
        global f_num
        global math
        self.math = "addition"
        self.f_num = int(self.first_number)
        self.master.e.delete(0, END)

    def button_subtract(self):
        self.first_number = self.master.e.get()
        global f_num
        global math
        self.math = "subtraction"
        self.f_num = int(self.first_number)
        self.master.e.delete(0, END)
    def button_multiply(self):
        self.first_number = self.master.e.get()
        global f_num
        global math
        self.math = "multiplication"
        self.f_num = int(self.first_number)
        self.master.e.delete(0, END)
    def button_divide(self):
        self.first_number = self.master.e.get()
        global f_num
        global math
        self.math = "division"
        self.f_num = int(self.first_number)
        self.master.e.delete(0, END)
    def button_percentage(self):
        self.first_number = self.master.e.get()
        global f_num
        global math
        self.math = "percentage"
        self.f_num = int(self.first_number)
        self.master.e.delete(0, END)
    def button_equal(self):
        self.second_number = self.master.e.get()
        self.master.e.delete(0, END)
        if self.math == "addition":
            self.master.e.insert(0 , self.f_num + int(self.second_number))
        if self.math == "subtraction":
            self.master.e.insert(0 , self.f_num - int(self.second_number))
        if self.math == "multiplication":
            self.master.e.insert(0 , self.f_num * int(self.second_number))
        if self.math == "division":
            self.master.e.insert(0 , self.f_num / int(self.second_number))
        if self.math == "percentage":
            self.master.e.insert(0, self.f_num / int(100))
    def on(self):
        self.master.config(bg="#2B2B2B")
        self.button_1.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_1.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_2.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_3.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_4.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_5.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_6.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_7.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_8.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_9.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_0.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_add.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_equal.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_clear.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_subtract.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_multiply.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_divide.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.button_percentage.config(bg="#2B2B2B", fg="#CECCBE", font="none 14")
        self.master.e.config(bg="#2B2B2B", fg="#CECCBE", font="none 10")
    def off(self):
        self.master.config(bg="#CECCBE")
        self.button_1.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_2.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_3.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_4.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_5.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_6.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_7.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_8.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_9.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_0.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_add.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_equal.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_clear.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_subtract.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_multiply.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_divide.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.button_percentage.config(bg="#CECCBE", fg="#2B2B2B", font="none 14")
        self.master.e.config(bg="#CECCBE", fg="#2B2B2B", font="none 10")

root = Tk()
mygui = Calculator(root)
root.mainloop()