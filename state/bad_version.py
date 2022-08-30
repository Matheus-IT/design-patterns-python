class Cellphone:
    def __init__(self):
        self.is_locked = True
        self.volume = 50
        self.charge_level = 80

    def is_charge_level_low(self):
        return self.charge_level < 20

    def lock(self):
        self.is_locked = True

    def unlock(self):
        if self.is_charge_level_low():
            print('Charge level low!')
        self.is_locked = False

    def increase_volume(self, value=10):
        if self.is_locked:
            self.is_locked = False
        if self.is_charge_level_low():
            print('Charge level low!')
        if self.volume + value <= 100:
            self.volume += value

    def decrease_volume(self, value=10):
        if self.is_locked:
            self.is_locked = False
        if self.is_charge_level_low():
            print('Charge level low!')
        if self.volume - value >= 0:
            self.volume -= value

    def play_music(self):
        if self.is_charge_level_low():
            print('Charge level low!')
        if not self.is_locked:
            print('Playing music...')


def main():
    phone = Cellphone()
    phone.unlock()
    phone.play_music()
    phone.increase_volume()
    phone.charge_level = 15
    phone.increase_volume(20)


if __name__ == '__main__':
    main()
