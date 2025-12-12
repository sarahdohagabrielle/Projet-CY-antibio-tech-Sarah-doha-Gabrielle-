# Projet-CY-antibio-tech-Sarah-doha-Gabrielle-
On étudie comment un traitement antibiotique donné à des souris au début de leur vie influence leur microbiote, en comparant un groupe traité avec un antibiotique à un groupe témoin recevant un placebo

from matplotlib import pyplot as plt 
import math
figure, axes,=plt.subplots()
N_mice=16


figure,axes=plt.subplots() 


for i in range(1,N_mice+1):
    mouse_id='00'+str(i)
    mouse_id=mouse_id[-3:]
    mouse_id='ABX'+ mouse_id
    treatement='?'
    x=[]
    y=[]
    fp=open('data_small.csv')
    line=fp.readline()
    line=fp.readline()
    while line!='':
        line=line.replace('\n','')
        data=line.split(';')
        if len(data)==11:
            if data[4]==mouse_id:
                vx=int(data[7])
                vy=math.log10(float(data[8]))
                print(line)
                x.append(vx)
                y.append(vy)
                treatement=data[5]
        line=fp.readline()           
    fp.close()
    axes.plot(x,y,label=mouse_id,color='#FF8020',alpha=0.5)
    
    
figure.legend(loc='right')
figure.savefig("out.png")
