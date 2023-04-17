import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
# from tkinter import filedialog
from PyPDF2 import PdfFileReader,PdfFileWriter
import os
import customtkinter
from customtkinter import *


home_directory = os.path.expanduser( '~' )
print( home_directory )
  
  

root=tk.Tk()
root.title("bdf protector")
root["bg"]="black"
root.geometry("850x440+300+200")
root.iconbitmap("images/pdf.ico")
root.resizable(0,0)


def browse():
     global filename
     filename=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(("PDF FILE","*pdf"),("all files","*.*")))
     explore_entry.configure(state=NORMAL)
     explore_entry.delete(0,1000)
     explore_entry.insert(END,filename)
     explore_entry.configure(state=DISABLED)

def protect():
    global filename
    link=".pdf"
    pas=pass_entry.get()
    rename=rename_entry.get()
    explor=explore_entry.get()
    if pas=="" and explor=="" and rename=="":
        messagebox.showerror("ERORR","please input information....")
    elif link not in explor:
        messagebox.showinfo("Erorr","Enter Pdf File Please.")
    elif rename=="":
        messagebox.showinfo("Erorr","Please Rename Your File...")
    elif pas=="":
        messagebox.showinfo("Erorr","Enter Password Please.")
    else:
        try:
            out=PdfFileWriter()
            file=PdfFileReader(open(f"{filename}","+rb"))
            print(file)
            num=file.numPages
            for i in range(num):
             page=file.getPage(i)
             out.addPage(page)
            out.encrypt(pas,use_128bit=True)
            file_read=open(f"output files//{rename}.pdf","wb")
            out.write(file_read)
            file_read.close()
            messagebox.showinfo("ALL DONE","File Generate Successfully IN [output files]..")
            explore_entry.delete(0,100)
            rename_entry.delete(0,100)
            pass_entry.delete(0,100)
        except:
            messagebox.showerror("ERORR","REORR")
            explore_entry.delete(0,200)
            rename_entry.delete(0,100)
            pass_entry.delete(0,100)
            
#main tkinter components......
img=tk.PhotoImage(file="images\\protect.png")

lbl1=tk.Label(root,image=img,bg="black").place(x=0,y=0)
lbl0=tk.Label(text="Note:Use Pdf Files Only..........................                                Made By: AHMED RAMADAN",fg="white",bg="red",font=("arail,20,bold")).place(x=0,y=205)

lbl2=tk.Label(text="File Name:",fg="white",bg="black",font=("arail,20,bold")).place(x=10,y=250)
lbl3=tk.Label(text="Rename File:",fg="white",bg="black",font=("arail,20,bold")).place(x=10,y=300)
lbl4=tk.Label(text="Password:",fg="white",bg="black",font=("arail,20,bold")).place(x=10,y=350)

explore_entry=tk.Entry(root,width=50,highlightthickness=6,font=("arail,5,bold"))
explore_entry.place(x=150,y=250)
explore_entry.configure(state=DISABLED)

rename_entry=tk.Entry(root,width=50,highlightthickness=6,font=("arail,5,bold"))
rename_entry.place(x=150,y=300)


pass_entry=tk.Entry(root,width=50,highlightthickness=6,font=("arail,5,bold"))
pass_entry.place(x=150,y=350)


button_img=PhotoImage(file="images//prowse.png")
prowse_button=tk.Button(root,image=button_img,bg="black",width=50,height=50,bd=0,command=browse).place(x=770,y=242)
send_button=customtkinter.CTkButton(root,text="Protect Your File..",font=("arial",20,"bold"),command=protect,border_color="green",hover_color="green",corner_radius=12).place(x=350,y=395)

root.mainloop()
