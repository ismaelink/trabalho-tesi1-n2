import json


class StringFile:
    def __init__(self, folder: str, file_name: str):
        self.__path = f"resources/string/{folder}/{file_name}.json"

        self.__string_file = {}
        with open(self.__path, "r") as json_file:
            self.__string_file = json.load(json_file)

    def get(self, string: str) -> str:
        return self.__string_file[string]

