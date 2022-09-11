import abc
from collections import namedtuple
from enum import Enum


class Problem(Enum):
    SIMPLE_LEVEL = 1
    MEDIUM_LEVEL = 2
    GEEK_LEVEL = 3


class Handler(abc.ABC):
    @abc.abstractmethod
    def handle(self, request) -> str:
        pass


class AutoResponder(Handler):
    def __init__(self):
        self.next = LiveOperator()

    def handle(self, request):
        print('tries to handle the problem in simple manner')
        if request.problem == Problem.SIMPLE_LEVEL:
            return 'Problem solved by a auto responder'
        else:
            return self.next.handle(request)


class LiveOperator(Handler):
    def __init__(self):
        self.next = TechEngineer()

    def handle(self, request):
        print('tries to handle the problem asking more questions')
        if request.problem == Problem.MEDIUM_LEVEL:
            return 'Problem solved by a live operator'
        else:
            return self.next.handle(request)


class TechEngineer(Handler):
    def handle(self, request):
        print('tries to handle the problem asking tech-like questions')
        if request.problem == Problem.GEEK_LEVEL:
            return 'Problem solved by a tech engineer'
        else:
            return 'Your problem can\'t be fixed, sorry'


def main():
    CostumerRequest = namedtuple('CustomerRequest', 'problem')

    # Customer makes a request of a problem that happened in his computer
    print('Problem 1')
    request = CostumerRequest(problem=Problem.MEDIUM_LEVEL)
    response = AutoResponder().handle(request)
    print(response)

    print('Problem 2')
    request = CostumerRequest(problem=Problem.GEEK_LEVEL)
    response = AutoResponder().handle(request)
    print(response)

    # Output:
    #
    # Problem 1
    # tries to handle the problem in simple manner
    # tries to handle the problem asking more questions
    # Problem solved by a live operator
    #
    # Problem 2
    # tries to handle the problem in simple manner
    # tries to handle the problem asking more questions
    # tries to handle the problem asking tech-like questions
    # Problem solved by a tech engineer


if __name__ == '__main__':
    main()
