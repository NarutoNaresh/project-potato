import os
class Fileana:
    def Collect_history(self):
        print("Iam from File analysis folder")
        # C:\Users\NARESH DANIEL .LAPTOP-16702FGF\AppData\Local\Google\Chrome\User Data\Default
        cmd="C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History" "C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\Project Potato\\aFile_analysis\\Victim_Browser_History"
        os.system('cmd /c copy "C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History" "C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\Project Potato\\aFile_analysis\\Victim_Browser_History"')




