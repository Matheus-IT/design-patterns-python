class LockedState:
    def __init__(self, phone):
        self.phone: 'Cellphone' = phone

    def handle_increase_volume(self):
        self.phone.unlock()

    def handle_decrease_volume(self):
        self.phone.unlock()

    def handle_play_music(self):
        pass


class UnlockedState:
    def __init__(self, phone):
        self.phone: 'Cellphone' = phone

    def handle_increase_volume(self):
        pass

    def handle_decrease_volume(self):
        pass

    def handle_play_music(self):
        print('Playing music...')


class NormalChargeLevelState:
    def __init__(self, phone, charge_level):
        self.context = phone
        self.level = charge_level

    def handle_unlock_phone(self):
        pass

    def handle_play_music(self):
        pass

    def handle_decrease_volume(self):
        pass

    def handle_increase_volume(self):
        pass


class LowChargeLevelState:
    def __init__(self, phone, charge_level):
        self.context = phone
        self.level = charge_level

    def handle_unlock_phone(self):
        print('Charge level low!')

    def handle_play_music(self):
        print('Charge level low!')

    def handle_decrease_volume(self):
        print('Charge level low!')

    def handle_increase_volume(self):
        print('Charge level low!')


class Cellphone:
    def __init__(self):
        self.lock_state = LockedState(self)
        self.charge_level_state = NormalChargeLevelState(self, charge_level=80)
        self.volume = 50

    def lock(self):
        self.lock_state = LockedState(self)

    def unlock(self):
        self.lock_state = UnlockedState(self)

    def increase_volume(self, value=10):
        self.lock_state.handle_increase_volume()
        self.charge_level_state.handle_increase_volume()

        if self.volume + value <= 100:
            self.volume += value

    def decrease_volume(self, value=10):
        self.lock_state.handle_decrease_volume()
        self.charge_level_state.handle_decrease_volume()

        if self.volume - value >= 0:
            self.volume -= value

    def play_music(self):
        self.charge_level_state.handle_play_music()
        self.lock_state.handle_play_music()


def main():
    phone = Cellphone()
    phone.unlock()
    phone.play_music()
    phone.increase_volume()
    phone.charge_level_state = LowChargeLevelState(phone, charge_level=15)
    phone.lock()
    phone.decrease_volume(20)


if __name__ == '__main__':
    main()
