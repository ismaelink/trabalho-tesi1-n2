class Node:
    def __init__(self, parent=None, name="", _class="", element=None):
        self.__parent = parent
        self.__name = name
        self.__class = _class
        self.__element = element
        self.__children = []


    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_class(self) -> str:
        return self.__class

    def set_class(self, _class: str) -> None:
        self.__class = _class

    def get_parent(self):
        return self.__parent

    def add_child(self, child_node) -> None:
        self.__children.append(child_node)

    def remove_child(self, child_name: str):
        for child in self.__children:
            if child.get_name() == child_name:
                self.__children.remove(child)
                return child

        return Node()

    

