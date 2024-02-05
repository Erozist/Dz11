from datetime import datetime
from collections import UserDict


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        print('Getattr')
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value
        print('Setter')

    def __str__(self):
        return str(self.__value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        Field.__init__(self, value)
        if value.isdigit() and len(value) == 10:
            pass
        else:
            raise ValueError('The phone number is in the wrong format!')


class Birthday(Field):
    def __init__(self, value):
        Field.__init__(self, value)
        if value == None:
            pass
        elif len(value) == 10 and value[0:2].isdigit() and value[3:5].isdigit()\
                and value[6:10].isdigit() and value[2] == '.' and value[5] == '.':
            pass
        else:
            raise ValueError('Incorrect date of birth format!')


class Record:
    def __init__(self, name, day_birthday=None):
        self.name = Name(name)
        self.phones = []
        self.day_birthday = Birthday(day_birthday)


    def add_phone(self, num):
        self.phones.append(Phone(num))
        return self.phones


    def remove_phone(self, num):
        for i, phone in enumerate(self.phones):
            if num in phone.value:
                del self.phones[i] #self.phones.remove(num)


    def edit_phone(self, old_num, new_num):
        for i, phone in enumerate(self.phones):
            if old_num in phone.value:
                self.phones[i] = Phone(new_num)
                return self.phones
        raise ValueError('This phone does not exist')


    def find_phone(self, num):
        for phone in self.phones:
            if num in phone.value:
                return Phone(num)
        return None

    def days_to_birthday(self):
        today = datetime.now().date()
        birth = datetime.strptime(str(self.day_birthday), '%d.%m.%Y').date()
        birth = birth.replace(year=today.year)
        if birth == today:
            print('There are 0 days left until the birthday. Happy Birthday!')
        else:
            if birth < today:
                birth = birth.replace(year=today.year + 1)
                days_before = birth - today
                print(f'There are {days_before.days} days left until the birthday.')

            else:
                days_before = birth - today
                print(f'There are {days_before.days} days left until the birthday.')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, args):
        self.data[args.name.value] = args
        return self.data


    def find(self, name):
        if name in self.data:
            return self.data[name]


    def delete(self, name):
        delete_value = self.data.pop(name, 'No Key found')
        print(f'{delete_value} -- Deleted!')

    def iterator(self, num):
        i = 0
        while i < len(self.data):
            print('iterator on yield')
            yield list(self.data)[i:i+num]
            i += num
            print('iterator off yield')



if __name__ == "__main__":
    # ...
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John", '20.06.1987')
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)
    
    # Додавання запису John до адресної книги
    john_record.days_to_birthday()

    # Створення та додавання нових записів дляперевірки ітератора
    for i in range(10):
        john_record = Record('John'+str(i))
        john_record.add_phone("123456789"+str(i))
        book.add_record(john_record)

    # Виведення записів через ітератор
    itr = book.iterator(4)
    for i in itr:
        print(i)


    # Додавання запису John до адресної книги
    #book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
