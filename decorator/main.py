from dataclasses import dataclass


class Notifier:
    def send(self, msg):
        print(f'writing to log file... {msg}')


@dataclass
class BaseDecorator:
    wrappee: Notifier

    def send(self, msg):
        self.wrappee.send(msg)


class SMSDecorator(BaseDecorator):
    def send(self, msg):
        super().send(msg)
        self.send_sms(msg)
    
    def send_sms(self, msg):
        print(f'sending sms {msg}')

class FacebookDecorator(BaseDecorator):
    def send(self, msg):
        super().send(msg)
        self.send_facebook(msg)
    
    def send_facebook(self, msg):
        print(f'sending facebook notification {msg}')


class SlackDecorator(BaseDecorator):
    def send(self, msg):
        super().send(msg)
        self.send_slack(msg)
    
    def send_slack(self, msg):
        print(f'sending slack notification {msg}')


@dataclass
class Application:
    notifier: Notifier

    def send_notification(self, msg):
        self.notifier.send(msg)


def main():
    stack = Notifier()
    stack = FacebookDecorator(stack)
    stack = SlackDecorator(stack)

    app = Application(stack)
    app.send_notification('my message')


if __name__ == '__main__':
    main()
