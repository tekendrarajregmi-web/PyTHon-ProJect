class store:

    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

    def call(self):
        print(self.show())

per1 = store("wwww")

print(per1.call())