import config
import sorter

conf = config.Config()


while True:
    print("What do you want to do:\n(1) Config\n(2) Execute\n(3) quit\n")
    inp = input(">>> ")

    if inp == "1":
        conf.run()
    elif inp == "2":
        sort = sorter.Sorter(conf.get_folder('input'), conf.get_folder('output'), conf.get_folder_handling())
        sort.sort(conf.get_folder('input'))
        print('Copied all files from ' + conf.get_folder('input') + ' to ' + conf.get_folder('output'))
    else:
        break
