"""
@author        Shuo Qiu
@date          2021/11/22
@describe
"""


class File:
    pass


class Directory(File):
    """
    Directory class
    """
    def __init__(self, directory_name, files, owner="default"):
        """
        :param directory_name: name of the directory
        :param files: file for details, it is a list
        """
        self.directory_name = directory_name
        self.files = files
        self.owner = owner

    def __repr__(self):  # Output method.
        return f'Directory({self.directory_name},{self.files}'

    def chown(self, new_owner):  # Owner updated method
        self.owner = new_owner

    def ls(self, retract=""):  # Recursively traverses directories and files
        print(retract + self.directory_name)
        retract += "    "  # Define the retract
        for i in self.files:
            try:  # If i is a directory,recurse, else print it
                i.files
            except AttributeError:
                print(retract + str(i)[11:-2])
            else:
                i.ls(retract)


class PlainFile(File):
    """
    PlainFile class
    """
    def __init__(self, file_name, owner="default"):
        """
        :param file_name: file name
        """
        self.file_name = file_name
        self.owner = owner

    def __repr__(self):
        return f'PlainFile("{self.file_name}")'

    def chown(self, new_owner):
        self.owner = new_owner


print("Testing question 1")
file = PlainFile("boot.exe")  # Instantiate a plain file
folder = Directory("Downloads", [])  # Instantiate a directory
root = Directory("root",
                 [PlainFile("boot.exe"),
                  Directory("home",
                            [Directory("thor",
                                       [PlainFile("hunde.jpg"),
                                        PlainFile("quatsch.txt")]),
                             Directory("isaac", [PlainFile("gatos.jpg")])])])  # Instantiate a plain file
print("-------------------------------------------------------------")
print("Testing question 2")
print(root)
print("-------------------------------------------------------------")
print("Testing question 3")
print(f'file.owner: {file.owner}; folder: {folder.owner}')
file.chown("root")
folder.chown("isaac")
print(f'file.owner: {file.owner}; folder: {folder.owner}')
print("-------------------------------------------------------------")
print("Testing question 4")
root.ls()
print("-------------------------------------------------------------")


class FileSystem:
    def __init__(self, directory):
        """
        :param directory: A directory instantiation
        """
        self.directory = directory
        self.directory_name = self.directory.directory_name  # directory_name equal the name of the instantiation
        self.files = self.directory.files  # files equal the file datails of the instantiation
        self.info_dict = {self.directory_name: self.files}  # Create a dict to store the directory_name
        self.fun_info_dict(self.files)  # Add directory_name

    def fun_info_dict(self, files):  # Add directory_name method
        for i in files:
            try:
                i.files
            except AttributeError:
                continue
            else:
                self.info_dict[i.directory_name] = i.files  # key: directory_name, value:files
                self.fun_info_dict(i.files)  # recursion

    def __repr__(self):
        return str(self.directory_name) + str(self.files)

    def pwd(self):  # Print current directory
        print("'" + self.directory_name + "'")

    def ls(self, retract=""):  # Recursively traverses directories and files
        print(retract + self.directory_name)
        retract += "    "
        for i in self.files:
            try:
                i.files
            except AttributeError:
                print(retract + str(i)[11:-2])
            else:
                i.ls(retract)

    def cd(self, directory):  # Add cd method
        if directory == "..":  # If input "..", go back to a parent directory through match information from info_dict
            for i in self.info_dict:
                for j in self.info_dict[i]:
                    try:
                        j.files
                    except AttributeError:
                        continue
                    else:
                        if self.directory_name == j.directory_name:  # Match by directory_name
                            self.directory_name = i
                            self.files = self.info_dict[i]
        elif directory not in self.info_dict:  # Print not exist
            print("The directory does not exist!")
        else:
            self.directory_name = directory
            self.files = self.info_dict[directory]  # go to the target directory through match information from
            # info_dict
        self.fun_info_dict(self.files)

    def create_file(self, name):  # Add create file method
        if name in self.info_dict:
            print("The directory has already exist within the working directory.")
        else:
            self.files.append(PlainFile(name))  # Add an empty directory
            self.fun_info_dict(self.files)

    def mkdir(self, name, owner="default"):  # Add mkdir method
        p_file_list = []
        for i in self.files:
            try:
                i.files
            except AttributeError:
                p_file_list.append(i.file_name)  # Store existing file names into a collection and check if they exist
            else:
                continue

        if name in p_file_list:
            print("The file has already exist within the working directory.")
        else:
            self.files.append(Directory(name, [], owner))  # Add new plain file
            # self.info_dict[name] = []
            self.fun_info_dict(self.files)

    def rm(self, name):  # Add rm method
        if name not in self.info_dict:  # Check whether the name is a directory or a file by checking whether the name
            # is in the dictionary
            for i in self.files:
                try:  # If i is a plain file
                    i.file_name
                except AttributeError:
                    continue
                else:
                    if name == i.file_name:
                        self.files.pop(self.files.index(i))  # Move file through index
        else:
            for i in self.files:
                try:
                    i.files  # If i is a directory
                except AttributeError:
                    continue
                else:
                    if name == i.directory_name:
                        if not self.files[self.files.index(i)].files:
                        # if self.files[self.files.index(i)].files == []:
                            self.files.pop(self.files.index(i))  # Move directory through index
                        else:
                            print("Sorry, the directory is not empty.")

    def find(self, name):  # Add find method
        path = self.directory_name + "/"
        files = self.files
        path = self.fun_find(path, files, name)  # Execute
        print(path)

    def fun_find(self, path, files, name):  # Implement find method
        for i in files:
            try:  # Check whether it is a file or a directory
                i.file_name
            except AttributeError:
                if name == i.directory_name:
                    return path + name  # Return directory path
                else:
                    path = path + i.directory_name + "/"
                    temp = self.fun_find(path, i.files, name)
                    if temp:
                        return temp
                    path = path[:-len(i.directory_name)-1]
            else:
                if name == i.file_name:
                    return path + name  # Return file path
        return False


print("Testing question 5a: basic filesystem and pwd")
fs = FileSystem(root)
fs.pwd()
print("-------------------------------------------------------------")
print("Testing question 5b: ls in working directory")
fs.ls()
print("-------------------------------------------------------------")
print("Testing question 5c: cd")
# if you try to move to a non existing directory or to a file,
# the method should complain:
fs.cd("casa")
# But you can move to an existing directory in the working directory.
fs.cd("home")
# if we now do ls(), you should only see the content in home:
fs.ls()
print("-------------------------------------------------------------")
print("Testing question 5d:  mkdir and create file")
fs = FileSystem(root)  # re-initialise fs
fs.mkdir("test")  # the owner of the directory should be 'default' as not indicated.  fs.mkdir("test","isaac")
# would set the owner to isaac
fs.cd("test")
fs.create_file("test.txt")
fs.ls()
print("-------------------------------------------------------------")
print("Testing question 5e:  dot dot")
root = Directory("root", [], owner="root")
fs = FileSystem(root)
fs.create_file("boot.exe")  # when creating a file we do not need to indicate owner, it will be the same as
# the working directory
fs.mkdir("test")
fs.cd("test")
fs.create_file("test.txt")
fs.cd("..")
fs.mkdir("home", owner="root")
fs.cd("home")
fs.mkdir("thor", owner="thor")
fs.mkdir("isaac", owner="isaac")
fs.cd("thor")
fs.create_file("hunde.jpg")
fs.create_file("quatsch.txt")
fs.cd("..")
fs.cd("isaac")
fs.create_file("gatos.jpg")
fs.cd("..")
fs.cd("..")
fs.ls()
print("-------------------------------------------------------------")
print("Testing question 5f:  rm")
fs.rm("test")  # shouldn't work!
fs.cd("test")
fs.rm("test.txt")
fs.cd("..")
fs.rm("test")
fs.ls()
print("-------------------------------------------------------------")
print("Testing question 5e:  find")
fs.find("gatos.jpg")
fs.cd("home")
fs.find("boot.exe")  # shouldn't find it!
fs.find("thor")  # should print the relative path "home/thor"
