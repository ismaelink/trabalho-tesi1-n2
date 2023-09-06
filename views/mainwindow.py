from views.settingswindow.settingswindow import SettingsWindow
from views.customwidgets import Tk, Button, Toplevel, Label
from views.settingswindow import SettingsWindow
from views.mainheader import MainHeader
from models.accessfile import ConfigFile, StringFile
from ttkbootstrap import Style
from ttkbootstrap.constants import SUCCESS
from tkinter import messagebox
import time


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__screenwidth = self.winfo_screenwidth()
        self.__screenheight = self.winfo_screenheight()
        self.__config_file = ConfigFile()
        self.__string_file = StringFile(folder="", file_name="mainwindow")
        self.__style = Style(self.__config_file.get_theme())


        self.title(self.__string_file.get("app-name"))
        self.geometry(f"{self.get_screenwidth()}x{self.get_screenheight()}")
        self.__check_settings()
        self.show_main_header()
        self.__set_events()   
        self.mainloop()

    def get_screenwidth(self) -> int:
        return self.__screenwidth

    def get_screenheight(self) -> int:
        return self.__screenheight

    def get_style(self) -> str:
        return self.__style

    def set_style(self, new_theme: str) -> None:
        self.__style.theme_use(new_theme)

    def __check_settings(self) -> None:
        if self.__config_file.get_is_first_run() == "true":
            settings_window = SettingsWindow(parent=self, name="settingswindow")

            # Espera a janela de configurações (settings_window)
            # ser fechada para, então, continuar a execução da 
            # aplicação.
            self.wait_window(settings_window)
            self.__config_file.set_all()
            self.set_style(self.__config_file.get_theme())

    def show_main_header(self) -> None:
        main_header = MainHeader(parent=self, name="mainheader")
        main_header.grid(row=0, column=0, sticky="nsew")

    def close(self) -> None:
        result = messagebox.askyesno("Confirmação", "Você deseja realmente sair?")

        if result:
            self.destroy()

    def __set_events(self):
        self.bind("<Control-q>", lambda event: self.close())
        self.protocol("WM_DELETE_WINDOW", self.close)

