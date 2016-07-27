class Dweller():
	def __init__(self, name, father, mother):
		self.name = name
		self.father = father
		self.mother = mother
		self.occupation_list = []
		self.title_list = []
		self.note_list = []

	#@staticmethod
	def add_name(self, nam):
		self.name = nam

	def add_father(self, fat):
		self.father = fat

	def add_mother(self, mot):
		self.mother = mot

	def add_occupation(self, ocp):
		self.occupation_list.append(ocp)

	def add_title(self, tit):
		self.title_list.append(tit)

	def add_note(self, nots):
		self.note_list.append(nots)

	def about(self):
		print("-------------------")
		print("Name: "+self.name)
		print("Parents: "+self.father+" and "+self.mother)
		print("Occupation: ")
		for i in range(len(self.occupation_list)):
			print("	"+self.occupation_list[i])
		print("Title: ")
		for j in range(len(self.title_list)):
			print("	"+self.title_list[j])
		print("Note: ")
		for k in range(len(self.note_list)):
			print("	"+self.note_list[k])
		print("-------------------")

