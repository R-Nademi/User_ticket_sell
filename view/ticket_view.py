from controller.ticket_controller import TicketController
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as msg

from model.entity.ticket import Ticket



class TicketView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Ticket View")
        self.window.geometry("1260x400")

       # تعریف متغیرهای فرم
        self.code = StringVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birth_date = StringVar()
        self.origin = StringVar()
        self.destination = StringVar()
        self.start_date_time = StringVar()
        self.end_date_time = StringVar()
        self.ticket_type = StringVar()
        self.seat_number = StringVar()
        self.price = IntVar()

        # ساخت لیبل‌ها و ورودی‌ها در سمت چپ با متد place
        Label(self.window, text="code:").place(x=20, y=40)
        Entry(self.window, textvariable=self.code).place(x=130, y=40)

        Label(self.window, text="name:").place(x=20, y=60)
        Entry(self.window, textvariable=self.name).place(x=130, y=60)

        Label(self.window, text="family:").place(x=20, y=80)
        Entry(self.window, textvariable=self.family).place(x=130, y=80)

        Label(self.window, text="birth_date:").place(x=20, y=100)
        Entry(self.window, textvariable=self.birth_date).place(x=130, y=100)

        Label(self.window, text="origin:").place(x=20, y=140)
        Entry(self.window, textvariable=self.origin).place(x=130, y=140)

        Label(self.window, text="destination:").place(x=20, y=180)
        Entry(self.window, textvariable=self.destination).place(x=130, y=180)

        Label(self.window, text="start_date_time:").place(x=20, y=220)
        Entry(self.window, textvariable=self.start_date_time).place(x=130, y=220)

        Label(self.window, text="end_date_time:").place(x=20, y=240)
        Entry(self.window, textvariable=self.end_date_time).place(x=130, y=240)

        Label(self.window, text="Ticket Type").place(x=20, y=20)
        Entry(self.window, textvariable=self.ticket_type).place(x=130, y=20)

        Label(self.window, text="seat_number:").place(x=20, y=160)
        Entry(self.window, textvariable=self.seat_number).place(x=130, y=160)

        Label(self.window, text="Price:").place(x=20, y=200)
        Entry(self.window, textvariable=self.price).place(x=130, y=200)

        # # search_by_name_family
        Label(self.window, text="Search by Name").place(x=300, y=20)
        self.search_name = StringVar()
        self.search_name_txt = Entry(self.window, textvariable=self.search_name, width=23, fg="gray64")
        self.search_name_txt.bind("<KeyRelease>", self.search_name_family)
        self.search_name_txt.place(x=420, y=20)

        Label(self.window, text="Search by Family").place(x=550, y=20)
        self.search_family = StringVar()
        self.search_family_txt = Entry(self.window, textvariable=self.search_family, width=23, fg="gray64")
        self.search_family_txt.bind("<KeyRelease>", self.search_name_family)
        self.search_family_txt.place(x=670, y=20)

        # جدول سمت راست برای نمایش بلیط‌ها
        self.table = ttk.Treeview(self.window, columns=("code", "name", "family", "birth_date", "origin",
                                               "destination", "start_date_time","end_date_time","ticket_type","seat_number","price"),
                                               show="headings")
                                  
        self.table.heading("code", text="code")
        self.table.heading("name", text="name")
        self.table.heading("family", text="family")
        self.table.heading("birth_date", text="birth_date")
        self.table.heading("origin", text="origin")
        self.table.heading("destination", text="destination")
        self.table.heading("start_date_time", text="start_date_time")
        self.table.heading("end_date_time", text="end_date_time")
        self.table.heading("ticket_type", text="ticket_type")
        self.table.heading("seat_number", text="seat_number")
        self.table.heading("price", text="Price")

        # تنظیم عرض ستون‌ها
        self.table.column("code", width=50)
        self.table.column("name", width=80)
        self.table.column("family", width=95)
        self.table.column("birth_date", width=80)
        self.table.column("origin", width=95)
        self.table.column("destination", width=95)
        self.table.column("start_date_time", width=95)
        self.table.column("end_date_time", width=95)
        self.table.column("ticket_type", width=80)
        self.table.column("seat_number", width=80)
        self.table.column("price", width=80)

        # جایگذاری جدول در سمت راست
        self.table.place(x=320, y=20, height=350)
        self.table.bind("<<TreeviewSelect>>")

        # دکمه‌ها پایین فرم
        Button(self.window, text="Save", width=34, command=self.save_click).place(x=20, y=280)
        Button(self.window, text="Edit", width=10, command=self.edit_click).place(x=20, y=320)
        Button(self.window, text="delete", width=10, command=self.delete_click).place(x=185, y=320)




        self.reset_form()

        self.window.mainloop()


    def save_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.save(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.family.get(),
            self.birth_date.get(),
            self.origin.get(),
            self.destination.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.ticket_type.get(),
            self.seat_number.get(),


        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.edit(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.origin.get(),
            self.destination.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.ticket_type.get(),
            self.seat_number.get(),
            self.price.get(),


        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        ticket_controller = TicketController()
        status, message = ticket_controller.delete(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.origin.get(),
            self.destination.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.ticket_type.get(),
            self.seat_number.get(),
            self.price.get(),

        )
        if status:
            msg.showinfo("delete", message)
            self.reset_form()
        else:
            msg.showerror("delete Error", message)

    def show_data_on_table(self, status, ticket_list):
        if status:
            for item in self.table.get_children():
                self.table.delete(item)

            for ticket in ticket_list:
                self.table.insert(
                    "",
                    END)


    def reset_form(self):
        self.code.set(0)
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")
        self.origin.set("")
        self.destination.set("")
        self.start_date_time.set("")
        self.end_date_time.set("")
        self.ticket_type.set("")
        self.seat_number.set("")
        self.price.set(0)

        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_all()
        self.show_data_on_table(status, ticket_list)

    def search_name_family(self, event):
        ticket_controller = TicketController()
        status, ticket_list = ticket_controller.find_name_family(self.search_name.get(), self.search_family.get())
        self.show_data_on_table(status, ticket_list)

    def select_ticket(self, event):
        ticket = Ticket(* self.table.item(self.table.focus())["values"]) # noqa
        self.code.set(ticket.code)
        self.name.set(ticket.name)
        self.family.set(ticket.family)
        self.birth_date.set(ticket.birth_date)
        self.origin.set(ticket.origin)
        self.destination.set(ticket.destination)
        self.start_date_time.set(ticket.start_date_time)
        self.end_date_time.set(ticket.end_date_time)
        self.ticket_type.set(ticket.ticket_type)
        self.seat_number.set(ticket.seat_number)
        self.price.set(ticket.price)

