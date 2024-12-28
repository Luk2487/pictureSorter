import os
import shutil


class Sorter:

    def __init__(self, folder_input, folder_output, folder_handler):
        self.inp = folder_input
        self.outp = folder_output
        self.folderh = folder_handler

    @staticmethod
    def get_file_year(file_path):
        return int(os.path.getctime(file_path) // 31560000) + 1971

    def sort(self, folder_path):
        temp = os.listdir(folder_path)
        for each in temp:
            if os.path.isdir(folder_path + '/' + each) and self.folderh:
                self.sort(folder_path + '/' + each)
            else:
                self.copy(folder_path + '/' + each)

    def copy(self, file_path):
        temp = self.outp + "/" + str(self.get_file_year(file_path))
        if os.path.exists(temp):
            shutil.copy(file_path, temp)
        else:
            os.mkdir(temp)
            shutil.copy(file_path, temp)

