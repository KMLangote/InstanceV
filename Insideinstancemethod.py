class Test:
    def __init__(self):
        self.a =100
        self.b=200
    def m1(self):
        self.c=300
t=Test()
t.m1()
print(t.__dict__)