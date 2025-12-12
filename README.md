# Projet-CY-antibio-tech-Sarah-doha-Gabrielle-
On étudie comment un traitement antibiotique donné à des souris au début de leur vie influence leur microbiote, en comparant un groupe traité avec un antibiotique à un groupe témoin recevant un placebo

from matplotlib import pyplot as plt 
import math

figure, axes,=plt.subplots()

N_mice=16

#for mouse_id in mice :
for i in range(1,N_mice+1):
    mouse_id='00'+str(i)
    mouse_id=mouse_id[-3:]
    mouse_id='ABX'+ mouse_id
    treatment='?'
    x=[]
    y=[]
    fp=open('data_small.csv')
    #remove first line
    line=fp.readline()
    #get read of 1st data line
    line=fp.readline()
    while line!='':
        line=line.replace('\n','')
        data=line.split(';')
        if len(data)==11:
            #process to retrieve mouse data
            if data[4]==mouse_id:
                vx=int(data[7])
                vy=math.log10(float(data[8]))
                print(line)
                #add x and y
                x.append(vx)
                y.append(vy)
                #retrieve treatment
                treatment=data[5]
        #get next line
        line=fp.readline()           
    fp.close()
    clr="#0000FF"
    if treatment =="ABX" :
        clr = "#FF0000"
    axes.plot(x, y, label=mouse_id, color=clr ,alpha=0.5)
    
    
figure.legend(loc='right')
figure.savefig("out.png", dpi=150))
figure.savefig("out.png")
