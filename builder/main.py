from dataclasses import dataclass, field
from typing import Union


@dataclass
class User:
    name: str  # required field
    age: Union[int, None] = field(init=False, default=None)
    phone: Union[str, None] = field(init=False, default=None)
    address: Union[str, None] = field(init=False, default=None)
    email: Union[str, None] = field(init=False, default=None)


class UserBuilder:
    def __init__(self, name: str):
        self.reset(name)

    def reset(self, name: str):
        self.user = User(name)
        return self

    def set_age(self, age: int):
        self.user.age = age
        return self

    def set_phone(self, phone: str):
        self.user.phone = phone
        return self

    def set_address(self, address: str):
        self.user.address = address
        return self

    def set_email(self, email: str):
        self.user.email = email
        return self

    def build(self):
        return self.user


def main():
    builder = UserBuilder('Matheus Costa')  # name is required

    # Builder setting optional stuff
    builder.set_phone('999999999999')

    user = builder.build()

    print(user)
    # Output:
    # User(
    #   name='Matheus Costa',
    #   age=None,
    #   phone='999999999999',
    #   address=None,
    #   email=None
    # )


if __name__ == '__main__':
    main()
