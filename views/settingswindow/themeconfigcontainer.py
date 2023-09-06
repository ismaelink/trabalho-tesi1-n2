from views.customwidgets import Frame, Label, Button, Radiobutton
from models.accessfile import ConfigFile
from tkinter import StringVar
from tkinter.font import Font
from PIL import Image, ImageTk


images = {}

def get_image(path: str):
    image = Image.open(path)
    imagetk = ImageTk.PhotoImage(image)

    return imagetk


class ThemeConfigContainer(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent=parent, name="themeconfigcontainer", *args,
                **kwargs)

        self.__chosen_theme = StringVar()
        self.__config_file = ConfigFile()
        self.font = Font(family="Heveltica", size=9)

        self.__title = Label(parent=self,
           text=self.get_parent().get_string("title-themeconfigcontainer"),
           font=Font(family="Heveltica", size=15, weight="bold"))
        self.__title.grid(row=0, column=0, pady=21)
        self.__show_options_container()
        self.__show_buttons_container()

        self.columnconfigure(0, weight=1)

    def get_chosen_theme(self) -> StringVar:
        return self.__chosen_theme

    def set_chosen_theme(self, value: str) -> None:
        valid_values = ["litera", "minty", "darkly"]
        
        if value in valid_values:
            self.__chosen_theme.set(value)

    def change_choice(self, event) -> None:
        widget_clicked = event.widget

        # Checa se o objeto "widget_clicked" possui a funçao "get_class" 
        if hasattr(widget_clicked, "get_class"):
            chosen_value = widget_clicked.get_class()
            self.set_chosen_theme(chosen_value)

    def __create_option_container(self, parent, opt, value) -> Frame:
        container = Frame(parent=parent,
                _class=value,
                cursor="hand2",
                border=1,
                relief="groove")

        images[value] = get_image(f"resources/images/theme_{value}.png")

        lbl_img = Label(parent=container, _class=value, image=images[value])
        lbl_img.pack(pady=2)

        lbl_theme = Label(parent=container, _class=value, text=opt, font=self.font)
        lbl_theme.pack()

        rbtn_opt = Radiobutton(parent=container, _class=value, value=value,
                variable=self.__chosen_theme)
        rbtn_opt.pack()

        theme = self.__config_file.get_theme()
        self.__chosen_theme.set(theme)

        spanwidth_frm = Frame(parent=container, width=200)
        spanwidth_frm.pack()

        container.bind_all("<1>", self.change_choice)

        return container

    def __show_options_container(self) -> None:
        opts_container = Frame(parent=self)
        opts_container.grid(row=1, column=0, pady=21, sticky="nsew")
        #opts_container.pack(pady=21, expand=True, fill="x")

        opt_container_litera = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-theme_litera"),
                value="litera")
        opt_container_litera.grid(row=0, column=0, padx=15, sticky="nsew")

        opt_container_minty = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-theme_minty"),
                value="minty")
        opt_container_minty.grid(row=0, column=1, padx=15, sticky="nsew")

        opt_container_darkly = self.__create_option_container(opts_container,
                opt=self.get_parent().get_string("opt-theme_darkly"),
                value="darkly")
        opt_container_darkly.grid(row=0, column=2, padx=15, sticky="nsew")

        print(opt_container_darkly)

        opts_container.columnconfigure(0, weight=1)
        opts_container.columnconfigure(1, weight=1)
        opts_container.columnconfigure(2, weight=1)

    def back(self) -> None:
        self.get_parent().show_lang_config_container()

    def apply(self) -> None:
        self.__config_file.set_theme(self.__chosen_theme.get())
        self.__config_file.set_is_first_run("false")
        print(self.__chosen_theme.get())
        self.get_parent().destroy()

    def __show_buttons_container(self) -> None:
        container = Frame(parent=self)
        container.grid(row=2, column=0, sticky="nsew", pady=55)
        #container.pack(side="bottom", expand=True, fill="both", pady=34)

        text_back_btn = self.get_parent().get_string("back-btn")
        back_btn = Button(parent=container, text=text_back_btn,
                command=self.back)
        back_btn.grid(row=0, column=0, sticky="nsew", ipady=15, padx=1)

        text_apply_btn = self.get_parent().get_string("apply-btn")
        apply_btn = Button(parent=container, text=text_apply_btn,
                command=self.apply)
        apply_btn.grid(row=0, column=1, sticky="nsew", ipady=15, padx=1)

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

