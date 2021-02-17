import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import hashlib as hsl

class Genreport :
    def __init__(self):
        pass
    def my_hasher(self):
        a=open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\1SystemInfo\\SystemInfo.txt", 'r',encoding='utf-8')
        abuffer=a.read()
        b=open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\aFile_analysis\\Hiddens.txt",'r',encoding='utf-8')
        bbuffer=b.read()
        c=open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\bNetwork_analysis\\Full_analysis.txt",'r',encoding='utf-8')
        cbuffer=c.read()

        hashfile=open("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Project Potato\\eHashes\\hashed.txt", 'w+',encoding='utf-8')
        hashfile.write("Hash of System info log \n")
        hashfile.write(hsl.md5(abuffer.encode('utf-8')).hexdigest())
        hashfile.write("\n\n")
        hashfile.write("Hash of Fileanalysid log \n")
        hashfile.write(hsl.md5(bbuffer.encode('utf-8')).hexdigest())
        hashfile.write("\n\n")
        hashfile.write("Hash of Networkanalysis log \n")
        hashfile.write(hsl.md5(cbuffer.encode('utf-8')).hexdigest())
        hashfile.close()



    def netdet(self):

        df =pd.read_csv("C:\\Users\\NARESH DANIEL .LAPTOP-16702FGF\\Desktop\\Forensics\\net.csv")
        df.head(10)

        req=df['IPv4 Statistics']
        req=pd.DataFrame(req)
        req['value']=df['Unnamed: 2']
        req.dropna(axis=0,how='any')

        req.head(10)

        total_packet_received=int(req.loc[1][1])
        packet_Discarded=int(req.loc[6][1])
        ipv4_Active_Opens=int(req.loc[81][1])
        ipv4_Passive_Opens=int(req.loc[82][1])
        ipv4_Failed_Connection=int(req.loc[83][1])
        ipv4_Reset_Connections=int(req.loc[84][1])
        ipv4_Current_Connections=int(req.loc[85][1])
        ipv4_Segments_Received=int(req.loc[86][1])
        ipv4_Segments_Sent=int(req.loc[87][1])
        ipv4_Segments_Retransmitted=int(req.loc[88][1])

        sizes=[total_packet_received,
        packet_Discarded,
        ipv4_Active_Opens,
        ipv4_Passive_Opens,
        ipv4_Failed_Connection,
        ipv4_Reset_Connections,
        ipv4_Current_Connections,
        ipv4_Segments_Received,
        ipv4_Segments_Sent,
        ipv4_Segments_Retransmitted]

        lables="total_packet_received",
        "packet_Discarded",
        "ipv4_Active_Opens",
        "ipv4_Passive_Opens",
        "ipv4_Failed_Connection",
        "ipv4_Reset_Connections",
        "ipv4_Current_Connections",
        "ipv4_Segments_Received",
        "ipv4_Segments_Sent",
        "ipv4_Segments_Retransmitted"
        print(type(ipv4_Active_Opens))



        x=["total_packet_received","packet_Discarded",
        "ipv4_Active_Opens",
        "ipv4_Passive_Opens",
        "ipv4_Failed_Connection",
        "ipv4_Reset_Connections",
        "ipv4_Current_Connections",
        "ipv4_Segments_Received",
        "ipv4_Segments_Sent",
        "ipv4_Segments_Retransmitted"]

        y=[total_packet_received,
        packet_Discarded,
        ipv4_Active_Opens,
        ipv4_Passive_Opens,
        ipv4_Failed_Connection,
        ipv4_Reset_Connections,
        ipv4_Current_Connections,
        ipv4_Segments_Received,
        ipv4_Segments_Sent,
        ipv4_Segments_Retransmitted]

        x_pos = [i for i, _ in enumerate(x)]
        plt.figure(figsize=(8,4))
        plt.bar(x_pos, y, color='green')
        plt.xlabel("Information")
        plt.ylabel("No.of Packets ")
        plt.title("Network Stats of Ipv4 TCP")
        plt.ylim(0,20000)
        plt.xticks(x_pos, x,rotation=70)

        y_pos = np.arange(len(x))
        plt.bar(y_pos, y, color=['black', 'red', 'green', 'blue', 'cyan','yellow', 'pink', 'orange', 'white', 'purple'])

        plt.show()

a =Genreport
a.netdet(self=a)
