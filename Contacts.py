class Person:
    def __init__(self, name):
       self.name = name

    def say_hi(self):
        print(f"Saying Hi,my name is{self.name}")

    def say_bye(self):
        print(f'Saying Bye.my name is {self.name}')

jordan = Person("Jordan")
jordan.say_hi()
jordan.say_bye()

Ivan = Person("Jordan")
Ivan.say_hi()
Ivan .say_bye()


# party = Party()
#
# line = input()
# while line != "End":
#     party.people.append(line)
#     line = input()


# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len.(party.people)}")

