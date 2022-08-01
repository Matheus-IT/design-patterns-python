from enum import Enum
from typing import List
from PIL import Image
from memory_profiler import profile


class TreeSprite:
    def __init__(self, src):
        self.src: str = src

    def get_image(self):
        return Image.open(self.src)


class Color(Enum):
    GREEN = 1
    BLUE = 2
    PINK = 3


class TreeType:
    """
    This is the flyweight object, which stores intrinsic state, that is,
    the immutable state of the object.
    """

    def __init__(self, name, sprite, color):
        self.name: str = name
        self.sprite: TreeSprite = sprite
        self.color: Color = color

    def __str__(self):
        return f"TreeType: {self.name} {self.sprite} {self.color}"


class TreeFactory:
    tree_types: List[TreeType] = []

    @staticmethod
    def get_tree_type(name, sprite, color):
        tree_type = TreeType(name, sprite, color)

        try:
            index = TreeFactory.tree_types.index(tree_type)
            tree_type = TreeFactory.tree_types[index]
        except ValueError:
            TreeFactory.tree_types.append(tree_type)
        return tree_type


class Tree:
    """
    This object stores extrinsic state, that is, the mutable
    state of the object.
    """

    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type: TreeType = tree_type

    def draw(self):
        image = self.tree_type.sprite.get_image()
        print(f"Drawing tree at {self.x}, {self.y}")
        image.show()


class Forest:
    def __init__(self):
        self.trees: List[Tree] = []

    def add_tree(self, x, y, name, sprite, color):
        tree_type = TreeFactory.get_tree_type(name, sprite, color)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


@profile
def main():
    forest = Forest()
    for i in range(5):
        for j in range(5):
            forest.add_tree(
                i,
                j,
                "Mulberry",
                TreeSprite("images/mulberry.jpg"),
                Color.GREEN,
            )
    forest.draw()


if __name__ == '__main__':
    main()
