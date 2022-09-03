import abc
from abc import abstractmethod


class HouseTemplate(abc.ABC):
    def build_house(self):
        self._hook_present_house()
        self._build_walls()
        self._build_roof()
        self._build_entrance()
        self._build_windows()

    def _build_walls(self):
        print('building walls with bricks')

    def _build_roof(self):
        print('building roof with tiles')

    @abstractmethod
    def _build_entrance(self):
        pass

    @abstractmethod
    def _build_windows(self):
        pass

    def _hook_present_house(self):
        pass


class House1(HouseTemplate):
    def _build_entrance(self):
        print('building entrance with wooden door')

    def _build_windows(self):
        print('building square windows')


class House2(HouseTemplate):
    def _build_entrance(self):
        print('building entrance with cristal door')

    def _build_windows(self):
        print('building round windows')

    def _hook_present_house(self):
        print('Presenting a second house')


def main():
    house1 = House1()
    print('\nBuilding House1:')
    house1.build_house()

    house2 = House2()
    print('\nBuilding House2:')
    house2.build_house()

    # Code output:
    #
    # Building House1:
    # building walls with bricks
    # building roof with tiles
    # building entrance with wooden door
    # building square windows
    #
    # Building House2:
    # Presenting a second house
    # building walls with bricks
    # building roof with tiles
    # building entrance with cristal door
    # building round windows


if __name__ == '__main__':
    main()
