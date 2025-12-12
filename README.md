# Projet-CY-antibio-tech-Sarah-doha-Gabrielle-
On étudie comment un traitement antibiotique donné à des souris au début de leur vie influence leur microbiote, en comparant un groupe traité avec un antibiotique à un groupe témoin recevant un placebo

from matplotlib import pyplot as plt
import math


figure, axes,=plt.subplots()

N_mice=16
# graphique 1
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
# liste violon 
cecal_no  = []
cecal_abx = []
ileal_no  = []
ileal_abx = []

fp = open('data_small.csv')
fp.readline()  # skip header
line = fp.readline()

while line != '':
    line = line.replace('\n', '')
    data = line.split(';')

    if len(data) == 11:
        sample_type = data[2].strip().lower()   # cecal / ileal
        treatment   = data[5]
        val = float(data[8])

        if val > 0:
            vy = math.log10(val)

            if sample_type == "cecal":
                if treatment == "ABX":
                    cecal_abx.append(vy)
                else:
                    cecal_no.append(vy)

            elif sample_type == "ileal":
                if treatment == "ABX":
                    ileal_abx.append(vy)
                else:
                    ileal_no.append(vy)

    line = fp.readline()

fp.close()

# graphique 2 
fig_cecal, ax_cecal = plt.subplots()
ax_cecal.violinplot([cecal_no, cecal_abx], showmedians=True)

ax_cecal.set_xticks([1, 2])
ax_cecal.set_xticklabels(["No ABX", "ABX"])
ax_cecal.set_ylabel("log10(live bacteria / wet g)")
ax_cecal.set_title("Cecal live bacteria")

fig_cecal.tight_layout()
fig_cecal.savefig("violin_cecal.png", dpi=150)


#grafique 3
fig_ileal, ax_ileal = plt.subplots()
ax_ileal.violinplot([ileal_no, ileal_abx], showmedians=True)

ax_ileal.set_xticks([1, 2])
ax_ileal.set_xticklabels(["No ABX", "ABX"])
ax_ileal.set_ylabel("log10(live bacteria / wet g)")
ax_ileal.set_title("Ileal live bacteria")

fig_ileal.tight_layout()
fig_ileal.savefig("violin_ileal.png", dpi=150)

plt.show()


