from tkinter import *
from tkinter import ttk

class PaymentHist_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("827x340+180+263")
        self.root.resizable(0, 0)

##___________________________TRANSACTION REGISTER TITLE_______________________________________________________##

        lbl_title = Label(self.root, text="PAYMENT HISTORY", font=("Arial", 15, "bold"), bg="dark slate gray", fg="seashell2", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=827, height=28)

##___________________________LABEL FRAME_______________________________________________________##

   #Search System
        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeright.place(x=255, y=28, height=310, width=570)

##___________________________LABELS AND ENTRIES_______________________________________________________##
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

        #Search Button
        btnSearch = Button(labelframeright, text="Search", font=("Arial", 8, "bold"), bg="dark slate gray",fg="seashell2", width=8)
        btnSearch.place(x=380, y=0)

        #Show All Button
        btnShowAll = Button(labelframeright, text="Show All", font=("Arial", 8, "bold"), bg="dark slate gray",fg="seashell2", width=8)
        btnShowAll.place(x=450, y=0)

##___________________________SHOW DATA TABLE_______________________________________________________##

        paymenthist_details_table = Frame(labelframeright, bd=1, relief=RIDGE)
        paymenthist_details_table.place(x=0, y=24, height=272, width=562)

        scroll_x = ttk.Scrollbar(paymenthist_details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(paymenthist_details_table,orient=VERTICAL)

        self.paymenthist_details_table = ttk.Treeview(paymenthist_details_table, column=("Ticket ID", "Parking ID", "Plate No.", 
                                                                         "Vehicle Category", "Payment Date", "Total Fee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.paymenthist_details_table.xview)
        scroll_y.config(command=self.paymenthist_details_table.yview)

        self.paymenthist_details_table.heading("Ticket ID", text="Ticket ID")
        self.paymenthist_details_table.heading("Parking ID", text="Parking ID")
        self.paymenthist_details_table.heading("Plate No.", text="Plate No.")
        self.paymenthist_details_table.heading("Vehicle Category", text="Vehicle Category")
        self.paymenthist_details_table.heading("Payment Date", text="Payment Date")
        self.paymenthist_details_table.heading("Total Fee", text="Total Fee")

        self.paymenthist_details_table["show"] = "headings"

        self.paymenthist_details_table.column("Ticket ID", width=100)
        self.paymenthist_details_table.column("Parking ID",width=100)
        self.paymenthist_details_table.column("Plate No.",width=100)
        self.paymenthist_details_table.column("Vehicle Category",width=100)
        self.paymenthist_details_table.column("Payment Date",width=100)
        self.paymenthist_details_table.column("Total Fee",width=100)

        self.paymenthist_details_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = PaymentHist_Window(root)
    root.configure(bg="snow2")
    root.mainloop()