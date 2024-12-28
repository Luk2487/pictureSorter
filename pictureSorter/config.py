
class Config:

    def __init__(self):
        self.input_folder_path = 'C:/Users/SomeoneLol/Pictures/Saved Pictures'
        self.output_folder_path = 'C:/Users/SomeoneLol/Pictures/plsWorkDumbIdiot'
        self.folder_handling = True
        self.run_input = None
        self.folder_handling_input = None
        self.input_folder_input = None
        self.output_folder_input = None

    def run(self):
        print('\nConfig:\n\nInput Folder: ' + self.input_folder_path +
              '\nOutput Folder: ' + self.output_folder_path +
              '\nFolder Handling: ' + str(self.folder_handling))
        print('\nWhat do you want to change or get info on:\n'
              '(1) Input Folder\n'
              '(2) Output Folder\n'
              '(3) Folder Handler\n'
              '(4) back\n')
        self.run_input = input('>>> ')

        if self.run_input == "1":
            self.input_folder()
        elif self.run_input == "2":
            self.output_folder()
        elif self.run_input == "3":
            self.folder_handler()

    def folder_handler(self):
        print('Whether or not to look inside directories and copy their content more than stupidly copying folders\n'
              'Currently, this value is set to ' + str(self.folder_handling))
        print('What do you want to do:\n'
              '(1) Set to True\n'
              '(2) Set to False\n'
              '(3) Back\n')
        self.folder_handling_input = input('>>> ')

        if self.folder_handling_input == "1":
            self.folder_handling = True
            print('Set to True')
        elif self.folder_handling_input == "2":
            self.folder_handling = False
            print('Set to False')
        print('\n')
        self.run()

    def get_folder_handling(self):
        return self.folder_handling

    def input_folder(self):
        print('The folder files will be taken from:\nCurrently, this is set to: ' + self.input_folder_path +
              '\n \'/\' and \'\\\' are handled')
        print('What do you want to do:\n(1) Change it\n(2) Back\n')
        self.input_folder_input = input('>>> ')

        if self.input_folder_input == "1":
            self.input_folder_path = input('>>> ').replace("\\", "/")
            print('New folder path: ' + self.input_folder_path)
        print('\n')
        self.run()

    def get_folder(self, folder):
        if folder == "input":
            return self.input_folder_path
        else:
            return self.output_folder_path

    def output_folder(self):
        print('The folder directories will be made to sort files:\nCurrently, this is set to: ' + self.output_folder_path +
              '\n \'/\' and \'\\\' are handled')
        print('What do you want to do:\n(1) Change it\n(2) Back\n')
        self.output_folder_input = input('>>> ')

        if self.output_folder_input == "1":
            self.output_folder_path = input('>>> ').replace("\\", "/")
            print('New folder path: ' + self.output_folder_path)
        print('\n')
        self.run()

