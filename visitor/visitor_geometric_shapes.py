from typing import List, Protocol


class Shape(Protocol):
    def draw(self):
        ...

    def move(self):
        ...

    def accept(self, visitor: 'Visitor'):
        ...


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: 'Visitor'):
        visitor.visit_circle(self)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: 'Visitor'):
        visitor.visit_rectangle(self)


class Visitor(Protocol):
    def visit_circle(self, circle: Circle):
        ...

    def visit_rectangle(self, rectangle: Rectangle):
        ...


class XMLExportVisitor:
    def visit_circle(self, circle: Circle):
        print(f'🔵 <circle>Circle radius: {circle.radius}</circle>')

    def visit_rectangle(self, rectangle: Rectangle):
        print(
            f'🟪 <rectangle>Rectangle width: {rectangle.width},',
            f'height: {rectangle.height}</rectangle>',
        )


def export(visitor: Visitor, shapes: List[Shape]):
    for s in shapes:
        s.accept(visitor)


def main():
    shapes = [Circle(10), Rectangle(10, 20)]
    visitor = XMLExportVisitor()

    export(visitor, shapes)

    # output:
    #
    #   🔵 <circle>Circle radius: 10</circle>
    #
    #   🟪 <rectangle>Rectangle width: 10, height: 20</rectangle>


if __name__ == '__main__':
    main()
