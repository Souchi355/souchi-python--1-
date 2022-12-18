
#--------------------------class teachers--------------------------
class teacher:
    def __init__(self,subject,name,age,email=None,phoneN=None,adress=None):
        self.subject=id
        self.name=name
        self.age=age
        self.email=email
        self.phoneN=phoneN
        self.adress=adress
        
    def add_email(self,email):
        self.email=email
    def add_phoneN(self,pn):
        self.phoneN=pn
    def add_adress(self,ad):
        self.adress=ad
        
#--------------------------class students--------------------------
class student:
    def __init__(self,id,name,age,teachers,email=None,phoneN=None,adress=None):
        self.id=id
        self.name=name
        self.age=age
        self.email=email
        self.phoneN=phoneN
        self.adress=adress
        self.teachers=teachers
        
    def add_email(self,email):
        self.email=email
        
    def add_phoneN(self,pn):
        self.phoneN=pn
        
    def add_adress(self,ad):
        self.adress=ad
        
    def show_teachers(self):
        if type(self.teachers)== tuple:
            t=""
            for i in range(len(self.teachers)):
                t+=self.teachers[i].name +" "
            return t
        else:
            return self.teachers.name

#--------------------------teachers list-----------------------------
t1=teacher("math","adnan",40)
t2=teacher("sti","ahmed",41)

#--------------------------students list-----------------------------
s1=student("001","rayen",17,(t1,t2))
s1.add_email("rayenbenyoussef355@gmail.com")
s1.add_phoneN(93071355)

#-------------------------------show---------------------------------
print(f"student id: {s1.id} \nstudent name: {s1.name} \nstudent age: {s1.age} \nstudent email: {s1.email}\nstudent phone number: {s1.phoneN} \nstudent adress: {s1.adress} \nstudent teachers: {s1.show_teachers()} ")