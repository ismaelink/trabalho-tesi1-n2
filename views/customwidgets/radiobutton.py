from tkinter.ttk import Radiobutton
from views.node import Node


class Radiobutton(Radiobutton, Node):
    def __init__(self, 
                 name="", 
                 _class="", 
                 parent=None, 
                 *args, 
                 **kwargs):
        super().__init__(parent, *args, **kwargs)

        Node.__init__(self, parent=parent, name=name, _class=_class)

    def get_class(self) -> str:
        return Node.get_class(self)

