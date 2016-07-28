from falloutShelter import Dweller
from os import walk

dweller_list = []

def main():
	loadDwellers()
	clearScr()
	print("----fallout shelter database----")
	print(" 1 - new dweller                ")
	print(" 2 - dwellers list              ")
	print(" 3 - view dweller               ")
	print(" 4 - add note to dweller        ")
	print(" 5 - add title to dweller       ")
	print(" 6 - exit                       ")
	print("--------------------------------")
	inputt = raw_input("-> ")
	if(inputt == '1'):
		new_dweller()
	elif(inputt == '2'):
		list_dweller()
	elif(inputt == '3'):
		view_dweller()
	elif(inputt == '4'):
		note_dweller()
	elif(inputt == '5'):
		title_dweller()
	elif(inputt == '6'):
		return 0
	else:
		print("    exiting...")
		return -1	
#menu entries	
# 1 - new dweller
def new_dweller():
	clearScr()
	print("----fallout shelter database----")
	print("----: new dweller :-------------")
	
	name = raw_input("name: ")
	father = raw_input("father: ")
	mother = raw_input("mother: ")
	
	filename = name.split()
	filename = ''.join(filename)
	filename += ".txt"
	filename = "dwellers/"+filename	

	filetext = name+"%"+father+"%"+mother	
		
	with open(filename,'w') as file:
		file.write(filetext)
	clearScr()
	print("----fallout shelter database----")
	print("----: new dweller :-------------")
	loadDwellers()
	print("       saved        ")
	print("1- menu | 2- exit ")
	inputt = raw_input("-> ")
	if(inputt == '1'):
		main()
	elif(inputt == '2'):
		return 0

# 2 - dwellers list
def list_dweller():
	clearScr()
	print("----fallout shelter database----")
	print("----: dweller list :-------------")	
	for i in range(len(dweller_list)):
		nm = dweller_list[i].name		
		print("  "+nm)
	print("---------------------------------")
	print("1- menu | 2- exit ")
	inputt = raw_input("-> ")
	if(inputt == '1'):
		main()
	elif(inputt == '2'):
		return 0	

# 3 - view dweller
def view_dweller():
	clearScr()
	print("----fallout shelter database----")
	print("----: view dweller :------------")	
	inp = raw_input("dweller name: ")
	valid = False
	choosen_index = 0
	for i in range(len(dweller_list)):
		if(inp == dweller_list[i].name):
			valid = True
			choosen_index = i
	if(valid):
		clearScr()
		print("----fallout shelter database----")
		print("----: view dweller :------------")	
		print("name: "+dweller_list[choosen_index].name)
		print("father: "+dweller_list[choosen_index].father)
		print("mother: "+dweller_list[choosen_index].mother)

		print("---------------------------------")
		print("1- menu | 2- exit ")
		inputt = raw_input("-> ")
		if(inputt == '1'):
			main()
		elif(inputt == '2'):
			return 0	
	else:
		a = raw_input("name not found")
		main()		

# 4 - add note to dweller
def note_dweller():
	clearScr()
	print("----fallout shelter database----")
	print("----: add note :-------------")
		
# 5 - add title to dweller	
def title_dweller():
	clearScr()
	print("----fallout shelter database----")
	print("----: add title :-------------")
	inp = raw_input("dweller name: ")
	valid = False
	choosen_index = 0
	for i in range(len(dweller_list)):
		if(inp == dweller_list[i].name):
			valid = True
			choosen_index = i
	if(valid):
		clearScr()
		print("----fallout shelter database----")
		print("----: add title :------------")
		titl = raw_input("title: ")
		#add title to file procedure	
		main()
	else:
		a = raw_input("name not found")
		main()	
	
#end of menu entries
def clearScr():
	for i in range(60):
		print(" ")

def loadDwellers():
	global dweller_list
	dweller_list = []	

	path, dirs, files = walk("dwellers").next()	
	dw_count = len(files)
	
	for index in range(dw_count):
		filetxt = open(path+"/"+files[index]).read()
		name = filetxt.split('\n')[0].split('%')[0]
		father = filetxt.split('\n')[0].split('%')[1]
		mother = filetxt.split('\n')[0].split('%')[2]		
		dweller_list.append(Dweller(name,father,mother))
	
main()
clearScr()
