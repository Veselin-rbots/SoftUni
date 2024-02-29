class Person:
    def __init__(self, name):
        self.name = name

    def get_atributes_with_prefix(self, prefix):
        # get_attributes_with_prefix('name')
        pass

    def set_later_value(self):
        self.age = 17

    def __repr__(self):
        return ':'.join(f'{ key}={value}' for (key, value) in self.__dict__.items())


pesho = Person('Pesho')
print(pesho.__dict__)
pesho.age = 13
print(pesho.__dict__)
pesho.print_state()
example = str(pesho)
print(example)