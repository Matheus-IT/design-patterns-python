from abc import ABC, abstractclassmethod
from collections import namedtuple
from time import sleep
import timeit
from typing import List


class TransportationStrategy(ABC):
    @abstractclassmethod
    def get_to_airport(self, person):
        raise NotImplementedError


class BicycleStrategy(TransportationStrategy):
    def get_to_airport(self, person):
        print(
            f'{person.name} is going by bicycle... 🚴\n'
            'It takes more time, but it\'s good for the trees 🌳\n'
        )
        sleep(2)


class BusStrategy(TransportationStrategy):
    def get_to_airport(self, person):
        print(
            f'{person.name} is going by bus... 🚌\n'
            'It\'s faster and cheaper 💰\n'
        )
        sleep(1)


class CarStrategy(TransportationStrategy):
    def get_to_airport(self, person):
        print(
            f'{person.name} is going by car 🚗\nIt\'s more convenient and '
            'fast, but you have to spend more money 💸\n'
        )
        sleep(0.5)


class TransportationAssessment:
    """Assess each transportation strategy to get the faster way possible"""

    def __init__(self, person, strategies: List[TransportationStrategy]):
        self.person = person
        self.strategies = strategies

    def perform_assessment(self):
        fastest = self.strategies[0]
        fastest_elapse = None

        for s in self.strategies:
            elapse = timeit.timeit(
                lambda: s.get_to_airport(self.person), number=1
            )

            if fastest_elapse is None or elapse < fastest_elapse:
                fastest_elapse = elapse
                fastest = s
        return fastest


def main():
    Person = namedtuple('Person', 'name age')
    p = Person('John', 35)

    strategies = [
        BicycleStrategy(),
        BusStrategy(),
        CarStrategy(),
    ]

    assessment_obj = TransportationAssessment(p, strategies)
    fastest_strategy = assessment_obj.perform_assessment()
    print(f'The fastest strategy is {fastest_strategy.__class__.__name__}')


if __name__ == '__main__':
    main()
