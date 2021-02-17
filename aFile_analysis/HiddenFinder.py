import os

class Find:
    def __init__(self):
        pass
    def Show(self):
        os.system('cmd /c "echo Hidden Files and Folers in D drive : > \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\aFile_analysis\\Hiddens.txt\"')
        # os.system('cmd /c d: && dir   >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\aFile_analysis\\Hiddens.txt\" ')
        os.chdir('d:')
        os.system('cmd /c attrib -s -h -r /s /d *.*   >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\aFile_analysis\\Hiddens.txt\" ')

a=Find
a.Show(self=a)