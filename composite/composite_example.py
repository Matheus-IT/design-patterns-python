from abc import ABC
from typing import List


class Component(ABC):
    def execute(self, text: str) -> str:
        raise NotImplementedError()


class Leaf(Component):
    def __init__(self, text: str):
        self.text = text

    def execute(self, text: str) -> str:
        return f'<p>{self.text} - {text}</p>\n'


class Composite(Component):
    def __init__(self, name: str, children: List[Component] = None):
        self.name = name
        self.children = children or []

    def add(self, child: Component):
        self.children.append(child)

    def remove(self, child: Component):
        self.children.remove(child)

    def execute(self, text: str) -> str:
        result = f'{self.name}:\n'
        for child in self.children:
            result += child.execute(text)
        return result


def main():
    composite = Composite('Composite1')

    composite.add(Leaf('l1'))
    composite.add(Leaf('l2'))
    composite.add(Leaf('l3'))

    composite2 = Composite('Composite2')
    composite2.add(Leaf('l4'))
    composite2.add(Leaf('l5'))

    composite.add(composite2)

    print(composite.execute('text'))

    # Output:
    #     Composite1:
    #     <p>l1 - text</p>
    #     <p>l2 - text</p>
    #     <p>l3 - text</p>
    #     Composite2:
    #     <p>l4 - text</p>
    #     <p>l5 - text</p>


if __name__ == '__main__':
    main()
