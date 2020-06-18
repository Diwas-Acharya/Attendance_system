from attendance import *
from tkinter import *
import pandas as pd
import time
import datetime
from openpyxl import worksheet , Workbook

#Data manupulation in Excel sheet


def excel_update(*args):
	data = Show_all_data()
	ids , names = [] , []
	for x in data:
		ids.append(x[0])
		names.append(x[1])
	date = str(datetime.datetime.now())[:10]
	# dataframe = pd.DataFrame({"id":ids,'name':names , date : "Absent"})

	dataframe = pd.read_excel("record_list.xlsx" , sheet_name = "candidate_attendence" , index_col = 0)

	insert_id = (set(ids)-set(dataframe['id']))
	new_data = []
	for x in insert_id:
		insert_info = Search_by_id(x)
		new_data.append(insert_info)
	if len(insert_id) > 0 and len(args) > 0:
		modi_dataframe = dataframe.append({'id':new_data[0][0][0] , 'name':new_data[0][0][1]} , ignore_index = True)
		modi_dataframe.fillna(value = "Absent" , inplace = True)
	
	if str(dataframe.columns[-1]) != date:
		dataframe[date] = dataframe.apply(lambda x : "Absent" , axis = 1)
	if args[0]:
		dataframe.at[(args[0]-1),date] = "PRESENT"
	try:
		modi_dataframe.to_excel( "record_list.xlsx" ,sheet_name = "candidate_attendence" )
	except:
		dataframe.to_excel( "record_list.xlsx" ,sheet_name = "candidate_attendence" )

# Main gui

win = Tk()
win.title("Attendance")
win.geometry("500x400")

ids = StringVar()
name = StringVar()
getid = StringVar()
getname = StringVar()
setdata = StringVar()
search_value = StringVar()

def add_entry():
	names = getname.get()
	insert_once()
	data = Show_all_data()
	ids = data[-1][0] +1
	try:
		if names !="":
			Insert(names)
			string = f'Added Sucessfully !! your Name is : {names} and id is : {ids}'
			excel_update(False , 'pass')
			# but["state"] = DISABLED
			
			setdata.set(string)
		else:
			setdata.set("Please Enter Name")
			# but["state"] = DISABLED
	except:
			setdata.set("Problem occured")
			# but["state"] = DISABLED


def register():

	Label(win , text = "").grid(row = 10 , column = 2)
	Label(win , text = "Register by Name" , font = (20) ).grid(row = 11 , column = 2)
	Entry(win , textvariable = getname).grid(row = 12 , column = 2)

	Button(win , text = " Done " , command = add_entry).grid(row = 13 , column = 2)
	butReg["state"] = DISABLED
	butSear["state"] = NORMAL

def present(idss , *args):
	excel_update(idss , 'pass')

def fetch():
	global but
	names = name.get()
	idss = ids.get()
	
	if names =="" and idss == "":
		setdata.set("Please Enter ID and Name")
		but["state"] = DISABLED
		return
	if names !="" and idss == "":
		setdata.set("Please enter ID")
		but["state"] = DISABLED
		return 
	if names == "" and idss !="":
		setdata.set("Please Enter Name")
		but["state"] = DISABLED
		return 
	else:
		data = Search(int(idss),names)

	try:
		if data[0][0] == int(idss) and data[0][1] == names:
			setdata.set("Enter record Found in Database")
			but = Button(win , text = "Mark Present" , command = present(int(idss)))
			but.grid(row = 16 , column = 2)
	except:
		setdata.set("Not found")
		Label(win , text = "Try again").grid(row = 16 , column = 2)

def search():
	Label(win , text = "").grid(row = 10 , column = 2)
	Label(win , text = " Search by Name " , font = (20) ).grid(row = 11 , column = 2)
	Entry(win , textvariable = search_value).grid(row = 12 , column = 2)

	Button(win , text = "Search" , command = get_search).grid(row = 13 , column = 2)
	butSear["state"] = DISABLED
	butReg['state'] =NORMAL

def get_search():
	value = search_value.get()
	if value == "":
		setdata.set("Please Enter Name")
		return
	data = Search_by_name(value)
	string = ""
	if len(data) !=0:
		for x in data:
			string = string + "ID : "+ str(x[0]) + " , Name : "+x[1]+"\n"
		setdata.set(string)
	else:
		setdata.set("Not Found")


label1 = Label(win , text= "DAILY ATTENDANCE SYSTEM" , justify = 'center' , font = ('tahoma',25))
label1.grid(row = 1 , columnspan = 5)


label1 = Label(win , text= "" , justify = 'center' , font = ('tahoma'))
label1.grid(row = 2 , columnspan = 5)


label2 = Label(win , text = "ID     :")
label2.grid(row = 3 , column = 1)

Entry(win , textvariable= ids).grid(row = 3 , column = 2)

label3 = Label(win , text = "Name     :")
label3.grid(row = 4 , column = 1)
Entry(win , textvariable = name).grid(row = 4 , column = 2)
Button(win , text = "fetch" , command = fetch).grid(row = 5 , column = 2)
Label(win , text = " " , font = (30)).grid(row = 14 , column = 2)
Label(win , textvariable = setdata , font = (30)).grid(row = 15 , column = 2)


butReg = Button(win , text = "Register" , command = register)
butReg.grid(row = 3 , column = 3)
butSear = Button(win , text = "Search" , command = search)
butSear.grid(row = 4 , column = 3)


win.mainloop()
