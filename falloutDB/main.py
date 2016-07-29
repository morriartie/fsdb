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
	print(" 6 - add occupation to dweller  ")
	print(" 7 - exit                       ")
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
		occupation_dweller()
	elif(inputt == '7'):
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
	filename = "dwellers/"+filename+".txt"	

	filetext = name+"%"+father+"%"+mother	
	filetext += '\n'
	filetext += '\n'		
	
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

		print("Titles("+str(len(dweller_list[choosen_index].title_list))+"): ")
		for i in range(len(dweller_list[choosen_index].title_list)):
			print("    "+dweller_list[choosen_index].title_list[i])

		print("Occupation("+str(len(dweller_list[choosen_index].occupation_list))+"): ")
		for i in range(len(dweller_list[choosen_index].occupation_list)):
			print("    "+dweller_list[choosen_index].occupation_list[i])
		
		print("Notes("+str(len(dweller_list[choosen_index].note_list))+"): ")
		for i in range(len(dweller_list[choosen_index].note_list)):
			print("    "+dweller_list[choosen_index].note_list[i])


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
		print("----: add note :------------")
		notte = raw_input("note: ")
		dweller_list[choosen_index].note_list.append(notte)
		clearScr()
		print("----fallout shelter database----")
		print("----: add note :------------")
		nn = raw_input("	saved		")
		saveDwellers()		
		main()
	else:
		a = raw_input("name not found")
		main()	
		
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
		dweller_list[choosen_index].title_list.append(titl)
		clearScr()
		print("----fallout shelter database----")
		print("----: add title :------------")
		nn = raw_input("	saved		")
		saveDwellers()		
		main()
	else:
		a = raw_input("name not found")
		main()	

# 6 - add occupation to dweller
def occupation_dweller():
	clearScr()
	print("----fallout shelter database----")
	print("----: add occupation :-------------")
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
		print("----: add occupation :------------")
		titl = raw_input("occupation: ")
		dweller_list[choosen_index].occupation_list.append(titl)
		clearScr()
		print("----fallout shelter database----")
		print("----: add occupation :------------")
		nn = raw_input("	saved		")
		saveDwellers()		
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

		t_list = filetxt.split('\n')[1].split(';')				
		if(len(t_list)>0):		
			del t_list[len(t_list)-1]

		o_list = filetxt.split('\n')[2].split(';')
		if(len(o_list)>0):
			del o_list[len(o_list)-1]
		
		n_list = filetxt.split('\n')[3].split(';')
		if(len(n_list)>0):
			del n_list[len(n_list)-1]

		dweller_list.append(Dweller(name,father,mother))
			
		for t in range(len(t_list)):
			dweller_list[len(dweller_list)-1].title_list.append(t_list[t])	

		for o in range(len(o_list)):
			dweller_list[len(dweller_list)-1].occupation_list.append(o_list[o])

		for n in range(len(n_list)):
			dweller_list[len(dweller_list)-1].note_list.append(n_list[n])		
		
def saveDwellers():
	global dweller_list
	dw_count = len(dweller_list)
	for i in range(dw_count):
		fname = dweller_list[i].name
		fname = fname.split()
		fname = ''.join(fname)
		fname = "dwellers/"+fname+".txt"

		filetext = dweller_list[i].name+"%"+dweller_list[i].father+"%"+dweller_list[i].mother
		filetext += '\n'

		for title_i in range(len(dweller_list[i].title_list)):
			filetext += dweller_list[i].title_list[title_i]+";"

		filetext += '\n'		
		for occ_i in range(len(dweller_list[i].occupation_list)):
			filetext += dweller_list[i].occupation_list[occ_i]+";"				
		
		filetext += '\n'
		for note_i in range(len(dweller_list[i].note_list)):
			filetext += dweller_list[i].note_list[note_i]+";"		
					
		with open(fname,'w') as file:
			file.write(filetext)
			
	
main()
clearScr()
