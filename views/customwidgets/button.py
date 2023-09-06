from tkinter.ttk import Button
from views.node import Node


class Button(Button, Node):
    def __init__(self, 
                 parent=None, 
                 name="", 
                 _class="", 
                 *args, 
                 **kwargs):

        kwargs.setdefault("cursor", "hand2")

        super().__init__(parent, *args, **kwargs)
        Node.__init__(self, parent=parent, name=name, _class=_class)

