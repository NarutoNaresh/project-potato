import os
from tkinter import *
import platform
import socket
import re
import uuid
import Network_analysis
from aFile_analysis import Fileanalysis as Fa
from aFile_analysis import HiddenFinder as Hi
from dReport_analysis import Report as Rep
from tkinter import messagebox

class software():
    def __init__(self,window):
        self.window=window
        # self.photo = PhotoImage(file="set.png")
        # self.s = self.photo.subsample(1, 1)
        self.intro='''Hey all !!!!\nWelcome to the NSN cyber forensic tool.\nThis tool has many great features to explore.\nBe sure to explore all of them and feel free to use them.\nJust plug into the system, click on the button, and then wait for a few seconds.\nOur tool will do the work for you. 
                    '''
        self.var=None
        self.sys_info=None
        self.canvas = Canvas(window, width=656, height=900, bg='black',scrollregion=(0,0,700,9000))#7665ff
        hbar=Scrollbar(window,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(window,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=RIGHT)

        # canvas=Canvas(frame,bg='pink',width=900,height=900)
        window.title("Yenga Tool da...!")
        window.geometry("780x591")
        window.configure(background="#393e46")

        self.canvas.create_text(350, 50, fill="DeepPink2", text="Forensic Analyser Tool ", font='Helvetica 40 bold')
        self.canvas.create_text(330, 200, fill="Cyan2", text=self.intro, font='Helvetica 11 bold')
        self.canvas.create_text(480, 460, fill="white", text="Credits\n\nD Naresh kumar\nSidharth V\nM.Naaga Boi", font='Helvetica 10 bold')
        os.chdir('C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato')
        print(os.getcwd())
        print("im inside init....")

    def hello(self):

        # c = Canvas(window, bg='#393e46', height=250, width=300, cursor='circle')
        self.canvas.delete('all')
        self.canvas.create_text(350, 50, fill="green", text="Hello_", font='Helvetica 40 bold')
        # line = c.create_line(10, 20, 200, 200, fill='black')
        # c.pack()
        # canvas = Canvas(window, width=676, height=584, bg='#d83ab0')
        # canvas.create_text(130, 10, fill="darkblue", text="Click the bubbles that are multiples of two.")
        # canvas.pack()
    #     # c.delete("all")
    #     # print(self.var)
    def Nwanalysis(self):
        self.canvas.delete('all')

        # cont='\n'*280
        cont=''
        Network_analysis.NetworkAnalysis.Findpids(self=Network_analysis)
        Network_analysis.NetworkAnalysis.Findroutingtable(self=Network_analysis)
        Network_analysis.NetworkAnalysis.Findstat(self=Network_analysis)
        Network_analysis.NetworkAnalysis.Findactiveports(self=Network_analysis)
        Network_analysis.NetworkAnalysis.Findrunningexe(self=Network_analysis)
        self.canvas.create_text(350, 80, fill="Green2", text="Network Analysis",font='Helvetica 40 bold')
        file =open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\bNetwork_analysis\\Full_analysis.txt",'r')
        for f in file:
            cont+="\t"+f
        self.canvas.create_text(350, 150,fill="white", text=cont, font='Helvetica 10 bold',anchor=N)

    def RepGen(self):
        cont='\n'*5
        self.canvas.delete('all')
        self.canvas.create_text(350, 80, fill="yellow2", text="Report Generation",font='Helvetica 40 bold')
        self.canvas.create_text(350, 140, fill="white", text="Generated Reports are shown in pictorial form.",font='Helvetica 20 bold')
        self.canvas.create_text(150, 180, fill="orange", text="Hashing Done.",font='Helvetica 20 bold')
        Rep.Genreport.my_hasher(self=Rep)
        print("yoooo!")
        hashfile=open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\eHashes\\hashed.txt", 'r',encoding='utf-8')
        for line in hashfile:
            cont+=line
        self.canvas.create_text(200, 250, fill="white", text=cont,font='Helvetica 12 bold')

        Rep.Genreport.netdet(self=Rep)

    def Inci(self):
        self.canvas.delete('all')
        self.canvas.create_text(350, 80, fill="hot pink", text="Incident Handler",font='Helvetica 40 bold')
        self.canvas.create_text(350, 140, fill="white", text="0 Wrong Login attempt made till now.",font='Helvetica 20 bold')
        # self.canvas.create_text(350, 150,fill="white", text=" 0 Wrong Login attempt made till now.", font='Helvetica 10 bold',justify=LEFT,anchor=N)


    def FLanalysis(self):
        cont2=''
        self.canvas.delete('all')
        self.canvas.create_text(350, 50, fill="Blue2", text="File Analysis",font='Helvetica 40 bold')
        Fa.Fileana.Collect_history(self=Fa)
        self.canvas.create_text(350, 140, fill="white", text="\n\n\nAcquired Victim's Browser History \n Logged in File Analysis directory\n\n\n",font='Helvetica 20 bold')
        Hi.Find.Show(self=Hi)
        file2 =open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\aFile_analysis\\Hiddens.txt",'r')
        for f in file2:
            cont2+=f
        self.canvas.create_text(350, 180,fill="white", text=cont2, font='Helvetica 11 bold',justify=LEFT,anchor=N)

    def System_info(self):
        s=110
        self.canvas.delete('all')
        self.sys_info={}
        self.sys_info['Hostname'] = socket.gethostname()
        self.sys_info['Platform'] = platform.system()
        self.sys_info['Platform-release'] = platform.release()
        self.sys_info['IP-address'] = socket.gethostbyname(socket.gethostname())
        self.sys_info['Mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.sys_info['Platform-version'] = platform.version()
        self.sys_info['Architecture'] = platform.machine()
        self.sys_info['Processor'] = platform.processor()

        sysfile =open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\1SystemInfo\\SystemInfo.txt", 'w+')
        self.canvas.create_text(350, 50, fill="red", text="System Information",font='Helvetica 40 bold')
        for i, j in zip(self.sys_info.keys(), self.sys_info.values()):
            sysfile.write(f"{i} : {j} \n\n")
        sysfile =open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\1SystemInfo\\SystemInfo.txt", 'r')
        for line in sysfile:
            self.canvas.create_text(350, s, fill="white", text=(line),font=('Helvetica 14 bold') ,justify=LEFT)
            s+=25
        # print("HELLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLo!")
        print(sysfile.readline())
        # print("sdfsfsdfsfsdfsdfsdf")
        self.canvas.pack(side=RIGHT)


    def Buttons(self):

        self.b_sysinfo = PhotoImage(file="inf.png")
        self.b_s=self.b_sysinfo.subsample(6,6)

        # b1 = Button(window, text="System Info", relief=FLAT, bg="#020423", fg="#4ecca3", bd=5,
        #             command=self.System_info(), image=self.b_s, compound=TOP).place(x=30, y=98)
        b1 = Button(window, text="System Info", relief=FLAT, bg="#020423", fg="#4ecca3", bd=5,
                    command=self.System_info, image=self.b_s, compound=TOP).place(x=0, y=0)


        self.b_file = PhotoImage(file="file.png")
        self.b_f = self.b_file.subsample(6, 6)
        b2 = Button(window, text="FileAanlysis", relief=FLAT, bg="#020423", fg="#4ecca3", bd=5,
                    command=self.FLanalysis, image=self.b_f, compound=TOP).place(x=0, y=118)

        self.b_net = PhotoImage(file="net.png")
        self.b_n = self.b_net.subsample(6, 6)
        b3 = Button(window, text="N/w Aanalysis", relief=FLAT, bg="#020423", fg="#4ecca3", bd=5,
                    command=self.Nwanalysis, image=self.b_n, compound=TOP).place(x=0, y=236)

        self.b_ins = PhotoImage(file="scn.png")
        self.b_i = self.b_ins.subsample(6, 6)
        b4 = Button(window, text="Inc_Handling", relief=FLAT, bg="#020423", fg="#4ecca3", bd=5,
                    command=self.Inci, image=self.b_i, compound=TOP).place(x=0, y=354) #2C2828

        self.b_rep = PhotoImage(file="stats.png")
        self.b_r = self.b_rep.subsample(6, 6)
        b4 = Button(window, text="Report", relief=FLAT, bg="#020423", fg="#4ecca3", bd=5,
                    command=self.RepGen, image=self.b_r, compound=TOP).place(x=0, y=472)



        #
        # b4 = Button(window, text="Report", height=6, width=14, relief=FLAT, bg="#2C2828", fg="#4ecca3", bd=5,
        #             command=self.hello).place(x=0, y=324)
        # b4 = Button(window, text="Settings", height=6, width=14, relief=FLAT, bg="#2C2828", fg="#4ecca3", bd=5,
        #             command=self.hello1).place(x=0, y=432)


window=Tk()



a=software(window)
a.Buttons()
window.mainloop()
