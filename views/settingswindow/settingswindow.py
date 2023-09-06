from views.customwidgets import Toplevel, Frame, Label, Button
from views.settingswindow.welcomecontainer import WelcomeContainer
from views.settingswindow.langconfigcontainer import LangConfigContainer
from views.settingswindow.themeconfigcontainer import ThemeConfigContainer
from ttkbootstrap import Style
from models.accessfile import StringFile, ConfigFile


from tkinter.font import Font


class SettingsWindow(Toplevel):
    def __init__(self, parent=None, name="", _class="", *args, **kwargs):
        super().__init__(parent=parent, name=name, _class=_class, *args, **kwargs)
        self.attributes("-topmost", True)

        self.__width = 720
        self.__height = 377

        screenwidth = self.get_parent().get_screenwidth()
        self.__x = (screenwidth // 2) - (self.__width // 2)
        self.__y = 144

        self.__config_file = ConfigFile()
        self.__string_file = StringFile(folder=self.__config_file.get_language(),
                file_name="settingswindow")

        self.__welcome_container = None
        self.__lang_config_container = None
        self.__theme_config_container = None
        
        self.title(self.get_string("window-name"))
        self.geometry(f"{self.__width}x{self.__height}")
        self.geometry(f"+{self.__x}+{self.__y}")
        self.show_welcome_container()
    
    def get_width(self) -> int:
        return self.__width

    def set_width(self, width: int) -> None:
        self.__width = width
        self.geometry(f"{width}x{self.__height}")

    def get_height(self) -> int:
        return self.__height

    def set_height(self, height: int) -> None:
        self.__height = height
        self.geometry(f"{self.__width}x{height}")

    def get_x(self) -> int:
        return self.__x

    def set_x(self, x: int) -> None:
        self.__x = x
        self.geometry(f"+{x}+{self.__y}")

    def get_y(self) -> int:
        return self.__y

    def set_y(self, y: int) -> None:
        self.__y = y
        self.geometry(f"+{self.__x}+{y}")

    def get_string(self, string: str) -> str:
        return self.__string_file.get(string)

    def show_welcome_container(self) -> None:
        if self.__lang_config_container != None:
            self.__lang_config_container.destroy()
            self.__lang_config_container = None

        self.__welcome_container = WelcomeContainer(parent=self,
                name="welcome-container")
        self.__welcome_container.pack(expand=True, fill="both")

    def show_lang_config_container(self) -> None:
        if self.__welcome_container != None:
            self.__welcome_container.destroy()
            self.__welcome_container = None

        if self.__theme_config_container != None:
            self.__theme_config_container.destroy()
            self.__theme_config_container = None

        self.__lang_config_container = LangConfigContainer(self)
        self.__lang_config_container.pack()
    
    def show_theme_config_container(self):
        if self.__lang_config_container != None:
            self.__lang_config_container.destroy()
            self.__lang_config_container = None

        self.__theme_config_container = ThemeConfigContainer(parent=self)
        self.__theme_config_container.pack()

"""
class SettingsWindow(Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent=parent, name="settingswindow", *args, **kwargs)
        self.grab_set()
        #self.attributes("-topmost", True)
        self.lift()

        self.__width = 720
        self.__height = 377
        self.__x = (parent.get_screenwidth() // 2) - (self.__width // 2)
        self.__y = 144
        language = ConfigFile().get_language()
        self.__string_file = StringFile(folder=language,
                file_name="settingswindow")
        self.__lang_config_container = None
        self.__theme_config_container = None


        self.title(self.get_string("window-name"))
        self.geometry(f"{self.__width}x{self.__height}")
        self.geometry(f"+{self.__x}+{self.__y}")
        self.init_config_container()
    
    def get_width(self) -> int:
        return self.__width

    def set_width(self, width: int) -> None:
        self.__width = width
        self.geometry(f"{width}x{self.__height}")

    def get_height(self) -> int:
        return self.__height

    def set_height(self, height: int) -> None:
        self.__height = height
        self.geometry(f"{self.__width}x{height}")

    def get_x(self) -> int:
        return self.__x

    def set_x(self, x: int) -> None:
        self.__x = x
        self.geometry(f"+{x}+{self.__y}")

    def get_y(self) -> int:
        return self.__y

    def set_y(self, y: int) -> None:
        self.__y = y
        self.geometry(f"+{self.__x}+{y}")

    def get_string(self, string: str) -> str:
        return self.__string_file.get(string)

    def next(self) -> None:
        self.container.destroy()
        self.show_language_config_container()

    def init_config_container(self) -> None:
        self.container = Frame(parent=self)
        self.container.pack(expand=True, fill="both")

        welcome_title = Label(parent=self.container, text="Olá, seja bem vindo!",
                font=Font(family="Heveltica", size=13, weight="bold"))
        welcome_title.pack()

        welcome_text = Label(parent=self.container,  
        text="Vamos fazer algumas configurações rápidas?")
        welcome_text.pack()

        next_btn = Button(parent=self.container, text="Próximo", command=self.next)
        next_btn.pack(side="right", ipady=15)

    def show_language_config_container(self) -> None:
        if self.__theme_config_container != None:
            self.__theme_config_container.destroy()
            self.__theme_config_container = None

        self.__lang_config_container = LanguageConfigContainer(self)
        self.__lang_config_container.pack()

    def show_theme_config_container(self):
        if self.__lang_config_container != None:
            self.__lang_config_container.destroy()
            self.__lang_config_container = None

        self.__theme_config_container = ThemeConfigContainer(parent=self)
        self.__theme_config_container.pack()
"""
