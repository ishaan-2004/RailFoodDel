from tkinter import *
from tkinter import messagebox


def feedback():
   
   fb = Tk()
   fb.title("Online Railway Food Delivery System")
   fb.geometry('750x750')
   fb.config(bg="#093e4a")
   
   # Creating a Text File To Store All the Data
   
   def save():
      
      warn=""
      cname_check = cname.get()
      contact_check = contact.get()
      fback_check = fback.get('1.0','end')
      
      check_count = 0

      if cname_check == "":
         warn = "Name can't be left empty !"
      else:
         check_count += 1
      if contact_check == "":
         warn = "Contact can't be left empty!"
      else:
         check_count += 1
   
      if fback_check == "":
         warn = "Feedback can't be left empty!"
      else:
         check_count += 1
         
      if check_count == 3:

            try:
               f = open("customer_feedback.txt", "a")
               f.write(f"Name : {cname.get()}\n")
               f.write(f"Contact : {contact.get()}\n")
               f.write(f"Feedback: {fback.get('1.0','end')}\n")
               f.write(f"===============================================================\n\n")

               f.close()
                              
               delete()
               
               messagebox.showinfo('Feedback', '😊 Thank You For The Feedback 😊')
               fb.destroy()
               

            except Exception as ep:
               messagebox.showerror('', ep) 
               
      else:
            messagebox.showerror('Error', warn)   
   
   
   # Functions
   
   def delete():
      fback.delete("1.0","end")

   # Frames
   
   frame = Frame(fb, padx=40, pady=20,bd=7,relief=RIDGE)
   frame.pack(expand=True)

   # Labels

   Label(
         frame,
         text="Railway Food Delivery System",
         font=("Times", "24", "bold")
         ).grid(row=0, columnspan=5, pady=10)

   Label(
         frame,
         text='Feedback',
         font=("Arial", "18","bold","underline","italic")
         ).grid(row=1, columnspan=4, pady=10)
   
   Label(
      frame, 
      text='Name :', 
      font=("Times", "14")
      ).grid(row=2, column=0, pady=10)
   
   Label(
      frame, 
      text='Contact :', 
      font=("Times", "14")
      ).grid(row=3, column=0, pady=10)

   # Entry Widgets

   
   cname=Entry(frame, width=30)
   cname.grid(row=2,column=1,pady=10)
   
   contact=Entry(frame, width=30)
   contact.grid(row=3,column=1,pady=10)
   
   fback = Text(frame, height=15, width=40,relief=RIDGE,bd=4)
   fback.grid(row=4, columnspan=5)
   fback.configure(font=("Courier",15))

   # Buttons 
   clear = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=delete)
   sub = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:[save()])
   ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:[fb.destroy()])

   clear.grid(row=12, column=0, pady=30,padx=22)
   sub.grid(row=12, column=1, pady=30)
   ext.grid(row=12, column=2, pady=30,padx=12)


   fb.mainloop()


