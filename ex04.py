"""
@author        Shuo Qiu
@date          2021/11/22
@describe
"""


def print_tree(directory):
    result = ""
    result += directory.directory_name
    return result


class Tree:
    pass


class Directory(Tree):
    def __init__(self, directory_name, files):
        self.directory_name = directory_name
        self.files = files

    def __str__(self):
        return print_tree(self)


class PlainFile(Tree):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"{self.file_name}"


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
