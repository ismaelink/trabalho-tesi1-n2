from views.customwidgets import Frame, Label, Button
from models.accessfile import ConfigFile, StringFile
from tkinter.font import Font


class WelcomeContainer(Frame):
    def __init__(self, parent=None, name="", _class="", *args, **kwargs):
        super().__init__(parent=parent,
                         name=name, 
                         _class=_class, 
                         *args,
                         **kwargs)

        self.__show_text_container()
        self.__show_button_container()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def __show_text_container(self) -> None:
        container = Frame(parent=self)
        container.grid(row=0, column=0)

        title_font = Font(family="Heveltica", size=21, weight="bold")
        text_font = Font(family="Heveltica", size=12)


        welcome_title = Label(parent=container, 
                text=self.get_parent().get_string("welcome-title"),
                font=title_font)
        welcome_title.grid(row=0, column=0)

        welcome_text = Label(parent=container, 
                text=self.get_parent().get_string("welcome-text"),
                font=text_font)
        welcome_text.grid(row=1, column=0, pady=21)


    def next(self) -> None:
        self.get_parent().show_lang_config_container()
    
    def __show_button_container(self) -> None:
        container = Frame(parent=self, name="button_container")
        container.grid(row=1, column=0)

        next_btn = Button(parent=container, name="next_btn",
                text=self.get_parent().get_string("next-btn"),
                command=self.next)
        next_btn.pack(ipady=15, ipadx=100, side="right")
        
