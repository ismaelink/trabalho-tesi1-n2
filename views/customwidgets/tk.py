from tkinter import Tk
from views.node import Node

class Tk(Tk, Node):
    def __init__(self, 
                 name="", 
                 _class="", 
                 *args, 
                 **kwargs):
        super().__init__(*args, **kwargs)
        Node.__init__(self, parent=None, name=name, _class=_class)

    def get_class(self) -> str:
        return Node.get_class(self)

