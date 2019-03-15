class Time:
    def __init__(self):
        self.time=0
    def Get(self):
        self.time=input("Enter the time ")
    def Show(self):
        print("time = "+self.time)
Obj=Time()
Obj.Get()
Obj.Show()
