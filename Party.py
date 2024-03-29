class Person:
    def __init__(self, name):
        self.name = name

class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def names_faces(self):
        return', '.join(person.name for person in self.people)


    def number_guests(self):
        return len(self.people)

party = Party()

while True:
    command = input()
    if command == "Stop":
        break
    name = command
    person = Person(name)
    party.invite(person)

print(f'Going : {party.names_faces()}')
print(f'Total : {party.number_guests()}')