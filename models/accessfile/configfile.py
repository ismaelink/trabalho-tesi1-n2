import json


class ConfigFile:
    def __init__(self):
        self.__is_first_run = None
        self.__language = None
        self.__theme = None
        
        self.__config_file_path = "resources/config_files/configure.json"

        self.set_all()

    def get_is_first_run(self) -> str:
        return self.__is_first_run

    def set_is_first_run(self, is_first_run: str) -> None:
        is_first_run = is_first_run.lower()

        config_file = self.__get_config_file()
        config_file["is_first_run"] = is_first_run

        self.__set_config_file(config_file)
        self.__is_first_run = is_first_run

    def get_language(self) -> str:
        return self.__language

    def set_language(self, new_language: str) -> None:
        new_language = new_language.lower()

        config_file = self.__get_config_file()
        config_file["language"] = new_language
        
        self.__set_config_file(config_file)
        self.__language = new_language

    def get_theme(self) -> str:
        return self.__theme

    def set_theme(self, new_theme: str) -> None:
        new_theme = new_theme.lower()

        config_file = self.__get_config_file()
        config_file["theme"] = new_theme

        self.__set_config_file(config_file)
        self.__theme = new_theme

    def __get_config_file(self) -> dict:
        config_file = {}

        with open(self.__config_file_path, "r") as json_file:
            config_file = json.load(json_file)

        return config_file

    def __set_config_file(self, new_file) -> None:
        with open(self.__config_file_path, "w") as json_file:
            json.dump(new_file, json_file, indent=3)
            
    def set_all(self) -> None:
        config_file = self.__get_config_file()

        self.__is_first_run = config_file["is_first_run"]
        self.__language = config_file["language"]
        self.__theme = config_file["theme"]

