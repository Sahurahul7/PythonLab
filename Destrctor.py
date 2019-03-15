class Time:
    def __init__(self):
        print("Constructor is called ")
    def __del__(self):
        print("Destructor is called ")
Obj=Time()
del Obj
