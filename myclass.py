class MyClass:
	def __init__(self,surname,city,profession):
                self.surname = surname
                self.city = city
                self.profession = profession
	def meth_1(self):
                print("Surname: ",self.surname)
                print("City: ", self.city,)
                print("Profession", self.profession)
                print('------------------')

	def meth_2(self):
		self.surname = "Yessenbayev"
		self.city = "Astana"
		self.profession = "teacher"

