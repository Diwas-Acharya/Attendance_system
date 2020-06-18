from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import sqlite3
import datetime
import pandas as pd
import os

def Search_through_id(idss):
	conn = sqlite3.connect( os.path.join(os.getcwd(),"attendance\\data"))
	cur = conn.cursor()
	data = cur.execute('SELECT * FROM candidate WHERE id = ?',(idss,))
	info = data.fetchall()
	return info

def sheet_update(*args):
	conn = sqlite3.connect( os.path.join(os.getcwd(),"attendance\\data"))
	cur = conn.cursor()
	info = cur.execute('SELECT * FROM candidate')
	data = info.fetchall()
	ids , names = [] , []
	for x in data:
		ids.append(x[0])
		names.append(x[1])
	date = str(datetime.datetime.now())[:10]
	# dataframe = pd.DataFrame({"id":ids,'name':names , date : "Absent"})

	dataframe = pd.read_excel( os.path.join(os.getcwd(),"attendance\\record_list.xlsx"), sheet_name = "candidate_attendence" , index_col = 0)

	insert_id = (set(ids)-set(dataframe['id']))
	new_data = []
	for x in insert_id:
		insert_info = Search_through_id(x)
		new_data.append(insert_info)
	if len(insert_id) > 0 and len(args) > 0:
		modi_dataframe = dataframe.append({'id':new_data[0][0][0] , 'name':new_data[0][0][1]} , ignore_index = True)
		modi_dataframe.fillna(value = "Absent" , inplace = True)
	
	if str(dataframe.columns[-1]) != date:
		dataframe[date] = dataframe.apply(lambda x : "Absent" , axis = 1)
	if args[0]:
		dataframe.at[(args[0]-1),date] = "PRESENT"
	try:
		modi_dataframe.to_excel(  os.path.join(os.getcwd(),"attendance\\record_list.xlsx") ,sheet_name = "candidate_attendence" )
	except:
		dataframe.to_excel( os.path.join(os.getcwd(),"attendance\\record_list.xlsx") ,sheet_name = "candidate_attendence" )



# Create your views here.
def home(request):
	return render(request,'index.html')


def ser_reg(request):
	if request.method == "POST":
		msg = ""
		list_msg = []
		r_name = request.POST["r_name"]
		s_name = request.POST["s_name"]
		if r_name == "" and s_name == "":
			msg = "Please Enter Name"
			return render(request,"index.html",{"msg":msg})
		if r_name != "":
			conn = sqlite3.connect(os.path.join(os.getcwd(),"attendance\\data"))
			cur = conn.cursor()
			cur.execute('INSERT INTO candidate (Name) VALUES (?)',(r_name,))
			data = cur.execute("SELECT * from candidate")
			info = data.fetchall()
			ids = info[-1][0] 
			conn.commit()
			sheet_update(False , 'pass')
			found = False
			msg =  f'Added Sucessfully !! your Name is : {r_name} and id is : {ids}'
		else:
			conn = sqlite3.connect(os.path.join(os.getcwd(),"attendance\\data"))
			cur = conn.cursor()
			data = cur.execute('SELECT * FROM candidate where name = ?',(s_name,))
			info = data.fetchall()

			if len(info) > 0:
				list_msg = [x for x in info]
				found = True
			else:
				found = False
				list_msg = ["Not found ! Try Again"]

	return render(request,"index.html",{"msg":msg , "list_msg":list_msg , 'found':found})
	
def finder(request):
	if request.method == "POST":
		id = request.POST['id']
		name = request.POST['name']
		conn = sqlite3.connect(os.path.join(os.getcwd(),"attendance\\data"))
		cur = conn.cursor()
		data = cur.execute('SELECT * FROM candidate where id = ? and name = ?',(int(id),name))
		info = data.fetchall()
		if len(info) != 0:
			msg = "Enter details found in Database"
			button = True 
		else:
			msg = "Not found ! Try Again"
			button = False
	return render(request,"index.html",{"msg":msg , "name" : name , "id" : id , "button":button})

def make_present(request,myid):
	sheet_update(myid , 'pass')
	return render(request,'index.html',{'msg':"Sucessfully Marked as Present for id : {} ".format(myid)})