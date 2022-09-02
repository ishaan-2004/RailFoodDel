import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import mysql.connector
from feedback import *

def menu():
        app=Tk()
        app.title("Online Railway Food Delivery System")
        w=app.winfo_screenwidth()
        h=app.winfo_screenheight()
        app.state("zoomed")
        
        
        # Creating Database
        
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password123",
        database="railfood_del"
        )
        c=mydb.cursor()

        
        c.execute("CREATE DATABASE IF NOT EXISTS railfood_del")
        c.execute("""CREATE TABLE IF NOT EXISTS orders(user_id INT AUTO_INCREMENT PRIMARY KEY , \
            order_id VARCHAR(20), total_value INT(10),\
            daal INT(10), dumaloo INT(10),thali INT(10), \
            purisabji INT(10), pavbhaji INT(10), paneer INT(10), \
            salad INT(10), rice INT(10), roti INT(10), \
                
                eggcurry INT(10), fish_fry INT(10), kebab INT(10), \
                platter INT(10), biriyani INT(10), fish_curry INT(10), \
                chicken INT(10), mutton INT(10), roll INT(10), \
                    
                    noodles INT(10), dosa INT(10), idli INT(10), \
                    sandwich INT(10), pasta INT(10), burger INT(10), \
                    cutlets INT(10), samosa INT(10), kachori INT(10) 

                ) """)
            
            
        #Variables

        
        e_roti=StringVar()
        e_daal=StringVar()
        e_purisabji = StringVar()
        e_rice = StringVar()
        e_dumaloo = StringVar()
        e_thali = StringVar()
        e_pavbhaji = StringVar()
        e_salad = StringVar()
        e_paneer = StringVar()

        e_noodles=StringVar()
        e_dosa = StringVar()
        e_idli = StringVar()
        e_cutlets = StringVar()
        e_sandwich = StringVar()
        e_pasta = StringVar()
        e_burger = StringVar()
        e_samosa = StringVar()
        e_kachori = StringVar()

        e_egg=StringVar()
        e_fishfry = StringVar()
        e_platter = StringVar()
        e_biriyani = StringVar()
        e_fish = StringVar()
        e_mutton = StringVar()
        e_kebab = StringVar()
        e_chicken = StringVar()
        e_chroll = StringVar()



        CostOfVegvar=StringVar()
        CostOfNVegvar=StringVar()
        CostOfFastvar=StringVar()
        subtotalvar=StringVar()
        Deliveryvar=StringVar()
        totalcostvar=StringVar()

        e_roti.set('0')
        e_daal.set('0')
        e_purisabji.set('0')
        e_rice.set('0')
        e_pavbhaji.set('0')
        e_salad.set('0')
        e_thali.set('0')
        e_dumaloo.set('0')
        e_paneer.set('0')

        e_egg.set('0')
        e_fishfry.set('0')
        e_platter.set('0')
        e_biriyani.set('0')
        e_fish.set('0')
        e_mutton.set('0')
        e_kebab.set('0')
        e_chicken.set('0')
        e_chroll.set('0')

        e_noodles.set('0')
        e_dosa.set('0')
        e_idli.set('0')
        e_cutlets.set('0')
        e_sandwich.set('0')
        e_pasta.set('0')
        e_burger.set('0')
        e_samosa.set('0')
        e_kachori.set('0')

        

        

        # FRAMES
        
        topFrame=Frame(app,bd=10,relief=GROOVE,bg="#2d5e69",width=w//4)
        topFrame.pack(side=TOP,fill=X)
        labelTitle=Label(topFrame,text='Online Railway Food Delivery System',font=('times nwe roman',30,'bold'),fg='white',bd=9, bg="#093e4a")
        labelTitle.pack(fill=X)
        
        frame1=Frame(app,bd=10,relief=RIDGE,bg="#447c84")
        frame1.pack(fill=X)

        rightFrame=Frame(app,bd=15,relief=RIDGE,bg="#447c84")
        rightFrame.pack(side=RIGHT)

        menuFrame=Frame(app,bd=10,relief=RIDGE,bg="#2d5e69")
        menuFrame.pack(side=LEFT,fill=Y)

        costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg="#2d5e69",pady=10,padx=80)
        costFrame.pack(side=BOTTOM,fill=X)

        foodFrame=LabelFrame(menuFrame,text='Main Course',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg="#093e4a",pady=8)
        foodFrame.pack(side=LEFT,fill=Y)

        fastFrame=LabelFrame(menuFrame,text='Fast Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg="#093e4a",pady=8)
        fastFrame.pack(side=LEFT,fill=Y)

        rightFrame=Frame(app,bd=10,relief=RIDGE,bg="#447c84")
        rightFrame.pack(side=RIGHT,fill=Y)

        recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg="#447c84")
        recieptFrame.pack()

        buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg="#447c84")
        buttonFrame.pack(side=BOTTOM)

        labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',14,'bold'),bg="#2d5e69",fg='white')
        labelSubTotal.grid(row=0,column=0)

        labelDelivery=Label(costFrame,text='Delivery Charge',font=('arial',14,'bold'),bg="#2d5e69",fg='white')
        labelDelivery.grid(row=1,column=0)

        labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',14,'bold'),bg="#2d5e69",fg='white')
        labelTotalCost.grid(row=2,column=0)
        
        #costlabels & entry fields

        labelCostOfVeg=Label(costFrame,text='Cost of Veg Items',font=('arial',16,'bold'),bg="#2d5e69",fg='white')
        labelCostOfVeg.grid(row=0,column=0,sticky=W)

        textCostOfVeg=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostOfVegvar)
        textCostOfVeg.grid(row=0,column=1,padx=41)

        labelCostOfNVeg=Label(costFrame,text='Cost of Non Veg Items',font=('arial',16,'bold'),bg="#2d5e69",fg='white')
        labelCostOfNVeg.grid(row=1,column=0,sticky=W)

        textCostOfNVeg=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostOfNVegvar)
        textCostOfNVeg.grid(row=1,column=1,padx=41)

        labelCostOfFast=Label(costFrame,text='Cost of Fast Food',font=('arial',16,'bold'),bg="#2d5e69",fg='white')
        labelCostOfFast.grid(row=2,column=0,sticky=W)

        textCostOfFast=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostOfFastvar)
        textCostOfFast.grid(row=2,column=1,padx=41)

        labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg="#2d5e69",fg='white')
        labelSubTotal.grid(row=0,column=2)

        textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
        textSubTotal.grid(row=0,column=3,padx=41)

        labelDelivery=Label(costFrame,text='Delivery Charge',font=('arial',16,'bold'),bg="#2d5e69",fg='white')
        labelDelivery.grid(row=1,column=2)

        textDelivery=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=Deliveryvar)
        textDelivery.grid(row=1,column=3,padx=41)

        labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg="#2d5e69",fg='white')
        labelTotalCost.grid(row=2,column=2)

        textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
        textTotalCost.grid(row=2,column=3,padx=41)
        
        # Text Area for Receipt

        textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=35)
        textReceipt.grid(row=0,column=0)



        #FUNCTIONS


        def receipt():
            global billnumber,date
            if CostOfVegvar.get() != '' or CostOfFastvar.get() != '' or CostOfNVegvar.get() != '':
                textReceipt.delete(1.0,END)
                x=random.randint(100,10000)
                billnumber='BILL'+str(x)
                date=time.strftime('%d/%m/%Y')
                textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
                textReceipt.insert(END,'***************************************************************\n')
                textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
                textReceipt.insert(END,'***************************************************************\n')
                

                if e_daal.get()!='0':
                    textReceipt.insert(END,f'Daal:\t\t\t{int(e_daal.get())*50}\n\n')

                if e_dumaloo.get() != '0':
                    textReceipt.insert(END, f'Dum Aloo:\t\t\t{int(e_dumaloo.get()) * 50}\n\n')

                if e_thali.get() != '0':
                    textReceipt.insert(END, f'Thali:\t\t\t{int(e_thali.get()) * 90}\n\n')

                if e_purisabji.get() != '0':
                    textReceipt.insert(END, f'Puri Sabji:\t\t\t{int(e_purisabji.get()) * 60}\n\n')

                if e_pavbhaji.get() != '0':
                    textReceipt.insert(END, f'Pav Bhaji:\t\t\t{int(e_pavbhaji.get()) * 70}\n\n')

                if e_paneer.get() != '0':
                    textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 70}\n\n')

                if e_salad.get() != '0':
                    textReceipt.insert(END, f'Salad:\t\t\t{int(e_salad.get()) * 30}\n\n')      

                if e_rice.get() != '0':
                    textReceipt.insert(END, f'Rice:\t\t\t{int(e_rice.get()) * 50}\n\n')    

                if e_roti.get()!='0':
                    textReceipt.insert(END,f'Roti:\t\t\t{int(e_roti.get())*10}\n\n')  


                if e_egg.get() != '0':
                    textReceipt.insert(END, f'Egg Curry:\t\t\t{int(e_egg.get()) * 120}\n\n')

                if e_fishfry.get()!='0':
                    textReceipt.insert(END,f'Fish Fry:\t\t\t{int(e_fishfry.get())*120}\n\n')
                    
                if e_kebab.get() != '0':
                    textReceipt.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 100}\n\n')

                if e_platter.get() != '0':
                    textReceipt.insert(END, f'Platter:\t\t\t{int(e_platter.get()) * 180}\n\n')

                if e_biriyani.get() != '0':
                    textReceipt.insert(END, f'Biriyani:\t\t\t{int(e_biriyani.get()) * 150}\n\n')

                if e_fish.get() != '0':
                    textReceipt.insert(END, f'Fish Curry:\t\t\t{int(e_fish.get()) * 180}\n\n')     

                if e_chicken.get() != '0':
                    textReceipt.insert(END, f'Butter Chicken:\t\t\t{int(e_chicken.get()) * 200}\n\n')

                if e_mutton.get() != '0':
                    textReceipt.insert(END, f'Mutton Curry:\t\t\t{int(e_mutton.get()) * 250}\n\n')

                if e_chroll.get() != '0':
                    textReceipt.insert(END, f'Chicken Roll :\t\t\t{int(e_chroll.get()) * 80}\n\n')


                if e_noodles.get() != '0':
                    textReceipt.insert(END, f'Noodles:\t\t\t{int(e_noodles.get()) * 80}\n\n')

                if e_dosa.get() != '0':
                    textReceipt.insert(END, f'Dosa:\t\t\t{int(e_dosa.get()) * 60}\n\n')

                if e_idli.get() != '0':
                    textReceipt.insert(END, f'Idli:\t\t\t{int(e_idli.get()) * 40}\n\n')

                if e_sandwich.get() != '0':
                    textReceipt.insert(END, f'Sandwich:\t\t\t{int(e_sandwich.get()) * 50}\n\n')

                if e_pasta.get() != '0':
                    textReceipt.insert(END, f'Pasta:\t\t\t{int(e_pasta.get()) * 60}\n\n')               

                if e_burger.get() != '0':
                    textReceipt.insert(END, f'Burger:\t\t\t{int(e_burger.get()) * 60}\n\n')

                if e_cutlets.get() != '0':
                    textReceipt.insert(END, f'Cutlets:\t\t\t{int(e_cutlets.get()) * 80}\n\n')

                if e_samosa.get() != '0':
                    textReceipt.insert(END, f'Samosa:\t\t\t{int(e_samosa.get()) * 15}\n\n')

                if e_kachori.get() != '0':
                    textReceipt.insert(END, f'Kachori:\t\t\t{int(e_kachori.get()) * 15}\n\n')    

                textReceipt.insert(END,'***************************************************************\n')
                if CostOfVegvar.get()!='0 Rs':
                    textReceipt.insert(END,f'Cost Of Veg Items:\t\t\t{priceofVeg} Rs\n\n')
                if CostOfNVegvar.get() != '0 Rs':
                    textReceipt.insert(END,f'Cost Of Non Veg Items:\t\t\t{priceofNVeg} Rs\n\n')
                if CostOfFastvar.get() != '0 Rs':
                    textReceipt.insert(END,f'Cost Of Fast Food:\t\t\t{priceofFast} Rs\n\n')

                textReceipt.insert(END, f'Sub Total:\t\t\t{subtotalofItems} Rs\n\n')
                textReceipt.insert(END, f'Delivery Charge:\t\t\t{50} Rs\n\n')
                textReceipt.insert(END, f'Total Cost:\t\t\t{subtotalofItems+50} Rs\n\n')
                textReceipt.insert(END,'***************************************************************\n')
                textReceipt.insert(END,'\t!!! Order Placed Successfully !!! \n\n')
                textReceipt.insert(END,'       Your Order Will Be Delivered On Your Seat\n  \t     At The Chosen Station\n\n')
                textReceipt.insert(END,'       \tThe Payment Has To Be Done\n \t       At The Time Of Delivery \n\n')
                textReceipt.insert(END,'          ***** Be Sure To Leave A Feedback ***** \n')
                
                try:

                    sql_command="INSERT INTO orders (order_id,total_value,daal,dumaloo,thali,purisabji,pavbhaji,paneer,salad, rice, roti, \
                        eggcurry, fish_fry, kebab, platter, biriyani, fish_curry, chicken, mutton, roll, \
                            noodles, dosa, idli, sandwich, pasta, burger,cutlets, samosa, kachori) \
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    
                    values=(x,subtotalofItems+50,e_daal.get(),e_dumaloo.get(),e_thali.get(),e_purisabji.get(),e_pavbhaji.get(),e_paneer.get(),e_salad.get(),e_rice.get(),e_roti.get(), \
                        e_egg.get(), e_fishfry.get(), e_kebab.get(), e_platter.get(), e_biriyani.get(), e_fish.get(), e_chicken.get(), e_mutton.get(), e_chroll.get(), \
                            e_noodles.get(), e_dosa.get(), e_idli.get(), e_sandwich.get(), e_pasta.get(), e_burger.get(), e_cutlets.get(), e_samosa.get(), e_kachori.get())
                    
                    
                    c.execute(sql_command,values)


                    mydb.commit()
                    mydb.close()
                    
                    

                except Exception as ep:
                    messagebox.showerror('', ep)

            else:
                messagebox.showerror('Error','No Item Is selected')

        def totalcost():
            global priceofVeg,priceofNVeg,priceofFast,subtotalofItems
            
            item1=int(e_daal.get())
            item2=int(e_dumaloo.get())
            item3=int(e_thali.get())
            item4 = int(e_purisabji.get())
            item5 = int(e_pavbhaji.get())
            item6 = int(e_paneer.get())
            item7 = int(e_salad.get())
            item8 = int(e_rice.get())
            item9 = int(e_roti.get())

            item10 = int(e_egg.get())
            item11 = int(e_fishfry.get())
            item12 = int(e_kebab.get())
            item13 = int(e_platter.get())
            item14 = int(e_biriyani.get())
            item15 = int(e_fish.get())
            item16 = int(e_chicken.get())
            item17 = int(e_mutton.get())
            item18 = int(e_chroll.get())

            item19 = int(e_noodles.get())
            item20 = int(e_dosa.get())
            item21 = int(e_idli.get())
            item22 = int(e_sandwich.get())
            item23 = int(e_pasta.get())
            item24 = int(e_burger.get())
            item25 = int(e_cutlets.get())
            item26 = int(e_samosa.get())
            item27 = int(e_kachori.get())

            priceofVeg=(item1*50)+(item2*50)+(item3*90)+(item4*60)+ (item5*70) + (item6 * 70) + (item7 * 30) \
                        + (item8 * 50) + (item9 * 10)

            priceofNVeg=(item10*120)+(item11*120)+ (item12 * 100) + (item13 * 180) + (item14 * 150) + (item15 * 180) \
                        + (item16 * 200) + (item17 * 250) + (item18 * 80)

            priceofFast=(item19*80)+(item20*60)+ (item21 * 40) + (item22 * 50) + (item23 * 60) + (item24 * 60) \
                        + (item25 * 80) + (item26 * 15) + (item27 * 15)

            CostOfVegvar.set(str(priceofVeg)+ ' Rs')
            CostOfNVegvar.set(str(priceofNVeg)+ ' Rs')
            CostOfFastvar.set(str(priceofFast)+ ' Rs')

            subtotalofItems=priceofVeg+priceofNVeg+priceofFast
            subtotalvar.set(str(subtotalofItems)+' Rs')

            Deliveryvar.set('50 Rs')

            tottalcost=subtotalofItems+50
            totalcostvar.set(str(tottalcost)+' Rs')

        def reset():
            textReceipt.delete(1.0,END)
            e_roti.set('0')
            e_daal.set('0')
            e_purisabji.set('0')
            e_rice.set('0')
            e_pavbhaji.set('0')
            e_salad.set('0')
            e_thali.set('0')
            e_dumaloo.set('0')
            e_paneer.set('0')

            e_egg.set('0')
            e_fishfry.set('0')
            e_platter.set('0')
            e_biriyani.set('0')
            e_fish.set('0')
            e_mutton.set('0')
            e_kebab.set('0')
            e_chicken.set('0')
            e_chroll.set('0')

            e_noodles.set('0')
            e_dosa.set('0')
            e_idli.set('0')
            e_cutlets.set('0')
            e_sandwich.set('0')
            e_pasta.set('0')
            e_burger.set('0')
            e_samosa.set('0')
            e_kachori.set('0')
            
            CostOfVegvar.set('')
            CostOfNVegvar.set('')
            CostOfFastvar.set('')
            subtotalvar.set('')
            Deliveryvar.set('')
            totalcostvar.set('')
            

        # VEG

        q=[]
        for i in range(0,11):
            q.append(i)

        g1=Label(foodFrame,text="VEG",font=('arial',15,'italic'),fg='white',bg='green').grid(row=0,column=0,sticky=W)

        p=Label(foodFrame,text="Price",font=('arial',15,'italic'),padx=12).grid(row=0,column=1,sticky=EW)

        quan=Label(foodFrame,text="Quantity",font=('arial',15,'italic'),padx=11).grid(row=0,column=2,sticky=EW,pady=10)

        
        daal=Label(foodFrame,text='Daal',font=('arial',18,'bold' ),pady=8)
        daal.grid(row=1,column=0,sticky=W)

        dumaloo=Label(foodFrame,text='Dum Aloo',font=('arial',18,'bold'),pady=8 )
        dumaloo.grid(row=2,column=0,sticky=W)

        thali=Label(foodFrame,text='Thali',font=('arial',18,'bold' ),pady=8)
        thali.grid(row=3,column=0,sticky=W)

        purisabji=Label(foodFrame,text='Puri Sabji',font=('arial',18,'bold' ),pady=8 )
        purisabji.grid(row=4,column=0,sticky=W)

        pavbhaji=Label(foodFrame,text='Pav Bhaji',font=('arial',18,'bold' ),pady=8 )
        pavbhaji.grid(row=5,column=0,sticky=W)

        paneer=Label(foodFrame,text='Paneer',font=('arial',18,'bold'),pady=8)
        paneer.grid(row=6,column=0,sticky=W)

        salad=Label(foodFrame,text='Salad',font=('arial',18,'bold' ),pady=8 )
        salad.grid(row=7,column=0,sticky=W)

        rice=Label(foodFrame,text='Rice',font=('arial',18,'bold'),pady=8)
        rice.grid(row=8,column=0,sticky=W)

        roti=Label(foodFrame,text='Roti',font=('arial',18,'bold'),pady=8 )
        roti.grid(row=9,column=0,sticky=W)

        # PRICES

        daal_p=Label(foodFrame,text=' 50 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        daal_p.grid(row=1,column=1)

        dumaloo_p=Label(foodFrame,text=' 50 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        dumaloo_p.grid(row=2,column=1)

        thali_p=Label(foodFrame,text=' 90 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        thali_p.grid(row=3,column=1)

        purisabji_p=Label(foodFrame,text=' 60 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        purisabji_p.grid(row=4,column=1)

        pavbhaji_p=Label(foodFrame,text=' 70 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        pavbhaji_p.grid(row=5,column=1)

        paneer_p=Label(foodFrame,text=' 70 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        paneer_p.grid(row=6,column=1)

        salad_p=Label(foodFrame,text=' 30 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        salad_p.grid(row=7,column=1)

        rice_p=Label(foodFrame,text=' 50 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        rice_p.grid(row=8,column=1)

        roti_p=Label(foodFrame,text=' 10 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        roti_p.grid(row=9,column=1)


        # QUANTITIES

        textdaal=ttk.Combobox(foodFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_daal)
        textdaal.grid(row=1,column=2)

        textdumaloo=ttk.Combobox(foodFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_dumaloo)
        textdumaloo.grid(row=2,column=2,padx=30)

        textthali=ttk.Combobox(foodFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_thali)
        textthali.grid(row=3,column=2)

        textpurisabji =ttk.Combobox(foodFrame, font=('arial', 18, 'bold'), values=q, width=4,  textvariable=e_purisabji)
        textpurisabji.grid(row=4, column=2)

        textpavbhaji =ttk.Combobox(foodFrame, font=('arial', 18, 'bold'), values=q, width=4,  textvariable=e_pavbhaji)
        textpavbhaji.grid(row=5, column=2)

        textpaneer =ttk.Combobox(foodFrame, font=('arial', 18, 'bold'), values=q, width=4,  textvariable=e_paneer)
        textpaneer.grid(row=6, column=2)

        textsalad = ttk.Combtextdaal=ttk.Combobox(foodFrame, font=('arial', 18, 'bold'), values=q, width=4,  textvariable=e_salad)
        textsalad.grid(row=7, column=2)

        textrice =ttk.Combobox(foodFrame, font=('arial', 18, 'bold'), values=q, width=4,textvariable=e_rice)
        textrice.grid(row=8, column=2)

        textroti=ttk.Combobox(foodFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_roti)
        textroti.grid(row=9,column=2,padx=30)

        


        #NON VEG

        g2=Label(foodFrame,text="NON VEG",font=('arial',15,'italic'),fg='white',bg='red').grid(row=0,column=3,padx=10)

        p=Label(foodFrame,text="Price",font=('arial',15,'italic'),padx=12).grid(row=0,column=4,sticky=EW)

        quan=Label(foodFrame,text="Quantity",font=('arial',15,'italic')).grid(row=0,column=5,sticky=EW)

        
        egg=Label(foodFrame,text='Egg Curry',font=('arial',18,'bold'),pady=8 )
        egg.grid(row=1,column=3,padx=5)

        fishfry=Label(foodFrame,text='Fish Fry',font=('arial',18,'bold' ),pady=8)
        fishfry.grid(row=2,column=3)

        kebab=Label(foodFrame,text='Kebab',font=('arial',18,'bold' ),pady=8)
        kebab.grid(row=3,column=3)

        platter=Label(foodFrame,text='Platter',font=('arial',18,'bold' ),pady=8)
        platter.grid(row=4,column=3)

        biriyani=Label(foodFrame,text='Biriyani',font=('arial',18,'bold' ),pady=8)
        biriyani.grid(row=5,column=3)

        fish=Label(foodFrame,text='Fish Curry',font=('arial',18,'bold' ),pady=8)
        fish.grid(row=6,column=3)

        chicken=Label(foodFrame,text='Butter Chicken',font=('arial',18,'bold'),pady=8 )
        chicken.grid(row=7,column=3)

        mutton=Label(foodFrame,text='Mutton Curry',font=('arial',18,'bold' ),pady=8)
        mutton.grid(row=8,column=3)

        chroll=Label(foodFrame,text='Chicken Roll',font=('arial',18,'bold' ),pady=8)
        chroll.grid(row=9,column=3)

        # QUANTITIES

        textegg =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_egg)
        textegg.grid(row=1, column=5,padx=30)

        textfishfry =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_fishfry)
        textfishfry.grid(row=2, column=5)

        textkebab =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_kebab)
        textkebab.grid(row=3, column=5)

        textplatter =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_platter)
        textplatter.grid(row=4, column=5)

        textbiriyani =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_biriyani)
        textbiriyani.grid(row=5, column=5)

        textfish =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_fish)
        textfish.grid(row=6, column=5)

        textchicken =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_chicken)
        textchicken.grid(row=7, column=5)

        textmutton =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_mutton)
        textmutton.grid(row=8, column=5)

        textchroll =ttk.Combobox(foodFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_chroll)
        textchroll.grid(row=9, column=5)

        # PRICES

        egg_p=Label(foodFrame,text=' 120 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        egg_p.grid(row=1,column=4)

        fishfry_p=Label(foodFrame,text=' 120 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        fishfry_p.grid(row=2,column=4)

        kebab_p=Label(foodFrame,text=' 100 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8)
        kebab_p.grid(row=3,column=4)

        platter_p=Label(foodFrame,text=' 180 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        platter_p.grid(row=4,column=4)

        biriyani_p=Label(foodFrame,text=' 150 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        biriyani_p.grid(row=5,column=4)

        fish_p=Label(foodFrame,text=' 180 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        fish_p.grid(row=6,column=4)

        chicken_p=Label(foodFrame,text=' 200 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        chicken_p.grid(row=7,column=4)

        mutton_p=Label(foodFrame,text=' 250 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        mutton_p.grid(row=8,column=4)

        chroll_p=Label(foodFrame,text='  80  ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        chroll_p.grid(row=9,column=4)



        # FAST FOOD

        p=Label(fastFrame,text="Price",font=('arial',15,'italic'),padx=11).grid(row=0,column=1,pady=5,sticky=EW)

        quan=Label(fastFrame,text="Quantity",font=('arial',15,'italic'),padx=10).grid(row=0,column=2,sticky=EW)


        
        noodles=Label(fastFrame,text='Noodles',font=('arial',18,'bold' ),pady=8)
        noodles.grid(row=1,column=0,sticky=W,padx=10)

        dosa=Label(fastFrame,text='Dosa',font=('arial',18,'bold'),pady=8 )
        dosa.grid(row=2,column=0,sticky=W,padx=10)

        idli=Label(fastFrame,text='Idli',font=('arial',18,'bold'),pady=8)
        idli.grid(row=3,column=0,sticky=W,padx=10)

        sandwich=Label(fastFrame,text='Sandwich',font=('arial',18,'bold' ),pady=8 )
        sandwich.grid(row=4,column=0,sticky=W,padx=10)

        pasta=Label(fastFrame,text='Pasta',font=('arial',18,'bold' ),pady=8 )
        pasta.grid(row=5,column=0,sticky=W,padx=10)

        burger=Label(fastFrame,text='Burger',font=('arial',18,'bold' ),pady=8 )
        burger.grid(row=6,column=0,sticky=W,padx=10)

        cutlets=Label(fastFrame,text='Cutlets',font=('arial',18,'bold' ),pady=8)
        cutlets.grid(row=7,column=0,sticky=W,padx=10)

        samosa=Label(fastFrame,text='Samosa',font=('arial',18,'bold'),pady=8)
        samosa.grid(row=8,column=0,sticky=W,padx=10)

        kachori=Label(fastFrame,text='Kachori',font=('arial',18,'bold'),pady=8 )
        kachori.grid(row=9,column=0,sticky=W,padx=10)

        # PRICES

        noodles_p=Label(fastFrame,text=' 80 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        noodles_p.grid(row=1,column=1)
        
        dosa_p=Label(fastFrame,text=' 60 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        dosa_p.grid(row=2,column=1)
        
        idli_p=Label(fastFrame,text=' 40 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        idli_p.grid(row=3,column=1)
        
        sandwich_p=Label(fastFrame,text=' 50 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        sandwich_p.grid(row=4,column=1)
        
        pasta_p=Label(fastFrame,text=' 60 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        pasta_p.grid(row=5,column=1)
        
        burger_p=Label(fastFrame,text=' 60 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        burger_p.grid(row=6,column=1)

        cutlets_p=Label(fastFrame,text=' 80 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        cutlets_p.grid(row=7,column=1)

        samosa_p=Label(fastFrame,text=' 15 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        samosa_p.grid(row=8,column=1)

        kachori_p=Label(fastFrame,text=' 15 ',font=('arial',15,'bold'),relief=GROOVE,bd=4,pady=8 )
        kachori_p.grid(row=9,column=1)



        # QUANTITIES

        textnoodles=ttk.Combobox(fastFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_noodles)
        textnoodles.grid(row=1,column=2,padx=30)

        textdosa=ttk.Combobox(fastFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_dosa)
        textdosa.grid(row=2,column=2)

        textidli=ttk.Combobox(fastFrame,font=('arial',18,'bold'),values=q,width=4,textvariable=e_idli)
        textidli.grid(row=3,column=2)

        textsandwich =ttk.Combobox(fastFrame, font=('arial',18, 'bold'), values=q, width=4, textvariable=e_sandwich)
        textsandwich.grid(row=4, column=2)

        textpasta =ttk.Combobox(fastFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_pasta)
        textpasta.grid(row=5, column=2)

        textburger =ttk.Combobox(fastFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_burger)
        textburger.grid(row=6, column=2)

        textcutlets =ttk.Combobox(fastFrame, font=('arial',18, 'bold'), values=q, width=4,textvariable=e_cutlets)
        textcutlets.grid(row=7, column=2)

        textsamosa =ttk.Combobox(fastFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_samosa)
        textsamosa.grid(row=8, column=2)

        textkachori =ttk.Combobox(fastFrame, font=('arial',18, 'bold'), values=q, width=4,  textvariable=e_kachori)
        textkachori.grid(row=9, column=2)


        #Buttons

        buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg="#2d5e69",bd=3,padx=3, command=lambda:totalcost())
        buttonTotal.grid(row=0,column=0)
        
        buttonReceipt=Button(buttonFrame,text='Place Order',font=('arial',14,'bold'),fg='white',bg="#2d5e69",bd=3,padx=3 ,command=lambda:[messagebox.showinfo("Confirmation", "Order Placed Successfully !!!"),receipt()])
        buttonReceipt.grid(row=0,column=1)

        buttonFeedback=Button(buttonFrame,text='Feedback',font=('arial',14,'bold'),fg='white',bg="#2d5e69",bd=3,padx=3,command=lambda:[app.destroy(),feedback()])
        buttonFeedback.grid(row=0,column=2)

        buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg="#2d5e69",bd=1,padx=2,command=lambda:reset())
        buttonReset.grid(row=0,column=3)

        

        app.mainloop()
        
