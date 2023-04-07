from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

#############button function###################
def add_data():
    if nme.get()=='' or lot.get()=='':
        messagebox.showerror('ERROR','All fields are required')
    else:
        conn=mysql.connector.connect(host='localhost',username='root',password='Palak@2026',database='XYZ_hospital')
        my_cursor=conn.cursor()
        my_cursor.execute('insert into meddata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ref.get(),typ.get(),nme.get(),lot.get(),issue.get(),exp.get(),use.get(),side.get(),prec.get(),dos.get(),pri.get(),proqu.get(),compn.get()))
        conn.commit()
        fetchdata()
        conn.close()
        messagebox.showinfo('success','Record has been inserted')
def fetchdata():
    conn=mysql.connector.connect(host='localhost',username='root',password='Palak@2026',database='XYZ_hospital')
    my_cursor=conn.cursor()
    my_cursor.execute('select * from meddata')
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        main_table.delete(* main_table.get_children())
        for items in rows:
            main_table.insert('',END,values=items)
        conn.commit()
    conn.close()
    
def get_data(event=''):
    cursor_row=main_table.focus()
    data=main_table.item(cursor_row)
    global a
    a=data['values']
    ref.set(a[0])
    typ.set(a[1])
    nme.set(a[2])
    lot.set(a[3])
    issue.set(a[4])
    exp.set(a[5])
    use.set(a[6])
    side.set(a[7])
    prec.set(a[8])
    dos.set(a[9])
    pri.set(a[10])
    proqu.set(a[11])
    compn.set(a[12])
def display_info():
    txt_frame.insert(END,'Name of medicine:\t\t\t'+nme.get()+'\n')
    txt_frame.insert(END,'Type of medicine:\t\t\t'+typ.get()+'\n')
    txt_frame.insert(END,'Issue Date:\t\t\t'+issue.get()+'\n')
    txt_frame.insert(END,'Exp Date:\t\t\t'+exp.get()+'\n')
    txt_frame.insert(END,'Uses:\t\t\t'+use.get()+'\n')
    txt_frame.insert(END,'Side Effects:\t\t\t'+side.get()+'\n')
    txt_frame.insert(END,'Precaution:\t\t\t'+prec.get()+'\n')
    txt_frame.insert(END,'Dosage:\t\t\t'+dos.get()+'\n')
    txt_frame.insert(END,'Price:\t\t\t'+pri.get()+'\n')
    txt_frame.insert(END,'Name of Company:\t\t\t'+compn.get()+'\n')
def med_reset():
    ref.set('')
    typ.set('')
    nme.set('')
    lot.set('')
    issue.set('')
    exp.set('')
    use.set('')
    side.set('')
    prec.set('')
    dos.set('')
    pri.set('')
    proqu.set('')
    compn.set('')
    txt_frame.delete(1.0,END)
def med_exit():
    confirm=messagebox.askyesno('CONFIRMATION','Are you sure you want to exit Pharmacy window?')
    if confirm>0:
        win.destroy()
        return
def med_delete():
    conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
    mycursor=conn.cursor()
    query=('delete from meddata where RefNo=%s')
    value=(ref.get(),)
    mycursor.execute(query,value)
    conn.commit()
    fetchdata()
    conn.close()
    messagebox.showinfo('DELETED','Medicine record deleted')
###############################################
def pharmacy():
    global win
    global main_table
    global txt_frame
    global ref
    global typ
    global nme
    global lot
    global issue
    global exp
    global use
    global side
    global prec
    global dos
    global pri
    global proqu
    global compn
    win=Tk()
    win.state('zoomed')
    win.config(bg='white')
    title=Label(win,text='XYZ HOSPITAL PHARMACY',bd=5,font='ariel 31 bold',relief=RIDGE,bg='salmon',fg='white')
    title.pack(fill=X)
    #textvariable for every entry field
    ref=StringVar()
    typ=StringVar()
    nme=StringVar()
    lot=StringVar()
    issue=StringVar()
    exp=StringVar()
    use=StringVar()
    side=StringVar()
    prec=StringVar()
    dos=StringVar()
    pri=StringVar()
    proqu=StringVar()
    compn=StringVar()

    #frame1
    frame1=Frame(win,bd=10,relief=RIDGE)
    frame1.place(x=0,y=54,width=1280,height=310)
    #label frame for medicine info input
    lf1=LabelFrame(frame1,text='Medicine Information',font='ariel 10 bold',bd=10,bg='pink',fg='black')
    lf1.place(x=10,y=0,width=750,height=280)
    #labels for medicine inofrmation
    labref=Label(lf1,text='Reference No.',bg='pink',fg='black')
    labref.place(x=10,y=5)
    txtmed=Entry(lf1,bd=3,textvariable=ref)
    txtmed.place(x=100,y=5,width=200)

    labtot=Label(lf1,text='Type of tablet',bg='pink',fg='black')
    labtot.place(x=10,y=35)
    txttot=Entry(lf1,bd=3,textvariable=typ)
    txttot.place(x=100,y=35,width=200)

    labmn=Label(lf1,text='Medicine Name',bg='pink',fg='black')
    labmn.place(x=10,y=65)
    medn=Entry(lf1,bd=3,textvariable=nme)
    medn.place(x=100,y=65,width=200)

    labln=Label(lf1,text='Lot No.',bg='pink',fg='black')
    labln.place(x=10,y=95)
    txtln=Entry(lf1,bd=3,textvariable=lot)
    txtln.place(x=100,y=95,width=200)

    labissd=Label(lf1,text='Issue Date',bg='pink',fg='black')
    labissd.place(x=10,y=125)
    txtissd=Entry(lf1,bd=3,textvariable=issue)
    txtissd.place(x=100,y=125,width=200)

    labexpd=Label(lf1,text='Exp.Date',bg='pink',fg='black')
    labexpd.place(x=10,y=155)
    txtexpd=Entry(lf1,bd=3,textvariable=exp)
    txtexpd.place(x=100,y=155,width=200)

    labuse=Label(lf1,text='Uses',bg='pink',fg='black')
    labuse.place(x=10,y=185)
    txtuse=Entry(lf1,bd=3,textvariable=use)
    txtuse.place(x=100,y=185,width=200)

    labse=Label(lf1,text='Side effect',bg='pink',fg='black')
    labse.place(x=10,y=215)
    txtse=Entry(lf1,bd=3,textvariable=side)
    txtse.place(x=100,y=215,width=200)

    labprecw=Label(lf1,text='Precation Warning',bg='pink',fg='black')
    labprecw.place(x=325,y=5)
    txtprecw=Entry(lf1,bd=3,textvariable=prec)
    txtprecw.place(x=440,y=5,width=200)

    labdos=Label(lf1,text='Dosage',bg='pink',fg='black')
    labdos.place(x=325,y=35)
    txtdos=Entry(lf1,bd=3,textvariable=dos)
    txtdos.place(x=440,y=35,width=200)

    labprice=Label(lf1,text='Price',bg='pink',fg='black')
    labprice.place(x=325,y=65)
    txtprice=Entry(lf1,bd=3,textvariable=pri)
    txtprice.place(x=440,y=65,width=200)

    labprodquan=Label(lf1,text='Product Quantity',bg='pink',fg='black')
    labprodquan.place(x=325,y=95)
    txtprodquan=Entry(lf1,bd=3,textvariable=proqu)
    txtprodquan.place(x=440,y=95,width=200)

    labcompn=Label(lf1,text='Company Name',bg='pink',fg='black')
    labcompn.place(x=325,y=125)
    txtcompn=Entry(lf1,bd=3,textvariable=compn)
    txtcompn.place(x=440,y=125,width=200)

    #label frame for medicine add department
    lf2=LabelFrame(frame1,text='MEDICINE ADD DEPARTMENT',font='ariel 10 bold',bd=10,bg='pink',fg='black')
    lf2.place(x=770,y=0,width=490,height=280)
    #textbox for prescription
    txt_frame=Text(lf2,font='ariel 10 bold',width=40,height=30,bg='white')
    txt_frame.pack(fill=BOTH)

    #frame details
    framedetails=Frame(win,bd=4,bg='pink',relief=RIDGE)
    framedetails.place(x=0,y=415,width=1280,height=230)
    #main table
    table_frame=Frame(win,bd=10,relief=RIDGE)
    table_frame.place(x=10,y=425,width=1260,height=210)
    sc_x1=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    sc_x1.pack(side=BOTTOM,fill=X)
    sc_y1=ttk.Scrollbar(table_frame,orient=VERTICAL)
    sc_y1.pack(side=RIGHT,fill=Y)

    main_table=ttk.Treeview(table_frame,column=('ref','type','medname','lotno','issdate','expdate','uses','sideef','warning','dosage','price','prodquan','compname'),xscrollcommand=sc_x1.set,yscrollcommand=sc_y1.set)
    sc_x1.config(command=main_table.xview)
    sc_y1.config(command=main_table.yview)
    main_table['show']='headings'
    main_table.heading('ref',text='Reference No')
    main_table.heading('type',text='Type of Medicine')
    main_table.heading('medname',text='Medicine Name')
    main_table.heading('lotno',text='Lot No')
    main_table.heading('issdate',text='Issue Date')
    main_table.heading('expdate',text='Exp Date')
    main_table.heading('uses',text='Uses')
    main_table.heading('sideef',text='Side Effect')
    main_table.heading('warning',text='Precaution')
    main_table.heading('dosage',text='Dosage')
    main_table.heading('price',text='Price')
    main_table.heading('prodquan',text='Product Quantity')
    main_table.heading('compname',text='Company Name')
    main_table.pack(fill=BOTH,expand=1)
    main_table.column('ref',width=80)
    main_table.column('type',width=100)
    main_table.column('medname',width=100)
    main_table.column('lotno',width=80)
    main_table.column('issdate',width=100)
    main_table.column('expdate',width=100)
    main_table.column('uses',width=100)
    main_table.column('sideef',width=100)
    main_table.column('warning',width=100)
    main_table.column('dosage',width=80)
    main_table.column('price',width=80)
    main_table.column('prodquan',width=100)
    main_table.column('compname',width=100)

    #frame2 with the buttons
    frame2=Frame(win,bd=10,relief=RIDGE)
    frame2.place(x=0,y=360,width=1280,height=55)
    #main buttons
    bADD=Button(frame2,text='MEDICINE ADD',command=add_data,font='ariel 12 bold',bg='white',fg='light salmon',width=25)
    bADD.grid(row=0,column=0)
    bDEL=Button(frame2,text='DELETE',font='ariel 12 bold',bg='red',fg='light salmon',width=25,command=med_delete)
    bDEL.grid(row=0,column=1)
    bRESMED=Button(frame2,command=med_reset,text='RESET',font='ariel 12 bold',bg='white',fg='light salmon',width=25)
    bRESMED.grid(row=0,column=2)
    bSHOW=Button(frame2,command=display_info,text='SHOW MED DATA',font='ariel 12 bold',bg='white',fg='light salmon',width=25)
    bSHOW.grid(row=0,column=3)
    bEXIT=Button(frame2,text='EXIT',font='ariel 12 bold',bg='red',fg='light salmon',width=20,command=med_exit)
    bEXIT.grid(row=0,column=4)

    main_table.bind('<ButtonRelease-1>',get_data)
    fetchdata()
    win.mainloop()
pharmacy()
