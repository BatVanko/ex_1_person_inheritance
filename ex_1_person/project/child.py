from project.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


chi = Child('Ivan',13)
print(chi.name)
print(chi.age)
