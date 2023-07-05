from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow

class Monitoring_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("827x340+180+263")
        self.root.resizable(0, 0)

##___________________________TRANSACTION REGISTER TITLE_______________________________________________________##

        lbl_title = Label(self.root, text="PARKING MANAGEMENT AND MONITORING", font=("Arial", 15, "bold"), bg="dark slate gray", fg="seashell2", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=827, height=28)

##___________________________TRANSACTION REGISTER TITLE_______________________________________________________##

        lbl_title = Label(self.root, text="TRANSACTION REGISTER", font=("Arial", 15, "bold"), bg="dark slate gray", fg="seashell2", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=827, height=28)

##___________________________LABEL FRAME_______________________________________________________##

        #Parking Space
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Parking Space Details", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeleft.place(x=0, y=28, height=150, width=250)

        labelframeleft2 = LabelFrame(self.root, bg="snow4", relief=RIDGE, bd=0)
        labelframeleft2.place(x=0, y=175, height=80, width=250)

        #Search_System
        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeright.place(x=255, y=28, height=310, width=570)

        ##___________________________LABELS AND ENTRIES_______________________________________________________##

        # Parking id
        lbl_parking_id = Label(labelframeleft, text="Parking_ID:", font=("Arial", 10, "bold"))
        lbl_parking_id.grid(row=0, column=0, sticky=W)

        entry_parking_id = ttk.Entry(labelframeleft, width=21, font=("times new roman", 10, "bold"))
        entry_parking_id.grid(row=0, column=1)

        # Parking category
        lbl_parking_categ = Label(labelframeleft, text="Parking Category:", font=("Arial", 9, "bold"))
        lbl_parking_categ.place(x=0, y=25)

        parking_categ_values = ["two wheels", "four wheels"]
        entry_parking_categ = ttk.Combobox(labelframeleft, values=parking_categ_values, width=17, font=("times new roman", 8, "bold"), state="readonly")
        entry_parking_categ.place(x=105, y=25)

        # Availability
        lbl_avail = Label(labelframeleft2, text="Availability:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_avail.place(x=20, y=10)

        entry_avail = ttk.Entry(labelframeleft2,  width=23, font=("times new roman", 7))
        entry_avail.place(x=88, y=10)

        # Initial fee
        lbl_initial_fee = Label(labelframeleft2, text="Initial Fee:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_initial_fee.place(x=20, y=30)

        entry_initial_fee = ttk.Entry(labelframeleft2, width=24, font=("times new roman", 7))
        entry_initial_fee.place(x=83, y=30)

        # Succeeding fee
        lbl_succ_fee = Label(labelframeleft2, text="Succeeding Fee:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_succ_fee.place(x=18, y=50)

        entry_succ_fee = ttk.Entry(labelframeleft2, width=18, font=("times new roman", 7))
        entry_succ_fee.place(x=113, y=50)

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
        btn_frame.place(x=0, y=250, height=40, width=250)

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

        monitoring_details_table = Frame(labelframeright, bd=1, relief=RIDGE)
        monitoring_details_table.place(x=0, y=24, height=272, width=562)

        scroll_y = ttk.Scrollbar(monitoring_details_table,orient=VERTICAL)

        self.monitoring_details_table = ttk.Treeview(monitoring_details_table, column=("Parking ID", "Parking Category", "Parking Availability", 
                                                                           "Initial Fee", "Succeeding Fee"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_y.config(command=self.monitoring_details_table.yview)

        self.monitoring_details_table.heading("Parking ID", text="Parking ID")
        self.monitoring_details_table.heading("Parking Category", text="Parking Category")
        self.monitoring_details_table.heading("Parking Availability", text="Parking Availability")
        self.monitoring_details_table.heading("Initial Fee", text="Initial Fee")
        self.monitoring_details_table.heading("Succeeding Fee", text="Succeeding Fee")

        self.monitoring_details_table["show"] = "headings"

        self.monitoring_details_table.column("Parking ID",width=70)
        self.monitoring_details_table.column("Parking Category",width=70)
        self.monitoring_details_table.column("Parking Availability",width=80)
        self.monitoring_details_table.column("Initial Fee",width=50)
        self.monitoring_details_table.column("Succeeding Fee",width=50)

        self.monitoring_details_table.pack(fill=BOTH, expand=1)

##___________________________IMAGES_______________________________________________________##

        img9=Image.open(r"C:/Users/Acer/Downloads/parkme/images/two wheels.png")
        img9 = img9.resize((200,100),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        lblimg = Label(self.root,image=self.photoimg9,bd=2,relief=RIDGE)
        lblimg.place(x=25,y=95,width=100,height=75)

        img10=Image.open(r"C:/Users/Acer/Downloads/parkme/images/four wheels.png")
        img10 = img10.resize((100,90),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        lblimg = Label(self.root,image=self.photoimg10,bd=2,relief=RIDGE)
        lblimg.place(x=123,y=95,width=100,height=75)

if __name__ == "__main__":
    root = Tk()
    obj = Monitoring_Window(root)
    root.configure(bg="snow2")
    root.mainloop()