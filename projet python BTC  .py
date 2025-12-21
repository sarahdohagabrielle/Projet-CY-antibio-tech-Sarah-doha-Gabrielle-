from matplotlib import pyplot as plt
import math
import random  # jitter
import os # folders managment
import csv # csv files creation
    
cecal_abx = []
cecal_plb = []
ileal_abx = []
ileal_plb = []
fecal_mouse = {} 

# step 1 : path creation
newpath = "output"
if not os.path.exists(newpath):
    os.makedirs(newpath)
newpath = 'images'   
if not os.path.exists(newpath):
    os.makedirs(newpath)
    
#csv files creation 
file_ileal = open('output/ileal.csv', 'w+', newline='', encoding='utf-8')
file_cecal = open('output/cecal.csv', 'w+', newline='', encoding='utf-8')
file_fecal = open('output/fecal.csv', 'w+', newline='', encoding='utf-8')
# creates csv writer
writer_ileal = csv.writer(file_ileal)
writer_cecal = csv.writer(file_cecal)
writer_fecal = csv.writer(file_fecal)


# open csv
file_name = input("Please enter the file name: ")
fd = open("input/"+file_name,"r")

# get csv delimiter 
fd.readline()     
line = fd.readline()
if len(line.split(";"))==11:
      delimiter = ";"
else : 
      delimiter = ","

# step 2 : data processing 
while line != '': # loop until empty line
    line = line.replace("\n", "") #remove newline character and split date
    data = line.split(delimiter)
     
    # variable initialisation 
    sample_type = data[2]
    mouse_id = data[4]
    treatment = data[5]
    experimental_day = int(data[7])
    value = math.log10(float(data[8]) + 1)#log transformation of bacterial count

    #cecal sample 
    if sample_type == 'cecal':
        writer_cecal.writerow(data) 
    
        if treatment == 'ABX':
            cecal_abx.append(value)
        else:
            cecal_plb.append(value)
            
   #ileal sample 
    if sample_type == 'ileal':
        writer_ileal.writerow(data) 
        if treatment == 'ABX':
            ileal_abx.append(value)
        else:
            ileal_plb.append(value)

   #fecal sample 
    if sample_type == 'fecal':
        writer_fecal.writerow(data) 
        if mouse_id not in fecal_mouse:
            # blue for Placebo and orange for ABX
            color = '#ff7f0e' if treatment == 'ABX' else '#1f77b4'
            fecal_mouse[mouse_id] = {'x': [], 'y': [], 'c': color}
        fecal_mouse[mouse_id]['x'].append(experimental_day)
        fecal_mouse[mouse_id]['y'].append(value)
    
    line = fd.readline()
fd.close()
file_ileal.close()
file_cecal.close()
file_fecal.close()

# Step 5 : cecal violin plot
plt.figure(figsize=(6, 5))
v = plt.violinplot([cecal_abx, cecal_plb])

# set colors : ABX (orange) and placebo (blue)
v['bodies'][0].set_facecolor('#ffcc99')
v['bodies'][1].set_facecolor('#6699ff')

# add jittered scatter points 
x_abx = [1 + random.uniform(-0.10, 0.10) for _ in cecal_abx]
x_plb = [2 + random.uniform(-0.10, 0.10) for _ in cecal_plb]
plt.scatter(x_abx, cecal_abx, color='orange', alpha=0.4, s=30, zorder=3)
plt.scatter(x_plb, cecal_plb, color='blue', alpha=0.4, s=30, zorder=3)

plt.title("Cecal live bacteria")
plt.legend(['ABX','Placebo'], loc='lower right')
plt.xlabel("Treatment")
plt.ylabel("log10(live bacteria/wet g)")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.savefig("images/cecal_results.png")

# Step 6 : ileal violin plot 
plt.figure(figsize=(6, 5))
v = plt.violinplot([ileal_abx, ileal_plb])

v['bodies'][0].set_facecolor('#ffcc99')
v['bodies'][1].set_facecolor('#6699ff')

# add jittered scatter points
x_abx = [1 + random.uniform(-0.08, 0.08) for _ in ileal_abx]
x_plb = [2 + random.uniform(-0.08, 0.08) for _ in ileal_plb]
plt.scatter(x_abx, ileal_abx, color='orange', alpha=0.4, s=30, zorder=3)
plt.scatter(x_plb, ileal_plb, color='blue', alpha=0.4, s=30, zorder=3)

plt.title("Ileal live bacteria")
plt.legend(['ABX','Placebo'], loc='lower right')
plt.xlabel("Treatment")
plt.ylabel("log10(live bacteria/wet g)")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.savefig("images/ileal_results.png")

# Step 7 : fecal time-course plot
plt.figure(figsize=(8, 6))
for name in fecal_mouse:
    infos = fecal_mouse[name]
    plt.plot(infos['x'], infos['y'], color=infos['c'], alpha=0.4)
plt.legend(['placebo','ABX'], loc='upper right')
plt.title("Fecal live bacteria")
plt.xlabel("washout day")
plt.grid(linestyle='--', alpha=0.3)
plt.ylabel("log10(live bacteria/wet g)")
plt.savefig("images/fecal_results.png")

plt.show()

