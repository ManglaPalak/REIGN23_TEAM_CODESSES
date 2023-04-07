from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

win_pat = Tk()
win_pat.state('zoomed')
win_pat.config(bg='black')
############################button functionality########################
def pat_data():
    if e1.get()=='' or e2.get()=='':
        messagebox.showerror('ERROR','All fields are required')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
        mycursor=conn.cursor()
        mycursor.execute('insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(pname.get(),pid.get(),pdob.get(),diag.get(),nametab.get(),pblood.get(),medication.get(),paddress.get(),pgen.get(),attdoc.get(),pphone.get(),phistory.get()))
        conn.commit()
        pat_fetchdata()
        conn.close()
        messagebox.showinfo('Success','Record added')
def doc_data():
    if e1.get()=='' or e2.get()=='':
        messagebox.showerror('ERROR','All fields are required')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
        mycursor=conn.cursor()
        mycursor.execute('insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(dname.get(),did.get(),ddob.get(),dblood.get(),demail.get(),dspe.get(),depart.get(),dqual.get(),dgen.get(),dage.get(),dcontact.get(),dadd.get(),dcab.get(),dhours.get()))
        conn.commit()
        doc_fetchdata()
        conn.close()
        messagebox.showinfo('Success','Record added')
def pat_fetchdata():
    conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
    mycursor=conn.cursor()
    mycursor.execute('select * from patient')
    rows=mycursor.fetchall()
    if len(rows)!=0:
        pat_table.delete(* pat_table.get_children())
        for items in rows:
            pat_table.insert('',END,values=items)
        conn.commit()
    conn.close()
def doc_fetchdata():
    conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
    mycursor=conn.cursor()
    mycursor.execute('select * from doctor')
    rows=mycursor.fetchall()
    if len(rows)!=0:
        doc_table.delete(* doc_table.get_children())
        for items in rows:
            doc_table.insert('',END,values=items)
        conn.commit()
    conn.close()
def pat_get_data(event=''):
    cursor_row=pat_table.focus()
    data=pat_table.item(cursor_row)
    row=data['values']
    pname.set(row[0])
    pid.set(row[1])
    pdob.set(row[2])
    diag.set(row[3])
    nametab.set(row[4])
    pblood.set(row[5])
    medication.set(row[6])
    paddress.set(row[7])
    pgen.set(row[8])
    attdoc.set(row[9])
    pphone.set(row[10])
    phistory.set(row[11])
def doc_get_data(event=''):
    cursor_row=doc_table.focus()
    data=doc_table.item(cursor_row)
    row=data['values']
    dname.set(row[0])
    did.set(row[1])
    ddob.set(row[2])
    dblood.set(row[3])
    demail.set(row[4])
    dspe.set(row[5])
    depart.set(row[6])
    dqual.set(row[7])
    dgen.set(row[8])
    dage.set(row[9])
    dcontact.set(row[10])
    dadd.set(row[11])
    dcab.set(row[12])
    dhours.set(row[13])
def pat_pres():
    pat_txt_frme.insert(END,'Name of Patient:\t\t\t'+pname.get()+'\n')
    pat_txt_frme.insert(END,'Patient ID:\t\t\t'+pid.get()+'\n')
    pat_txt_frme.insert(END,'Gender:\t\t\t'+pgen.get()+'\n')
    pat_txt_frme.insert(END,'BloodGroup:\t\t\t'+pblood.get()+'\n')
    pat_txt_frme.insert(END,'Diagnosis:\t\t\t'+diag.get()+'\n')
    pat_txt_frme.insert(END,'Name of Tablet:\t\t\t'+nametab.get()+'\n')
    pat_txt_frme.insert(END,'Medication:\t\t\t'+medication.get()+'\n')
    pat_txt_frme.insert(END,'Attending Doctor:\t\t\t'+attdoc.get()+'\n')
    pat_txt_frme.insert(END,'Patient Medical History:\t\t\t'+phistory.get()+'\n')
    pat_txt_frme.insert(END,'Patient Phone No:\t\t\t'+pphone.get()+'\n')
def doc_info():
    doc_txt_frme.insert(END,'Name of Doctor:\t\t\t'+dname.get()+'\n')
    doc_txt_frme.insert(END,'Doctor ID:\t\t\t'+did.get()+'\n')
    doc_txt_frme.insert(END,'Gender:\t\t\t'+dgen.get()+'\n')
    doc_txt_frme.insert(END,'Email:\t\t\t'+demail.get()+'\n')
    doc_txt_frme.insert(END,'Speciality:\t\t\t'+dspe.get()+'\n')
    doc_txt_frme.insert(END,'Department:\t\t\t'+depart.get()+'\n')
    doc_txt_frme.insert(END,'Qualifications:\t\t\t'+dqual.get()+'\n')
    doc_txt_frme.insert(END,'Phone No:\t\t\t'+dcontact.get()+'\n')
    doc_txt_frme.insert(END,'Cabin No:\t\t\t'+dcab.get()+'\n')
    doc_txt_frme.insert(END,'Available Hours:\t\t\t'+dhours.get()+'\n')
def pat_delete():
    conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
    mycursor=conn.cursor()
    query=('delete from patient where P_Id=%s')
    value=(pid.get(),)
    mycursor.execute(query,value)
    conn.commit()
    conn.close()
    pat_fetchdata()
    messagebox.showinfo('DELETED','Patient record deleted')
def doc_delete():
    conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026',database='XYZ_hospital')
    mycursor=conn.cursor()
    query=('delete from doctor where D_Id=%s')
    value=(did.get(),)
    mycursor.execute(query,value)
    conn.commit()
    conn.close()
    doc_fetchdata()
    messagebox.showinfo('DELETED','Doctor record deleted')
def pat_clear():
    pname.set('')
    pid.set('')
    pdob.set('')
    diag.set('')
    nametab.set('')
    pblood.set('')
    medication.set('')
    paddress.set('')
    pgen.set('')
    attdoc.set('')
    pphone.set('')
    phistory.set('')
    pat_txt_frme.delete(1.0,END)

def doc_clear():
    dname.set('')
    did.set('')
    ddob.set('')
    dblood.set('')
    demail.set('')
    dspe.set('')
    depart.set('')
    dqual.set('')
    dgen.set('')
    dage.set('')
    dcontact.set('')
    dadd.set('')
    dcab.set('')
    dhours.set('')
    doc_txt_frme.delete(1.0,END)
def pat_exit():
    confirm=messagebox.askyesno('CONFIRMATION','Are you sure you want to exit Patient record window?')
    if confirm>0:
        win_pat.destroy()
        return
def doc_exit():
    confirm=messagebox.askyesno('CONFIRMATION','Are you sure you want to exit Doctor record window?')
    if confirm>0:
        win_doc.destroy()
        return
###################textvariable for every entry field###################
pname=StringVar()
pid=StringVar()
pdob=StringVar()
diag=StringVar()
nametab=StringVar()
pblood=StringVar()
medication=StringVar()
paddress=StringVar()
pgen=StringVar()
attdoc=StringVar()
pphone=StringVar()
phistory=StringVar()
######################################################################
#Heading
Label(win_pat,text='XYZ HOSPITAL PATIENTS RECORDS',font='impack 31 bold',bg='salmon',fg='white').pack(fill=X)
#Frame1
frame1 = Frame(win_pat,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1280,height=310)
#Label frame for patient info
lf1=LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10,bg='LightGoldenrod1')
lf1.place(x=10,y=0,width=750,height=280)
#Label for patient info
Label(lf1,text='Name of Patient',bg='LightGoldenrod1').place(x=5,y=10)
Label(lf1,text='Patient Id',bg='LightGoldenrod1').place(x=5,y=40)
Label(lf1,text='DOB',bg='LightGoldenrod1').place(x=5,y=70)
Label(lf1,text='Diagnosis',bg='LightGoldenrod1').place(x=5,y=100)
Label(lf1,text='Name of the Tablets',bg='LightGoldenrod1').place(x=5,y=130)
Label(lf1,text='Blood Pressure',bg='LightGoldenrod1').place(x=5,y=160)
Label(lf1,text='Medication',bg='LightGoldenrod1').place(x=5,y=190)
Label(lf1,text='Patient Address',bg='LightGoldenrod1').place(x=5,y=220)
Label(lf1,text='Gender',bg='LightGoldenrod1').place(x=370,y=40)
Label(lf1,text='Attending Dr.',bg='LightGoldenrod1').place(x=370,y=70)
Label(lf1,text='Patient Contact info',bg='LightGoldenrod1').place(x=370,y=100)
Label(lf1,text='Patient Medical History',bg='LightGoldenrod1').place(x=370,y=130)
# Entry Field for all labels
e1=Entry(lf1,bd=4,textvariable=pname)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=pid)
e2.place(x=130,y=40,width=200)
e3=Entry(lf1,bd=4,textvariable=pdob)
e3.place(x=130,y=70,width=200)
e4=Entry(lf1,bd=4,textvariable=diag)
e4.place(x=130,y=100,width=200)
e5=Entry(lf1,bd=4,textvariable=nametab)
e5.place(x=130,y=130,width=200)
e6=Entry(lf1,bd=4,textvariable=pblood)
e6.place(x=130,y=160,width=200)
e7=Entry(lf1,bd=4,textvariable=medication)
e7.place(x=130,y=190,width=200)
e8=Entry(lf1,bd=4,textvariable=paddress)
e8.place(x=130,y=220,width=200)
e10=Entry(lf1,bd=4,textvariable=pgen)
e10.place(x=500,y=40,width=200)
e11=Entry(lf1,bd=4,textvariable=attdoc)
e11.place(x=500,y=70,width=200)
e12=Entry(lf1,bd=4,textvariable=pphone)
e12.place(x=500,y=100,width=200)
e13=Entry(lf1,bd=4,textvariable=phistory)
e13.place(x=500,y=130,width=200)
#Label frame for prescription
lf2=LabelFrame(frame1,text='Prescription',font='ariel 12 bold',bd=10,bg='LightGoldenrod1')
lf2.place(x=770,y=0,width=470,height=280)
#Textbox for prescription
pat_txt_frme=Text(lf2,font='impack 10 bold',width=40,height=30,bg='white')
pat_txt_frme.pack(fill=BOTH)
#frame2
frame2 = Frame(win_pat,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1280,height=250)
#Button
#DELETE BUTTON
delete_btn = Button(win_pat,command=pat_delete,text='Delete',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
delete_btn.place(x=0,y=600,width=270)
#PRESCRIPTION BUTTON
pres_btn = Button(win_pat,command=pat_pres,text='Prescription',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
pres_btn.place(x=270,y=600,width=330)
#Save Prescription Data Button
pd_btn= Button(win_pat,command=pat_data,text='Save Prescription Data ',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
pd_btn.place(x=600,y=600,width=340)
#Clear Button
clr_btn= Button(win_pat,command=pat_clear,text='Clear',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
clr_btn.place(x=940,y=600,width=170)
#exit button
ex_btn= Button(win_pat,command=pat_exit,text='Exit',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
ex_btn.place(x=1110,y=600,width=170)
#Scroll Bar for prescription Data
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill=X)
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill=Y)
pat_table=ttk.Treeview(frame2,columns=('nop','pId','dob','dgn','not','bp','med','pA','gen','Adr','pCI','pMh'))
scroll_x=ttk.Scrollbar(command=pat_table.xview)
scroll_y=ttk.Scrollbar(command=pat_table.yview)
#Heading for prescription Data
pat_table.heading('nop',text='Name of Patient')
pat_table.heading('pId',text='Patient Id')
pat_table.heading('dob',text='DOB')
pat_table.heading('dgn',text='Diagnosis')
pat_table.heading('not',text='Name of the Tablets')
pat_table.heading('bp',text='Blood Pressure')
pat_table.heading('med',text='Medication')
pat_table.heading('pA',text='Patient Address')
pat_table.heading('gen',text='Gender')
pat_table.heading('Adr',text='Attending Dr')
pat_table.heading('pCI',text='Patient Contact info')
pat_table.heading('pMh',text='Patient Medical History')
pat_table['show']='headings'
pat_table.pack(fill=BOTH,expand=1)
pat_table.column('nop',width=100)
pat_table.column('pId',width=70)
pat_table.column('dob',width=80)
pat_table.column('dgn',width=100)
pat_table.column('not',width=100)
pat_table.column('bp',width=100)
pat_table.column('med',width=100)
pat_table.column('pA',width=100)
pat_table.column('gen',width=45)
pat_table.column('Adr',width=100)
pat_table.column('pCI',width=100)
pat_table.column('pMh',width=100)
pat_table.bind('<ButtonRelease-1>',pat_get_data)
pat_fetchdata()
mainloop()
########################win for doctor info#############################
win_doc = Tk()
win_doc.state('zoomed')
win_doc.config(bg='black')
#####################textvariable for every entry#######################
dname=StringVar()
did=StringVar()
ddob=StringVar()
dblood=StringVar()
demail=StringVar()
dspe=StringVar()
depart=StringVar()
dqual=StringVar()
dgen=StringVar()
dage=StringVar()
dcontact=StringVar()
dadd=StringVar()
dcab=StringVar()
dhours=StringVar()
#Heading
Label(win_doc,text='XYZ HOSPITAL DOCTORS RECORDS',font='impack 31 bold',bg='salmon',fg='white').pack(fill=X)
#Frame1
frame1 = Frame(win_doc,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1280,height=310)
#Label frame for doctor info
lf1=LabelFrame(frame1,text='Doctor Information',font='ariel 10 bold',bd=10,bg='sky blue')
lf1.place(x=10,y=0,width=750,height=280)
#Label for doctor info
Label(lf1,text='Name of Doctor',bg='sky blue').place(x=5,y=10)
Label(lf1,text='Doctor Id',bg='sky blue').place(x=5,y=40)
Label(lf1,text='DOB',bg='sky blue').place(x=5,y=70)
Label(lf1,text='BloodGroup',bg='sky blue').place(x=5,y=100)
Label(lf1,text='Email',bg='sky blue').place(x=5,y=130)
Label(lf1,text='Speciality',bg='sky blue').place(x=5,y=160)
Label(lf1,text='Department',bg='sky blue').place(x=5,y=190)
Label(lf1,text='Qualification',bg='sky blue').place(x=5,y=220)
Label(lf1,text='Gender',bg='sky blue').place(x=370,y=40)
Label(lf1,text='Age',bg='sky blue').place(x=370,y=70)
Label(lf1,text='Contact No.',bg='sky blue').place(x=370,y=100)
Label(lf1,text='Address',bg='sky blue').place(x=370,y=130)
Label(lf1,text='Cabin no.',bg='sky blue').place(x=370,y=160)
Label(lf1,text='Available Hours',bg='sky blue').place(x=370,y=190)
# Entry Field for all labels
e1=Entry(lf1,bd=4,textvariable=dname)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=did)
e2.place(x=130,y=40,width=200)
e3=Entry(lf1,bd=4,textvariable=ddob)
e3.place(x=130,y=70,width=200)
e4=Entry(lf1,bd=4,textvariable=dblood)
e4.place(x=130,y=100,width=200)
e5=Entry(lf1,bd=4,textvariable=demail)
e5.place(x=130,y=130,width=200)
e6=Entry(lf1,bd=4,textvariable=dspe)
e6.place(x=130,y=160,width=200)
e7=Entry(lf1,bd=4,textvariable=depart)
e7.place(x=130,y=190,width=200)
e8=Entry(lf1,bd=4,textvariable=dqual)
e8.place(x=130,y=220,width=200)
e10=Entry(lf1,bd=4,textvariable=dgen)
e10.place(x=500,y=40,width=200)
e11=Entry(lf1,bd=4,textvariable=dage)
e11.place(x=500,y=70,width=200)
e12=Entry(lf1,bd=4,textvariable=dcontact)
e12.place(x=500,y=100,width=200)
e13=Entry(lf1,bd=4,textvariable=dadd)
e13.place(x=500,y=130,width=200)
e14=Entry(lf1,bd=4,textvariable=dcab)
e14.place(x=500,y=160,width=200)
e15=Entry(lf1,bd=4,textvariable=dhours)
e15.place(x=500,y=190,width=200)
#Label frame for DOCTOR RECORD
lf2=LabelFrame(frame1,text='Doctor Record',font='ariel 12 bold',bd=10,bg='light blue')
lf2.place(x=770,y=0,width=470,height=280)
#Textbox for Doctor record
doc_txt_frme=Text(lf2,font='impack 10 bold',width=40,height=30,bg='white')
doc_txt_frme.pack(fill=BOTH)
#frame2
frame2 = Frame(win_doc,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1280,height=250)
#Button
#DELETE BUTTON
delete_btn = Button(win_doc,command=doc_delete,text='Delete',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
delete_btn.place(x=0,y=600,width=270)
#Doctor info BUTTON
pres_btn = Button(win_doc,command=doc_info,text='Doctor Record Display',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
pres_btn.place(x=270,y=600,width=330)
#Save Doctor Data Button
pd_btn= Button(win_doc,command=doc_data,text='Save Doctor Data ',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
pd_btn.place(x=600,y=600,width=340)
#Clear Button
clr_btn= Button(win_doc,command=doc_clear,text='Clear',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
clr_btn.place(x=940,y=600,width=170)
#exit button
ex_btn= Button(win_doc,command=doc_exit,text='Exit',font='ariel 15 bold', bg='salmon',fg='white',bd=6,cursor='hand2')
ex_btn.place(x=1110,y=600,width=170)
#Scroll Bar for Data
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill=X)
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill=Y)
doc_table=ttk.Treeview(frame2,columns=('nod','dId','dob','bg','email','spec','dept','qua','gen','age','mob','adrs','cno','avH'))
scroll_x=ttk.Scrollbar(command=doc_table.xview)
scroll_y=ttk.Scrollbar(command=doc_table.yview)
#Heading for Data
doc_table.heading('nod',text='Name of Doctor')
doc_table.heading('dId',text='Doctor Id')
doc_table.heading('dob',text='DOB')
doc_table.heading('bg',text='BloodGroup')
doc_table.heading('email',text='Email')
doc_table.heading('spec',text='Speciality')
doc_table.heading('dept',text='Department')
doc_table.heading('qua',text='Qualification')
doc_table.heading('gen',text='Gender')
doc_table.heading('age',text='Age')
doc_table.heading('mob',text='Contact No.')
doc_table.heading('adrs',text='Address')
doc_table.heading('cno',text='Cabin no.')
doc_table.heading('avH',text='Available Hours')
doc_table['show']='headings'
doc_table.pack(fill=BOTH,expand=1)
#
doc_table.column('nod',width=100)
doc_table.column('dId',width=80)
doc_table.column('dob',width=90)
doc_table.column('bg',width=80)
doc_table.column('email',width=100)
doc_table.column('spec',width=100)
doc_table.column('dept',width=100)
doc_table.column('qua',width=100)
doc_table.column('gen',width=50)
doc_table.column('age',width=50)
doc_table.column('mob',width=100)
doc_table.column('adrs',width=100)
doc_table.column('cno',width=80)
doc_table.column('avH',width=100)
doc_table.bind('<ButtonRelease-1>',doc_get_data)
doc_fetchdata()
mainloop()
