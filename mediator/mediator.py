from enum import Enum
from time import sleep
from typing import Literal, Union


class LandingStatus(Enum):
    LANDING = 1
    LANDED = 2
    REQUEST_LANDING = 3
    LANDING_NOT_CLEAR = 4
    LANDING_CLEAR = 5


class Mediator:
    def __init__(self, runway, plane):
        self.runway = runway
        self.runway.mediator = self

        self.plane = plane
        self.plane.mediator = self

        self.is_landing_clear = True

    def _handle_landing(self):
        print('Plane is landing... 🛬')
        self.is_landing_clear = False

    def _handle_landed(self):
        self.is_landing_clear = True
        print('Plane just landed!')

    def _handle_request_landing(self, sender):
        if sender is not self.plane:
            print('Landing denied')
            raise ValueError('Only the plane can request landing')
        if self.is_landing_clear:
            self.plane.do_land()
        else:
            print('Landing denied')

    def _handle_landing_not_clear(self, sender):
        if sender is not self.runway:
            print('Landing denied')
            raise ValueError('Only the runway can block landing')
        self.is_landing_clear = False
        print('Landing blocked 🚧')

    def _handle_landing_clear(self, sender):
        if sender is not self.runway:
            print('Landing denied')
            raise ValueError('Only the runway can unblock landing')
        self.is_landing_clear = True
        print('Landing available 🚩')

    def notify(
        self,
        sender,
        message: LandingStatus,
    ):
        if message == LandingStatus.LANDING:
            self._handle_landing()

        if message == LandingStatus.LANDED:
            self._handle_landed()

        if message == LandingStatus.REQUEST_LANDING:
            self._handle_request_landing(sender)

        if message == LandingStatus.LANDING_NOT_CLEAR:
            self._handle_landing_not_clear(sender)

        if message == LandingStatus.LANDING_CLEAR:
            self._handle_landing_clear(sender)


class Plane:
    def do_land(self):
        self.mediator.notify(self, LandingStatus.LANDING)
        sleep(2)
        self.mediator.notify(self, LandingStatus.LANDED)

    def request_landing(self):
        self.mediator.notify(self, LandingStatus.REQUEST_LANDING)


class Runway:
    def clean_runway(self):
        self.mediator.notify(self, LandingStatus.LANDING_NOT_CLEAR)
        sleep(2)

    def finish_cleaning(self):
        self.mediator.notify(self, LandingStatus.LANDING_CLEAR)


def main():
    p = Plane()
    r = Runway()

    Mediator(r, p)

    print('Runway is busy...')
    r.clean_runway()
    p.request_landing()

    print('Runway is free...')
    r.finish_cleaning()
    p.request_landing()


if __name__ == '__main__':
    main()
