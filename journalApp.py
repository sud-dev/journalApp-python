import datetime
import os
import getpass
import base64
from datetime import date

author = "" #Setting up a global variable that we can use throughout 
def home_page():
	print("Welcome To Personal Journal Application")
	print("1: SignUp")
	print("2: Login")
	print("3: Exit")
	option = input("Your choice:  ")
	print("-----\n-----")
	if option == "1" or option == 1:
		create_user()
	elif option == "2" or option == 2:
		login_user()
	else:
		print("Thanks! See you later")
		return


def create_user():
	name = input("Username:   ")
	pswd = getpass.getpass('Password: ')
	usr=name.encode("utf-8")
	pwd=pswd.encode("utf-8")
	file = open("UserDetails.txt", "a")
	file.close()
	if os.stat("UserDetails.txt").st_size != 0:
		if file_len("UserDetails.txt") <=9:
			f= open("UserDetails.txt","a+")
			f.write(str(base64.b64encode(usr))+'||'+str(base64.b64encode(pwd)))
			f.write("\n")
			f.close()
			authenticate(name,pswd)
		else:
			print("SignUp'ed user count is already 10(user count limit exceeded)")
	else:
			f= open("UserDetails.txt","a+")
			f.write(str(base64.b64encode(usr))+'||'+str(base64.b64encode(pwd)))
			f.write("\n")
			f.close()
			authenticate(name,pswd)
	
def file_len(fname):
    with open(fname,"rb+") as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
def login_user():	
	while True:
		name = input("Username:   ")
		if not len(name) > 0:
			print("Username can't be blank")
		else:
			break
	while True:
		pswd = getpass.getpass('Password: ')
		if not len(pswd) > 0:
			print("Password can't be blank")
		else:
			break
	authenticate(name,pswd)
	
def authenticate(name,pswd):
	usr=name.encode("utf-8")
	pwd=pswd.encode("utf-8")
	flag=0
	check=str(base64.b64encode(usr))+'||'+str(base64.b64encode(pwd))
	fread=open("UserDetails.txt","r+")
	for line in fread:
		if check==line.strip('\r\n'):
			controls(name)
			flag=1
			break
	if flag==0 :
		print("Username/Credentials invalid")
		print("Please login/signup")
		home_page()
		
def create_entries(name):	
	content = input("Enter your today's entry to journal:  ")
	c=content.encode("utf-8")
	filename = name.replace(" ","") + ".txt"
	entry = open(filename, "a")
	t =datetime.datetime.now()
	if os.stat(filename).st_size != 0:
		if file_len(filename) !=50:
			entry.write(str(t.strftime("%b %d %Y %H:%M%p")) + " - ")
			entry.write(str(base64.b64encode(c)) + "\n")	
		else:
			with open(filename) as f:
				lines = f.readlines()
			lineno=file_len(filename)%50
			lines[lineno] = str(t.strftime("%b %d %Y %H:%M%p")) + " - "+str(base64.b64encode(c))+"\n"
			with open(filename, "w") as f:
				f.writelines(lines)	
	else:
		f= open(filename,"w")
		f.write(str(t.strftime("%b %d %Y %H:%M%p")) + " - ")
		f.write(str(base64.b64encode(c)) + "\n")
		f.close()	
					
	entry.close()
    
		
		
def list_entries(name):
	filename = name.replace(" ","") + ".txt"
	# length=0
	# with open(filename) as f:
		# length=length+1
		# lines = f.readlines()
		# print(lines)
	# print(length)
	if os.path.isfile(filename)== True:
		f = open(filename, "r")
		for aline in f:
			values = aline.split("-")
			val=str(base64.b64decode(aline[23:len(aline)]))
			print(values[0]+"- "+val[2:len(val)-1])
		f.close()
			# print(val[2:len(val)-1])
	else:
		print("You haven't logged anything yet in journal Please log entries first in journal")
		create_entries(name)
		list_entries(name)
	
	
			
def controls(name):
	print("What would you like to do?: ")
	print("1: List Previous Entries")
	print("2: Create an entry")
	option = input("Your choice:  ")
	print("-----\n-----")
	
	if option == "1" or option == 1:
		list_entries(name)
	elif option == "2" or option == 2:
		create_entries(name)
	else:
		print("Please answer based on your choices\n")
		controls(name)
	
	choice = input("Do you want to continue? (y/n)")
	if choice == "y" or choice == "Y":
		controls(name)
	else:
		print("Thanks!")		
	


home_page()
