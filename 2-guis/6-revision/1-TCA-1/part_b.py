from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # resources
        self.default_image = PhotoImage(file="U:/com404/COM404/2-guis/6-revision/1-TCA-1/default.gif")
        self.filled_image = PhotoImage(file="U:/com404/COM404/2-guis/6-revision/1-TCA-1/correct.png")
        self.empty_image = PhotoImage(file="U:/com404/COM404/2-guis/6-revision/1-TCA-1/incorrect.png")
        
        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_email_image_label()
        self.__add_subscribe_type_label()
        self.__add_subscribe_dropdown()
        self.__add_subscribe_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", 
                                   padx=10, 
                                   pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER", 
                                     font="Arial 14",
                                     padx=10)

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(text="Please enter your email below to receiver our newsletter",
                                         padx=10,
                                         pady=10)

    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, sticky=E)
        self.email_label.configure(text="Email:",
                                   padx=10)

    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W, pady=10)
        self.email_entry.configure(bd=2,
                                   fg="#f00",
                                   width=30)
        # Email Check
        self.email_entry.bind("<KeyRelease>", self.__check_email)
    
    def __check_email(self, event):
        if (self.email_entry.get() == ""):
            self.email_image_label.configure(image=self.empty_image)
            messagebox.showerror("Newsletter", "Please enter your email.")
        else:
            self.email_image_label.configure(image=self.filled_image)
    
    def __add_email_image_label(self):
        self.email_image_label = Label(self.outer_frame)
        self.email_image_label.grid(row=2, column=1, sticky=E, padx=10)
        self.email_image_label.configure(image=self.default_image)

    def __add_subscribe_type_label(self):
        self.subscribe_type_label = Label(self.outer_frame)
        self.subscribe_type_label.grid(row=3, column=0, padx=10, sticky=E)
        self.subscribe_type_label.configure(text="Type")

    def __add_subscribe_dropdown(self):
        # Options and default
        self.subscribe_list = StringVar()
        choices = {'Weekly', 'Monthly', 'Yearly'}
        self.subscribe_list.set('Weekly')
        # Button itself
        self.subscribe_dropdown = OptionMenu(self.outer_frame, self.subscribe_list, *choices)
        self.subscribe_dropdown.grid(row=3, column=1, sticky=W, pady=10)
        self.subscribe_dropdown.configure(width=33)

    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=4, column=0, columnspan=3, pady=10, sticky=E+W)
        self.subscribe_button.configure(bg="#fee",
                                        text="Subscribe")
        # Events
        self.subscribe_button.bind("<ButtonRelease-1>", self.__clicked_subscribe_button)

    def __clicked_subscribe_button(self, event):
        selected_subscription = self.subscribe_list.get()
        if(self.email_entry.get() == ""):
            messagebox.showerror("Newsletter", "Please enter your email.")
        elif(selected_subscription == "Weekly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter!")
        elif(selected_subscription == "Monthly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the monthly newsletter!")
        elif(selected_subscription == "Yearly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the yearly newsletter!")

# This means that two files are not required
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()