import numpy as np
import matplotlib.pyplot as plt
#Defino la función que encuentra los parametros beta
def least(n,m,data):
    trdata=data[0:n,:]
    matx=np.zeros((n,m))
    for i in range(n):
        for i2 in range(m):
            matx[i,i2]=trdata[i,0]**i2    
    b=np.linalg.pinv(matx) @ trdata[:,1] 
    return b
#Defino la función que construye los valores para y del modelo
def y_model(b):
    x=np.linspace(0,1,100)
    y=[sum(b[j]*(i**j) for j in range(b.shape[0])) for i in x]
    return y
#Función que encuentra el error entre los datos del modelo y los datos reales en cierto rango
def err(data,ni,nf,b):
    x=data[ni:nf+1,0]
import numpy as np
import matplotlib.pyplot as plt
#Defino la función que encuentra los parametros beta
def least(n,m,data):
    trdata=data[0:n,:]
    matx=np.zeros((n,m))
    for i in range(n):
        for i2 in range(m):
            matx[i,i2]=trdata[i,0]**i2    
    b=np.linalg.pinv(matx) @ trdata[:,1] 
    return b
#Defino la función que construye los valores para y del modelo
def y_model(b):
    x=np.linspace(0,1,100)
    y=[sum(b[j]*(i**j) for j in range(b.shape[0])) for i in x]
    return y
#Función que encuentra el error entre los datos del modelo y los datos reales en cierto rango
def err(data,ni,nf,b):
    x=data[ni:nf+1,0]
    y=data[ni:nf+1,1]
    error=1/2 *sum(np.power([sum(b[j]*(i**j) for j in range(b.shape[0])) for i in x]-y,2))
    erms=np.sqrt(2*error/(nf-ni))
    return erms
#Cargo los datos
data=np.loadtxt("numeros_20.txt")
#Defino cantidad de datos usados para el entrenamiento
n=10
#Defino el rango máximo con el que quiero hacer el ajuste
rm=10
fig=plt.figure(figsize=(15,40))
errt=np.zeros(rm)
errte=np.zeros(rm)
for i in range(rm):
    plt.subplot(int(rm/2)+1,2,i+1)
    m=i+1
    b=least(n,m,data)
    errt[i]=err(data,0,n-1,b)
    errte[i]=err(data,n,20,b)
    y=y_model(b)
    plt.plot(data[0:15,0],data[0:15,1],"o")
    plt.plot(np.linspace(0,1,100),y)
    plt.ylim(0,2)
    plt.title("M="+str(m-1))
    plt.xlabel("x")
    plt.ylabel("y")
#Puedo escoger hasta que grado graficar ya que en los grados mas altos el error es muy grande
Mmax=10
ymax=max(errte[0:Mmax+1])
plt.figure()
plt.plot(np.linspace(0,rm-1,rm),errt,"-bo")
plt.plot(np.linspace(0,rm-1,rm),errte,"-ro")
plt.legend(["Training","Test"])
plt.xlabel("M")
plt.ylabel("ERMS")
plt.xlim(0,Mmax)
plt.ylim(-0.4,ymax*1.1)
