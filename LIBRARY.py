from project.library import Library
from project.user import User

user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2,'Igor'))
print(library.change_username(2,'Peter'))
print(library.change_username(2,'George'))

print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.change_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secretsa',
                                                "The Prisoner of Azkaban",
                                               'The Goblet of the Phoenix',
                                                'The Order of the Phoenix',
                                                'The Half Blood Prince',
                                                'The Deathly Hallows']})

user.get_book(f'J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_avalable)
print(library.rented_books)
print(user.books)
print(user.get_book(f'J.K.Rowling', 'The Deathly Hallows', 18, library))
print(user.return_book(f'J.K.Rowling', 'The Deathly Hallows', library))
print(library.books_avalable)
print(library.rented_books)
print(user.books)