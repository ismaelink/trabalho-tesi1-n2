from views.customwidgets import Radiobutton, Frame, Label, Button
from tkinter import StringVar
from PIL import Image, ImageTk
from tkinter.font import Font
from models.accessfile import StringFile, ConfigFile


images = {}

def get_image(path: str):
    image = Image.open(path)
    imagetk = ImageTk.PhotoImage(image)

    return imagetk


class LangConfigContainer(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)

        self.__chosen_language = StringVar() 
        self.__config_file = ConfigFile()
        self.font = Font(family="Heveltica", size=9)
        

        self.__title = Label(parent=self, 
                text=self.get_parent().get_string("title-langconfigcontainer"), 
                font=Font(family="Heveltica", size=21, weight="bold"))
        self.__title.grid(row=0, column=0, pady=21)
        self.__show_options_container()
        self.__show_buttons_container()
        self.columnconfigure(0, weight=1)

    def get_chosen_language(self) -> None:
        return self.__chosen_language

    def set_chosen_lang(self, value: str) -> None:
        valid_values = ["pt_br", "pt_pt", "es_es", "en_us"]
        
        if value in valid_values:
            self.__chosen_language.set(value)

    def change_choice(self, event) -> None:
        widget_clicked = event.widget

        # Checa se o objeto "widget_clicked" possui a funçao "get_class" 
        if hasattr(widget_clicked, "get_class"):
            chosen_value = widget_clicked.get_class()
            self.set_chosen_lang(chosen_value)


    def __create_option_container(self, parent, opt, value) -> Frame:
        container = Frame(parent=parent, 
                _class=value, 
                cursor="hand2", 
                border=1,
                relief="groove")

        images[value] = get_image(f"resources/images/{value}.png")

        lbl_img = Label(_class=value, parent=container, image=images[value])
        lbl_img.pack(pady=2)

        lbl_language = Label(_class=value, parent=container, text=opt, font=self.font)
        lbl_language.pack()

        rbtn_opt = Radiobutton(parent=container, _class=value, 
                value=value, variable=self.__chosen_language)
        rbtn_opt.pack()

        language = self.__config_file.get_language()
        self.__chosen_language.set(language)

        spanwidth_frm = Frame(parent=container, width=150)
        spanwidth_frm.pack()


        container.bind_all("<1>", self.change_choice)

        return container

    def __show_options_container(self) -> None:
        opts_container = Frame(parent=self)
        opts_container.grid(row=1, column=0, pady=21, sticky="nsew")
    
        opt_container_brazil = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-pt_br"), value="pt_br")
        opt_container_brazil.grid(row=0, column=0, padx=13, sticky="nsew")

        opt_container_portugal = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-pt_pt"), value="pt_pt")
        opt_container_portugal.grid(row=0, column=1, padx=13, sticky="nsew")

        opt_container_spain = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-es_es"),
                value="es_es")
        opt_container_spain.grid(row=0, column=2, padx=13, sticky="nsew")

        opt_container_usa = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-en_us"), value="en_us")
        opt_container_usa.grid(row=0, column=3, padx=13, sticky="nsew")

        opts_container.columnconfigure(0, weight=1)
        opts_container.columnconfigure(1, weight=1)
        opts_container.columnconfigure(2, weight=1)
        opts_container.columnconfigure(3, weight=1)

    def back(self) -> None:
        self.get_parent().show_welcome_container()

    def next(self) -> None:
        self.__config_file.set_language(self.__chosen_language.get())
        super().get_parent().show_theme_config_container()

    def __show_buttons_container(self) -> None:
        container = Frame(parent=self)
        container.grid(row=2, column=0, sticky="nsew", pady=76)

        text_back_btn = self.get_parent().get_string("back-btn")
        back_btn = Button(parent=container, 
                text=text_back_btn,
                command=self.back)
        back_btn.grid(row=0, column=0, ipady=15, padx=1, sticky="nsew")

        text_next_btn = self.get_parent().get_string("next-btn")
        next_btn = Button(parent=container, 
                text=text_next_btn, 
                command=self.next)
        next_btn.grid(row=0, column=1, ipady=15, padx=1, sticky="nsew")

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

