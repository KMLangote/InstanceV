class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
t1 = Test()
t2 = Test()
t1.a=999
t1.b=888
print(t1.__dict__)
print(t2.__dict__)