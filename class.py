class student:
    def __init__(self,id,name,age,email=None,phoneN=None,adress=None):
        self.id=id
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
        
s1=student("001","rayen",17)
s1.add_email("rayenbenyoussef355@gmail.com")
print(f"student id: {s1.id} ,student name: {s1.name} ,student age: {s1.age} ,student email: {s1.email}\nstudent phone number: {s1.phoneN} ,student adress: {s1.adress}")