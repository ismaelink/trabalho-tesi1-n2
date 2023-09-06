from tkinter.ttk import Frame
from views.node import Node


class Frame(Frame, Node):
    def __init__(self, 
                 parent=None, 
                 name="", 
                 _class="", 
                 *args, 
                 **kwargs):
        super().__init__(parent, *args, **kwargs)

        Node.__init__(self, parent=parent, name=name, _class=_class)


    def get_class(self) -> str:
        return Node.get_class(self)

