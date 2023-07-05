from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from transreg import Transreg_Window
from paypros import Paypros_Window
from transacthist import TransactHist_Window
from paymenthist import PaymentHist_Window
from monitoring import Monitoring_Window

class ParkingManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("1000x500+180+105")
        self.root.resizable(0, 0)

##___________________________IMAGE 1_______________________________________________________##
        img1=Image.open(r"C:/Users/Acer/Downloads/parkme/images/frontimge.png")
        img1 = img1.resize((1000,250),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=1,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1000,height=100)

##___________________________HOME TITLE_______________________________________________________##

        lbl_title = Label(self.root,text="PARKING MANAGEMENT SYSTEM",font=("Arial",15,"bold"),bg="seashell2",fg="dark slate gray", bd=1, relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1000,height=28)
        
##___________________________MAIN FRAME_______________________________________________________##

        main_frame = Frame(self.root,bd=0,relief=RIDGE)
        main_frame.place(x=0,y=127,width=1000,height=410)

##___________________________MENU_______________________________________________________##
        
        lbl_home = Label(main_frame,text="HOME",font=("Helvetica",20,"bold"),bg="dark slate gray",fg="seashell2",bd=0,relief=RIDGE)
        lbl_home.place(x=827,y=1.3,width=170)

##___________________________BUTTON FRAME_______________________________________________________##
                
        btn_frame = Frame(main_frame,bd=0,relief=RIDGE)
        btn_frame.place(x=827,y=35,width=170,height=300)
        
        transreg_btn = Button(btn_frame,text="TRANSACTION REGISTER", width=23,height=2,font=("Helvetica",9,"bold"),bg="seashell2",fg="dark slate gray",bd=2,command=self.transreg_details)
        transreg_btn.grid(row=1,column=0)
        
        paypro_btn = Button(btn_frame,text="PAYMENT PROCESSING",width=23,height=2,font=("Helvetica",9,"bold"),bg="seashell2",fg="dark slate gray",bd=2,command=self.paypros_details)
        paypro_btn.grid(row=2,column=0)
        
        transhist_btn = Button(btn_frame,text="TRANSACTION HISTORY",width=23,height=2,font=("Helvetica",9,"bold"),bg="seashell2",fg="dark slate gray",bd=2,command=self.transacthist_details)
        transhist_btn.grid(row=3,column=0)

        payhist_btn = Button(btn_frame,text="PAYMENT HISTORY",width=23,height=2,font=("Helvetica",9,"bold"),bg="seashell2",fg="dark slate gray",bd=2,command=self.paymenthist_details)
        payhist_btn.grid(row=4,column=0)

        occupancy_btn = Button(btn_frame,text="MANAGEMENT & MONITORING",width=23,height=2,font=("Helvetica",8,"bold"),bg="seashell2",fg="dark slate gray",bd=2,command=self.monitoring_details)
        occupancy_btn.grid(row=5,column=0)
##___________________________IMAGE 2_______________________________________________________##

        img2=Image.open(r"C:/Users/Acer/Downloads/parkme/images/parking.jpg")
        img2 = img2.resize((416,300),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE)
        lblimg.place(x=0,y=128,width=416,height=172)

##___________________________IMAGE 3_______________________________________________________##

        img3=Image.open(r"C:/Users/Acer/Downloads/parkme/images/parkingbooth.png")
        img3 = img3.resize((415,200),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root,image=self.photoimg3,bd=1,relief=RIDGE)
        lblimg.place(x=412,y=128,width=415,height=172)

##___________________________IMAGE 4_______________________________________________________##

        img4=Image.open(r"C:/Users/Acer/Downloads/parkme/images/parkingentrance.png")
        img4 = img4.resize((415,200),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(self.root,image=self.photoimg4,bd=1,relief=RIDGE)
        lblimg.place(x=0,y=300,width=415,height=200)

##___________________________IMAGE 5_______________________________________________________##

        img5=Image.open(r"C:/Users/Acer/Downloads/parkme/images/parkingstairs.png")
        img5 = img5.resize((415,200),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(self.root,image=self.photoimg5,bd=1,relief=RIDGE)
        lblimg.place(x=412,y=300,width=415,height=200)

##___________________________LOGO_______________________________________________________##

        img6=Image.open(r"C:/Users/Acer/Downloads/parkme/images/logo2.png")
        img6 = img6.resize((170,110),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg = Label(self.root,image=self.photoimg6,bd=1,relief=RIDGE)
        lblimg.place(x=828,y=408,width=170,height=50)

    def transreg_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Transreg_Window(self.new_window)
    

    def paypros_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Paypros_Window(self.new_window)

    def transacthist_details(self):
        self.new_window = Toplevel(self.root)
        self.app = TransactHist_Window(self.new_window)

    def paymenthist_details(self):
        self.new_window = Toplevel(self.root)
        self.app = PaymentHist_Window(self.new_window)

    def monitoring_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Monitoring_Window(self.new_window)
















if __name__ == "__main__":
    root=Tk()
    obj=ParkingManagementSystem(root)
    root.configure(bg="gray")
    root.mainloop()



