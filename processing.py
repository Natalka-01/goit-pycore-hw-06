from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(value) != 10:
            raise ValueError("The phone number should contain 10 numbers")
        else:
              self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        "This method checks if the phone number exists in the list and deletes it"
        for p in self.phones:
              if p.value == phone:
                  self.phones.remove(p)
                  return
        raise ValueError("Phone number not found")

    def edit_phone(self, old_phone, new_phone):
          "This method checks that the old phone number is exist in the list and edit it "
          for p in self.phones:
                if p.value == old_phone: 
                    p.value = Phone(new_phone).value
                    return
          raise ValueError("Phone number not found")
    
    def find_phone(self, phone):
          "This method checks if the phone number exists in the list and returns it"
          for p in self.phones:
                if p.value == phone:
                      return p
          raise ValueError("Phone number not found")
          

    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
     def add_record(self, record):
          self.data[record.name.value] = record

     def find(self, name):
          return self.data.get(name, None)
     
     def delete(self, name):
          if name in self.data:
               del self.data[name]




