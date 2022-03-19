from typing import Protocol


class Transport(Protocol):
    def deliver(self):
        ...


class Truck:
    def __init__(self, delivery_plan):
        self.delivery_plan = delivery_plan

    def deliver(self):
        print(f'{self.delivery_plan} 🚚')


class Ship:
    def __init__(self, delivery_plan):
        self.delivery_plan = delivery_plan

    def deliver(self):
        print(f'{self.delivery_plan} 🚢')


class Logistics(Protocol):
    def _plan_delivery(self):
        ...

    def create_transport(self) -> Transport:
        ...


class RoadLogistics:
    def _plan_delivery(self):
        return 'Deliver by land in a box'

    def create_transport(self) -> Transport:
        return Truck(self._plan_delivery())


class SeaLogistics:
    def _plan_delivery(self):
        return 'Deliver by sea in a container'

    def create_transport(self) -> Transport:
        return Ship(self._plan_delivery())


def client_code(logistics: Logistics):
    transport = logistics.create_transport()
    transport.deliver()


def main():
    client_code(SeaLogistics())  # I want logistics related to sea services
    client_code(RoadLogistics())  # Now the one related to road services


if __name__ == '__main__':
    main()
