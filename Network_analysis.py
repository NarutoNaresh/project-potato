# https://www.ionos.com/digitalguide/server/tools/introduction-to-netstat/
import os

class NetworkAnalysis:
    def Findactiveports(self):
        # os.system('cmd /c "echo d={}> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
        os.system('cmd /c " echo \"active_ports\"= \> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
        # os.system('cmd /c "echo \'\'\' >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
        os.system('cmd /c "netstat -a >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
        # os.system('cmd /c "echo \'\'\'; >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\""')

        os.system('cmd /c " echo [ active_ports ] >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "netstat -a >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c " echo[ &echo[ &echo[&echo[ >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')

    def Findrunningexe(self):
        os.system('cmd /c "echo di={}> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\runningExe.txt\"')
        os.system('cmd /c " echo di[\"exe_running\"]= \>> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\runningExe.txt\"')
        os.system('cmd /c "echo \'\'\' >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\runningExe.txt\"')
        os.system('cmd /c "netstat -b >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\runningExe.txt\"')
        os.system('cmd /c "echo \'\'\'; >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\runningExe.txt\""')


        os.system('cmd /c " echo [ Executable File ] >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "netstat -b >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "echo[ &echo[ &echo[&echo[ >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')


    def Findpids(self):
        os.system('cmd /c "echo dic={}> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\pids.txt\"')
        os.system('cmd /c " echo dic[\"pids\"]= \>> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\pids.txt\"')
        os.system('cmd /c "echo \'\'\' >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\pids.txt\"')
        os.system('cmd /c "netstat -o >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\pids.txt\"')
        os.system('cmd /c "echo \'\'\'; >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\pids.txt\""')


        os.system('cmd /c " echo [ Process ID\'s ] > \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "netstat -o >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "echo[ &echo[ &echo[&echo[ >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')


    def Findstat(self):
        # os.system('cmd /c "echo dicc={}> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\stat.txt\"')
        # os.system('cmd /c " echo dicc[\"stat\"]= \>> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\stat.txt\"')
        # os.system('cmd /c "echo \'\'\' >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\stat.txt\"')
        os.system('cmd /c "netstat -s > \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\stat.txt\"')

        # os.system('cmd /c "echo \'\'\'; >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\stat.txt\""')

        os.system('cmd /c " echo [ Network-stats ] >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "netstat -s >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "echo[ &echo[ &echo[&echo[ >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')




    def Findroutingtable(self):
        # os.system('cmd /c "echo dicct={}> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\routingTable.txt\"')
        # os.system('cmd /c " echo dicct[\"routing_table\"]= \>> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\routingTable.txt\"')
        # os.system('cmd /c "echo \'\'\' >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\routingTable.txt\"')
        os.system('cmd /c "netstat -r > \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\routingTable.txt\"')
        # os.system('cmd /c "echo \'\'\'; >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\routingTable.txt\""')

        os.system('cmd /c " echo [ Routing Table ] >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "netstat -r >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')
        os.system('cmd /c "echo[ &echo[ &echo[&echo[ >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\Full_analysis.txt\"')


# onb=NetworkAnalysis()
# # onb.Findactiveports()
NetworkAnalysis.Findpids(self=NetworkAnalysis)
NetworkAnalysis.Findroutingtable(self=NetworkAnalysis)






from tkinter import *
from tkinter.ttk import *
# tk=Tk()
# load=Progressbar(tk,orient=HORIZONTAL,length=100,mode='indeterminate')
#
# def bar():
#     import time
#     k=0
#     while k<=100:
#         load['value']=k
#         tk.update_idletasks()
#         time.sleep(.5)
#         k+=20
# def dest():
#     load.stop()
#
# load.pack()
# Button(tk,text='Strt',command=bar).pack()
# Button(tk,text='strop',command=dest).pack()
# mainloop()

#
# os.system('cmd /c "echo d={}>> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
# os.system('cmd /c " echo d[\"active_ports\"]= \>> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
# os.system('cmd /c "echo \'\'\' >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
# os.system('cmd /c "netstat -a >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\"')
# os.system('cmd /c "echo \'\'\'; >> \"C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\Desktop\Project Potato\\bNetwork_analysis\\activePort.txt\""')


# os.system('cmd /c "time /t >>3cmd.txt"')
# os.system('cmd /c " netstat -b > 3cmd.txt"')
# os.system(('cmd /c "echo ----------------------------------------- >>3cmd.txt"'))
# print("hello")

