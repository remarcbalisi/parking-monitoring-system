from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow

class Paypros_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("827x340+180+263")
        self.root.resizable(0, 0)

##___________________________TRANSACTION REGISTER TITLE_______________________________________________________##

        lbl_title = Label(self.root, text="PAYMENT PROCESSING", font=("Arial", 15, "bold"), bg="dark slate gray", fg="seashell2", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=827, height=28)

##___________________________LABEL FRAME_______________________________________________________##

        #Ticket Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Ticket Details", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeleft.place(x=0, y=28, height=90, width=250)

        #Payment Details
        labelframeleft2 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Payment Details", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeleft2.place(x=0, y=120, height=90, width=250)

        labelframeleft3 = LabelFrame(self.root, bg="snow4", relief=RIDGE, bd=0)
        labelframeleft3.place(x=0, y=190, height=77, width=250)

        #Search System
        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeright.place(x=255, y=28, height=310, width=570)

        ##___________________________LABELS AND ENTRIES_______________________________________________________##

        # Ticket id
        lbl_parking_id = Label(labelframeleft, text="Ticket_ID:", font=("Arial", 10, "bold"), padx=2, pady=6)
        lbl_parking_id.grid(row=0, column=0, sticky=W)

        entry_ticket_id = ttk.Entry(labelframeleft, width=20, font=("times new roman", 10, "bold"))
        entry_ticket_id.grid(row=0, column=1)

        # Parking id
        lbl_parking_id = Label(labelframeleft, text="Parking_ID:", font=("Arial", 10, "bold"), padx=2, pady=6)
        lbl_parking_id.grid(row=1, column=0, sticky=W)

        entry_parking_id = ttk.Entry(labelframeleft, font=("times new roman", 10, "bold"))
        entry_parking_id.grid(row=1, column=1)

        # Amount Paid
        lbl_amnt_paid = Label(labelframeleft2, text="Amount Paid:", font=("Arial", 8, "bold"), padx=2, pady=6)
        lbl_amnt_paid.grid(row=0, column=0,)

        entry_amnt_paid = ttk.Entry(labelframeleft2, width=23, font=("times new roman", 8, "bold"))
        entry_amnt_paid.place(x=83, y=7)

        # Succeeding Fee
        lbl_succeeding_fee = Label(labelframeleft2, text="Succeeding Fee:", font=("Arial", 8, "bold"))
        lbl_succeeding_fee.place(x=0, y=28)

        entry_succeeding_fee = ttk.Entry(labelframeleft2, width=21, font=("times new roman", 8, "bold"))
        entry_succeeding_fee.place(x=95, y=30)

        # Initial Fee
        lbl_initial_fee = Label(labelframeleft3, text="Initial Fee:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_initial_fee.place(x=28, y=10)

        entry_initial_fee = ttk.Entry(labelframeleft3, width=19, font=("times new roman", 7))
        entry_initial_fee.place(x=88, y=10)

        # Date
        lbl_date = Label(labelframeleft3, text="Date:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_date.place(x=28, y=30)

        entry_date = ttk.Entry(labelframeleft3, width=24, font=("times new roman", 7))
        entry_date.place(x=63, y=30)

        # Duration
        lbl_duration = Label(labelframeleft3, text="Duration:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_duration.place(x=28, y=50)

        duration_values = ["1 Hour", "2 Hours", "3 Hours", "4 Hours", "5 Hours"]  # Example duration values
        entry_duration = ttk.Combobox(labelframeleft3, values=duration_values, width=17, height=5, font=("times new roman", 7), state="readonly")
        entry_duration.place(x=82, y=50)

        # Search by
        lblSearchBy = Label(labelframeright,font=("Calibre", 8,"bold"),text="Search By:", bg="snow4")
        lblSearchBy.place(x=0, y=2)

        lblSearchBy_values = ["two wheels", "four wheels"]
        lblSearchBy_values = ttk.Combobox(labelframeright, values=lblSearchBy_values, width=17, font=("Arial", 8, "bold"), state="readonly")
        lblSearchBy_values.current(0)
        lblSearchBy_values.place(x=65, y=2)

        txtSearch = ttk.Entry(labelframeright, width=30, font=("times new roman", 8))
        txtSearch.place(x=190, y=2)

##___________________________BUTTON FRAME_______________________________________________________##

        # Button frame
        btn_frame = Frame(self.root, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=268, height=40, width=250)

        # Add button
        btn_add = Button(btn_frame, text="Add", font=("Arial", 8, "bold"), bg="dark slate gray", fg="seashell2", bd=1, width=7, relief=RIDGE)
        btn_add.grid(row=0, column=0, padx=2, pady=4)

        # Update button
        btn_update = Button(btn_frame, text="Update", font=("Arial", 8, "bold"), bg="dark slate gray", fg="seashell2", bd=1, width=7, relief=RIDGE)
        btn_update.grid(row=0, column=1, padx=2, pady=4)

        # Delete button
        btn_delete = Button(btn_frame, text="Delete", font=("Arial", 8, "bold"), bg="dark slate gray", fg="seashell2", bd=1, width=7, relief=RIDGE)
        btn_delete.grid(row=0, column=2, padx=2, pady=4)

        # Reset button
        btn_reset = Button(btn_frame, text="Reset", font=("Arial", 8, "bold"), bg="dark slate gray", fg="seashell2", bd=1, width=7, relief=RIDGE)
        btn_reset.grid(row=0, column=3, padx=2, pady=4)

        #Search Button
        btnSearch = Button(labelframeright, text="Search", font=("Arial", 8, "bold"), bg="dark slate gray",fg="seashell2", width=8)
        btnSearch.place(x=380, y=0)

        #Show All Button
        btnShowAll = Button(labelframeright, text="Show All", font=("Arial", 8, "bold"), bg="dark slate gray",fg="seashell2", width=8)
        btnShowAll.place(x=450, y=0)


##___________________________SHOW DATA TABLE_______________________________________________________##

        details_table = Frame(labelframeright, bd=1, relief=RIDGE)
        details_table.place(x=0, y=24, height=272, width=562)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.paypros_details_table = ttk.Treeview(details_table, column=("Ticket ID", "Parking ID", "Plate No.", "Vehicle Category",
                                                                           "Amount Paid", "Total Fee", "Payment Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.paypros_details_table.xview)
        scroll_y.config(command=self.paypros_details_table.yview)

        self.paypros_details_table.heading("Ticket ID", text="Ticket ID")
        self.paypros_details_table.heading("Parking ID", text="Parking ID")
        self.paypros_details_table.heading("Plate No.", text="Plate No.")
        self.paypros_details_table.heading("Vehicle Category", text="Vehicle Category")
        self.paypros_details_table.heading("Amount Paid", text="Amount Paid")
        self.paypros_details_table.heading("Total Fee", text="Total Fee")
        self.paypros_details_table.heading("Payment Date", text="Payment Date")

        self.paypros_details_table["show"] = "headings"

        self.paypros_details_table.column("Ticket ID", width=100)
        self.paypros_details_table.column("Parking ID",width=100)
        self.paypros_details_table.column("Plate No.",width=100)
        self.paypros_details_table.column("Vehicle Category",width=100)
        self.paypros_details_table.column("Amount Paid",width=90)
        self.paypros_details_table.column("Total Fee",width=90)
        self.paypros_details_table.column("Payment Date",width=100)

        self.paypros_details_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Paypros_Window(root)
    root.configure(bg="snow2")
    root.mainloop()