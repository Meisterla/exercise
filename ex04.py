"""
@author        Shuo Qiu
@date          2021/11/22
@describe
"""


class File:
    def __init__(self, owner="default"):
        self.owner = owner

    def chown(self, new_owner):
        self.owner = new_owner


class Directory(File):
    def __init__(self, directory_name, files):
        self.directory_name = directory_name
        self.files = files

    def __repr__(self):
        return f'Directory({self.directory_name},{self.files}'

    def ls(self, retract=""):
        print(retract + self.directory_name)
        retract += "    "
        for i in self.files:
            try:
                i.files
            except AttributeError:
                print(retract + str(i)[11:-2])
            else:
                i.ls(retract)


class PlainFile(File):
    def __init__(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        return f'PlainFile("{self.file_name}")'


file = PlainFile("boot.exe")
folder = Directory("Downloads", [])
root = Directory("root",
                 [PlainFile("boot.exe"),
                  Directory("home",
                            [Directory("thor",
                                       [PlainFile("hunde.jpg"),
                                        PlainFile("quatsch.txt")]),
                             Directory("isaac", [PlainFile("gatos.jpg")])])])


print(root)
# root.ls()


class FileSystem:
    def __init__(self, directory):
        self.directory = directory
        self.directory_name = self.directory.directory_name
        self.files = self.directory.files
        self.info_dict = {self.directory_name: self.files}
        self.fun_info_dict(self.files)

    def fun_info_dict(self, files):
        for i in files:
            try:
                i.files
            except AttributeError:
                continue
            else:
                self.info_dict[i.directory_name] = i.files
                self.fun_info_dict(i.files)

    def __repr__(self):
        return str(self.directory_name) + str(self.files)

    def pwd(self):
        print("'" + self.directory_name + "'")

    def ls(self, retract=""):
        print(retract + self.directory_name)
        retract += "    "
        for i in self.files:
            try:
                i.files
            except AttributeError:
                print(retract + str(i)[11:-2])
            else:
                i.ls(retract)

    def cd(self, directory):
        if directory == "..":
            for i in self.info_dict:
                for j in self.info_dict[i]:
                    try:
                        j.files
                    except AttributeError:
                        continue
                    else:
                        if self.directory_name == j.directory_name:
                            self.directory_name = i
                            self.files = self.info_dict[i]
        elif directory not in self.info_dict:
            print("The directory does not exist!")
        else:
            self.directory_name = directory
            self.files = self.info_dict[directory]

    def create_file(self, name):
        if name in self.info_dict:
            print("The directory has already exist within the working directory.")
        else:
            self.files.append(Directory(name, []))
            self.info_dict[name] = []

    def mkdir(self, name):
        p_file_list = []
        for i in self.files:
            try:
                i.files
            except AttributeError:
                p_file_list.append(i.file_name)
            else:
                continue

        if name in p_file_list:
            print("The file has already exist within the working directory.")
        else:
            self.files.append('PlainFile("' + name + '")')

    def rm(self, name):
        if name not in self.info_dict:
            for i in self.files:
                try:
                    i.file_name
                except AttributeError:
                    continue
                else:
                    if name == i.file_name:
                        self.files.pop(self.files.index(i))
        else:
            for i in self.files:
                try:
                    i.files
                except AttributeError:
                    continue
                else:
                    if name == i.directory_name:
                        if not self.files[self.files.index(i)].files:
                        # if self.files[self.files.index(i)].files == []:
                            self.files.pop(self.files.index(i))
                        else:
                            print("Sorry, the directory is not empty.")

    def find(self, name):
        path = self.directory_name + "/"
        if name not in self.info_dict:
            f_file_list = self.fun_find("f_file", name)
            for i in f_file_list:
                path += i + "/"
        path = path[:-1]
        print(path)

    def fun_find(self, tp, name):
        if tp == "f_file":
            f_file_list = []
            f_file_temp = str(self.info_dict[self.directory_name])
            f_file_temp = f_file_temp.replace("Directory(", "").replace(" ", "").replace("[", "").replace("]", "")\
                .replace('PlainFile("', "").replace('")', "")
            for i in f_file_temp.split(","):
                if i in self.info_dict or i == name:
                    f_file_list.append(i)
            f_file_list = f_file_list[:f_file_list.index(name) + 1]
            return f_file_list


print("------------------------------")

fs = FileSystem(root)

# fs.pwd()
# fs.ls()

# fs.cd("home")
# fs.pwd()
# fs.ls()

# fs.create_file("test")
# fs.cd("test")
# fs.mkdir('boot.exe2')

# fs.cd("home")
# fs.cd("..")

