import matplotlib.pyplot as plt
import numpy as np

nums=[5, 10, 15,20,25,30,35,40,45,50,55]
#nums= [0.4,0.45,0.5,0.55,0.6,0.65,0.7]
for num in nums:
    print('\n',num)
    fifi = open('C:/MultiScaleMethod/Github/textfiles/Stiffness__NF-'+str(num)+'.txt','r')
    tekst = fifi.read()
    fifi.close()
    lines = tekst.split('\n')
    lines = lines[:-1]
    #print (lines)
    print ('lines',len(lines))
    allparts=[]
    for line in lines:
        parts = line.split('\t\t\t')
        part = parts[1]
        bits = part.split('\t\t')
        alldata=[]
        for bit in bits:
            data = bit.split('\t')
            for dat in data:
                alldata.append(float(dat))
        allparts.append(alldata)
        Ploting = np.zeros([36,len(allparts)])
    print(len(Ploting))
    Xaxis= []
    for par in range(0,len(allparts)):
        Xaxis.append(par+1)
        for ci in range(0,36):
            Ploting[ci][par]=allparts[par][ci]
    print(Ploting[0,:])

    #Cumsum
    Cumavg= np.zeros([36,len(allparts)])
    for csi in range(0, 36):
        for x in range(0,len(Ploting[csi,:])):
            Cumavg[csi][x]=np.sum(Ploting[csi, :][0:(x+1)])/(x+1)


    plt.title('Stiffness convergence for number of fibers in RVEs')
    plt.ylabel('Stiffness matrix constants [GPa]')
    plt.xlabel('Average basis')
    plt.plot(Xaxis, Cumavg[0, :])


    for csi in range(0,36):
        plt.plot(Xaxis,Cumavg[csi,:])
        plt.plot(Xaxis,Ploting[csi,:],'x')
    plt.xlim(0, 25)
    plt.ylim(12.5, 20)
plt.tight_layout()
plt.show()




