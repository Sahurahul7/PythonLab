class Stack :
    def __init__(self):
        self.List=[]
    def push(self, value):
        self.List.insert(0,value)
    def pop(self):
        return (self.List.pop())
    
Obj=Stack()
Obj.push(20)
Obj.push(22)
Obj.push(24)
Obj.push(26)
Obj.pop()
Obj.pop()
print("Remaining values in Queue are ")
print(Obj.List)
