class Email:
    def __init__(self):
        self.a=0
        self.b=0
    def Get(self):
        self.a=input("Enter the Email ")
    def Split(self):
        self.b=self.a.split('@')
    def Show(self):
        print(self.b)
Obj=Email()
Obj.Get()
Obj.Split()
Obj.Show()
