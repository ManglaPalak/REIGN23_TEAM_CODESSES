from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pharmacy
import patient_and_doctor_record

conn=mysql.connector.connect(host='localhost',user='root',password='Palak@2026')
mycursor=conn.cursor()
mycursor.execute('create database XYZ_hospital')
mycursor.execute('use XYZ_hospital')
mycursor.execute('create table meddata(RefNo varchar(30),Type varchar(30),MedName varchar(30),LotNo varchar(30),IssueD varchar(30),ExpD varchar(30),Uses varchar(30),SideEf varchar(30),Precaution varchar(30),Dosage varchar(30),Price varchar(30),ProdQuan varchar(30),CompName varchar(30))')
mycursor.execute('create table patient(Name varchar(30),P_Id varchar(30),DOB varchar(30),Diagnosis varchar(30),NameTablet varchar(30),BloodP varchar(30),Medication varchar(30),P_address varchar(30),Gender varchar(30),Att_Doc varchar(30),P_phoneno varchar(30),P_medicalhistory varchar(30))')
mycursor.execute('create table doctor(Name varchar(30),D_Id varchar(30),DOB varchar(30),BloodG varchar(30),Email varchar(30),Speciality varchar(30),Department varchar(30),Qualification varchar(30),Gender varchar(30),Age varchar(30),Contact varchar(30),Address varchar(30),Cabinno varchar(30),Available_hours varchar(30))')
