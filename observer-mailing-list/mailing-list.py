from abc import ABC, abstractmethod
from typing import List


class MailingListPublisherAbc(ABC):
    """Publisher interface with a set of methods for managing subscribers"""

    @abstractmethod
    def add_subscriber(self, subscriber):
        raise NotImplementedError

    @abstractmethod
    def remove_subscriber(self, subscriber):
        raise NotImplementedError

    @abstractmethod
    def notify(self):
        raise NotImplementedError

    @abstractmethod
    def process_latest_content(self) -> str:
        raise NotImplementedError


class SubscriberAbc(ABC):
    """Subscriber interface to interact with publisher"""

    @abstractmethod
    def interact_with_new_content(self, publisher: MailingListPublisherAbc):
        raise NotImplementedError


class MailingListPublisher(MailingListPublisherAbc):
    """Publisher of mailing list"""

    _latest_content: str = ''
    _subscribers: List[SubscriberAbc] = []

    def add_subscriber(self, subscriber: SubscriberAbc) -> None:
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: SubscriberAbc) -> None:
        try:
            self._subscribers.remove(subscriber)
        except ValueError:
            print('Tried to remove nonexisting subscriber!')

    def update_latest_content(self, new_content: str):
        self._latest_content = new_content
        self.notify()

    def notify(self) -> None:
        for s in self._subscribers:
            s.interact_with_new_content(self)

    def process_latest_content(self):
        return f'This is the latest content 📮: {self._latest_content}'


class SubscriberReaderKind(SubscriberAbc):
    """This is the kind of subscriber which always reads the latest content"""

    def interact_with_new_content(self, publisher: MailingListPublisherAbc):
        content = publisher.process_latest_content()
        self.read(content)

    @staticmethod
    def read(content: str):
        print(content)
        print('Reader says: humm, how interesting...')


class SubscriberProcrastinatorKind(SubscriberAbc):
    """This guy never reads, always saying: latter... 😂"""

    def interact_with_new_content(self, publisher: MailingListPublisherAbc):
        content = publisher.process_latest_content()
        print('Procrastinator says: Nah! I\'ll read latter. 😪')


def main():
    publisher = MailingListPublisher()

    reader = SubscriberReaderKind()
    procrastinator = SubscriberProcrastinatorKind()

    publisher.add_subscriber(reader)
    publisher.add_subscriber(procrastinator)

    publisher.update_latest_content('Programmers are filthy rich! 🤑')

    publisher.remove_subscriber(procrastinator)
    print('Bye bye procrastinator! Well, this guy never reads anyway! 🤷‍♂️')


if __name__ == '__main__':
    main()
