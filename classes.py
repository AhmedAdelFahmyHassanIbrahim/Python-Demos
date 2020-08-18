class Presenter():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("In the getter")
        return self.__name
    
    @name.setter
    def name(self, value):
        print("Print in setter")
        self.__name = value

    def say_hello(self):
        print(self.name)

        

presenter = Presenter('Chris')
presenter.name = "Ahmed"
#presenter.say_hello()
print(presenter.name)