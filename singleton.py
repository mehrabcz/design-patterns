"""
A simple logger written by singleton design pattern

author: mehrab <mehrabox@gmail.com>
"""
from datetime import datetime


class Singleton(type):
    _instances = {} # contains created instances
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # instance dose not exists so create and save it 
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls] # instance already exists


class Logger(metaclass=Singleton):
    def __init__(self, file_name):
        self.file_name = file_name # file name which should logging in

    def __write_log(self, level, log):
        with open(self.file_name, 'a+') as log_file:
            log_file.write(f"[{datetime.now()}]-[{level}]   {log}\n")

    def info(self, log):
        self.__write_log("INFO", log)

    def error(self, log):
        self.__write_log("INFO", log)

    def warning(self, log):
        self.__write_log("INFO", log)

    def debug(self, log):
        self.__write_log("INFO", log)


if __name__ == '__main__':
    obj_1 = Logger("singleton.log")
    obj_2 = Logger("singleton2.log")
    print(id(obj_2) == id(obj_2)) # to test it works fine it should be True ; )
