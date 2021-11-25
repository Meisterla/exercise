"""
@author        Shuo Qiu
@date          2021/11/22
@describe
"""


class Tree:
    pass


class Directory(Tree):
    def __init__(self, directory_name, files):
        self.directory_name = directory_name
        self.files = files
        self.owner = "default"

    def __str__(self):
        return f'"{self.directory_name},{self.files}"'

    def chown(self, new_owner):
        self.owner = new_owner


class PlainFile(Tree):
    def __init__(self, file_name):
        self.file_name = file_name
        self.owner = "default"

    def __str__(self):
        return f'PlainFile("{self.file_name}")'

    def chown(self, new_owner):
        self.owner = new_owner


# file = PlainFile("boot.exe")
# folder = Directory("Downloads", [])
root = Directory("root",
                 [PlainFile("boot.exe"),
                  Directory("home",
                            [Directory("thor",
                                       [PlainFile("hunde.jpg"),
                                        PlainFile("quatsch.txt")]),
                             Directory("isaac", [PlainFile("gatos.jpg")])])])


print(root)


# class FileSystem:
#     def __init__(self, directory):
#         self.directory = directory
#
#     def pwd(self):
#         print("'" + self.directory.directory_name + "'")
#
#
# fs = FileSystem(root)
#
# fs.pwd()
