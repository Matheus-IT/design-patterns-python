class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def charge_laptop(self) -> str:
        return 'Target: try to put laptop to charge with BR plug'


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is
    incompatible with the existing client code. The Adaptee needs some
    adaptation before the client code can use it.
    """

    def put_laptop_to_charge(self) -> str:
        return 'gulp naeporue htiw egrahc ot potpal tup yrt :eetpadA'


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via composition.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def charge_laptop(self) -> str:
        return f'Adapter: (TRANSLATED) {self.adaptee.put_laptop_to_charge()[::-1]}'


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.charge_laptop())


if __name__ == "__main__":
    print('Client: I can work just fine with the Target objects:')
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print('Client: The Adaptee class has a weird interface. '
          'See, I don\'t understand it:')
    print(f'Adaptee: {adaptee.put_laptop_to_charge()}')

    print('Client: But I can work with it via the Adapter:')
    adapter = Adapter(adaptee)
    client_code(adapter)
