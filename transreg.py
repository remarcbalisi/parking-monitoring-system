from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow

from config import CURRENT_DIRECTORY
from db import insert_new_vehicle


class Transreg_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("827x340+180+263")
        self.root.resizable(0, 0)

##___________________________VARIABLES_______________________________________________________##

        self.var_parkingid = StringVar()
        self.var_plateno=StringVar()
        self.var_vehiclecategory=StringVar()
        self.var_timein=StringVar()
        self.var_date=StringVar()
        self.var_duration=StringVar()

##___________________________TRANSACTION REGISTER TITLE_______________________________________________________##

        lbl_title = Label(self.root, text="TRANSACTION REGISTER", font=("Arial", 15, "bold"), bg="dark slate gray", fg="seashell2", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=827, height=28)

##___________________________LABEL FRAME_______________________________________________________##

        #Parking Space
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Parking Space Details", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeleft.place(x=0, y=28, height=130, width=250)

        #Vehicle
        labelframeleft2 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Vehicle Details", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeleft2.place(x=0, y=160, height=90, width=250)

        labelframeleft3 = LabelFrame(self.root, bg="snow4", relief=RIDGE, bd=0)
        labelframeleft3.place(x=0, y=231, height=80, width=250)

        #Search_System
        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("Arial", 7, "bold"), padx=2, fg="dark slate gray")
        labelframeright.place(x=255, y=28, height=310, width=570)

        ##___________________________LABELS AND ENTRIES_______________________________________________________##

        # Parking id
        lbl_parking_id = Label(labelframeleft, text="Parking_ID:", font=("Arial", 10, "bold"), padx=2, pady=6)
        lbl_parking_id.grid(row=0, column=0, sticky=W)

        entry_parking_id = ttk.Entry(labelframeleft, textvariable=self.var_parkingid, width=20, font=("times new roman", 10, "bold"))
        entry_parking_id.grid(row=0, column=1)

        # Plate no.
        lbl_plate_no = Label(labelframeleft2, text="Plate No.:", font=("Arial", 10, "bold"), padx=2, pady=6)
        lbl_plate_no.grid(row=0, column=0,)

        entry_plate_no = ttk.Entry(labelframeleft2, textvariable=self.var_plateno, width=25, font=("times new roman", 8, "bold"))
        entry_plate_no.place(x=74, y=7)

        # Vehicle type
        lbl_vehicle_type = Label(labelframeleft2, text="Vehicle Category:", font=("Arial", 8, "bold"))
        lbl_vehicle_type.place(x=0, y=28)

        vehicle_type_values = ["two wheels", "four wheels"]
        entry_vehicle_type = ttk.Combobox(labelframeleft2, textvariable=self.var_vehiclecategory, values=vehicle_type_values, width=17, font=("times new roman", 8, "bold"), state="readonly")
        entry_vehicle_type.place(x=105, y=30)

        # Time in
        lbl_time_in = Label(labelframeleft3, text="Time In:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_time_in.place(x=35, y=10)

        entry_time_in = ttk.Entry(labelframeleft3, textvariable=self.var_timein, width=19, font=("times new roman", 7))
        entry_time_in.place(x=88, y=10)

        # Date
        lbl_date = Label(labelframeleft3, text="Date:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_date.place(x=35, y=30)

        entry_date = ttk.Entry(labelframeleft3, textvariable=self.var_date, width=22, font=("times new roman", 7))
        entry_date.place(x=73, y=30)

        # Duration
        lbl_duration = Label(labelframeleft3, text="Duration:", font=("Calibre", 8,"bold"), bg="snow4")
        lbl_duration.place(x=35, y=50)

        duration_values = ["1 Hour", "2 Hours", "3 Hours", "4 Hours", "5 Hours"]  # Example duration values
        entry_duration = ttk.Combobox(labelframeleft3, textvariable=self.var_duration, values=duration_values, width=15, height=5, font=("times new roman", 7), state="readonly")
        entry_duration.place(x=89, y=50)

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
        btn_frame.place(x=0, y=305, height=40, width=250)

        # Add button
        btn_add = Button(btn_frame,
                         text="Add",
                         font=("Arial", 8, "bold"),
                         bg="dark slate gray",
                         fg="seashell2",
                         bd=1,
                         width=7,
                         relief=RIDGE,
                         command=lambda: insert_new_vehicle(entry_plate_no.get(), entry_vehicle_type.get())
                         )
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

        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.transreg_details_table = ttk.Treeview(details_table, column=("Parking ID", "Plate No.", "Vehicle Category", 
                                                                           "Time In", "Date", "Duration"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_y.config(command=self.transreg_details_table.yview)

        self.transreg_details_table.heading("Parking ID", text="Parking ID")
        self.transreg_details_table.heading("Plate No.", text="Plate No.")
        self.transreg_details_table.heading("Vehicle Category", text="Vehicle Category")
        self.transreg_details_table.heading("Time In", text="Time In")
        self.transreg_details_table.heading("Date", text="Date")
        self.transreg_details_table.heading("Duration", text="Duration")

        self.transreg_details_table["show"] = "headings"

        self.transreg_details_table.column("Parking ID",width=70)
        self.transreg_details_table.column("Plate No.",width=70)
        self.transreg_details_table.column("Vehicle Category",width=80)
        self.transreg_details_table.column("Time In",width=50)
        self.transreg_details_table.column("Date",width=50)
        self.transreg_details_table.column("Duration",width=40)

        self.transreg_details_table.pack(fill=BOTH, expand=1)


##___________________________IMAGES_______________________________________________________##

        img7=Image.open(f"{CURRENT_DIRECTORY}/images/two wheels.png")
        img7 = img7.resize((200,100),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        lblimg = Label(self.root,image=self.photoimg7,bd=2,relief=RIDGE)
        lblimg.place(x=25,y=73,width=100,height=75)

        img8=Image.open(f"{CURRENT_DIRECTORY}/images/four wheels.png")
        img8 = img8.resize((100,90),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lblimg = Label(self.root,image=self.photoimg8,bd=2,relief=RIDGE)
        lblimg.place(x=123,y=73,width=100,height=75)


if __name__ == "__main__":
    root = Tk()
    obj = Transreg_Window(root)
    root.configure(bg="snow2")
    root.mainloop()
