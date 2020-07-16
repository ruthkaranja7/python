#this program estimates and compares the values of Pi by Monte Carlo Intergration
#generated using the random number generator and congruential number generator

import random
import matplotlib.pyplot as plt
import numpy
import math

#Part 1
#Using the Random number generator
global buffer #global variable to be called in the main program
buffer=0

def MonteInt(N):
    global buffer 
    pointList=[]   
    
    for i in range (N):
        x1=random.uniform(0,1)
        x2=random.uniform(0,1)
                
        a=(x1**2)+(x2**2)# ensures point a is within 0 and 1 positive quadrant circle
        if a<1:
            pointList.append(a)
                
    k=len(pointList)
    k=float(k)
                  
    Pi=(4.0*k)/float(N) #estimation of number pi
    buffer=Pi   
    
N=[]
for i in range(1,6):
    nvalue=10**i
    N.append(nvalue)
print N

sampleEstList1=[] 
for i in range(15):#creates list of estimates of pi for the first element in N
    MonteInt(N[0])
    sampleEstList1.append(buffer) #appends estimates generated from each iteration to the list
    m1=len(sampleEstList1)
    
bestEstVal1=numpy.mean(sampleEstList1)#calculates the best estimate from the list of estimates using mean
s1=numpy.std(sampleEstList1,dtype=numpy.float64)    
error1=(s1)/math.sqrt((m1)-1)# computing error using standard deviation
 #process is repeated for each of the elements in N
sampleEstList2=[] 
for i in range(15):
    MonteInt(N[1])
    sampleEstList2.append(buffer)
    m2=len(sampleEstList2)
    
bestEstVal2=numpy.mean(sampleEstList2)
s2=numpy.std(sampleEstList2,dtype=numpy.float64)    
error2=(s2)/math.sqrt((m2)-1)

sampleEstList3=[] 
for i in range(15):
    MonteInt(N[2])
    sampleEstList3.append(buffer)
    m3=len(sampleEstList3)
    
bestEstVal3=numpy.mean(sampleEstList3)
s3=numpy.std(sampleEstList3,dtype=numpy.float64)    
error3=(s3)/math.sqrt((m3)-1)  

sampleEstList4=[] 
for i in range(15):
    MonteInt(N[3])
    sampleEstList4.append(buffer)
    m4=len(sampleEstList4)
    
bestEstVal4=numpy.mean(sampleEstList4)    
s4=numpy.std(sampleEstList4,dtype=numpy.float64)     
error4=(s4)/math.sqrt((m4)-1)  

sampleEstList5=[] 
for i in range(15):
    MonteInt(N[4])
    sampleEstList5.append(buffer)
    m5=len(sampleEstList5)
    
bestEstVal5=numpy.mean(sampleEstList5)
s5=numpy.std(sampleEstList4,dtype=numpy.float64)    
error5=(s5)/math.sqrt((m5)-1)   


meanList=[bestEstVal1,bestEstVal2,bestEstVal3,bestEstVal4,bestEstVal5]
errorList=[error1,error2,error3,error4,error5]
print meanList
print errorList

xAxis=[]
for i in N:
    xvalues=math.log10(i)
    xAxis.append(xvalues)
print xAxis
#plotting the graph of the number of iteratiions against best estimates and showing the error
plt.errorbar(xAxis,meanList,yerr=errorList,fmt='o',color='r',label='uniform generator')

#******************************************************************************************************************************
#part 2
#Using the Congruential random number generator
b=0
a=125
M=8192
x_k=1
series=[x_k]
# generateing a series of congruential random numbers
for k in range(100000):
    x_k=(a*(x_k)+b)%M 
    series.append(x_k)

randNList=[]
for i in series:
    randN=float(i)/M #normalizing the random numbers so that they are in the interval(0,1)
    randNList.append(randN)
    
buffer2=0 #global variable that will be used in this part of the program

def MonteInt2(N):
    global buffer2
    pointListA=[]    
    
    for i in range (N):
        xA1=random.choice(randNList)
        xA2=random.choice(randNList)
                
        if (xA1**2)+(xA2**2)<1:
            point=(xA1,xA2)
            pointListA.append(point)
            
    k=len(pointListA)
    k=float(k)
                  
    Pi=(4.0*k)/float(N)
    buffer2=Pi   

#repeating the process as in part 1
sampleEstListA1=[]
for i in range(15):
    MonteInt2(N[0])
    sampleEstListA1.append(buffer2)
    mA1=len(sampleEstListA1)
    
bestEstValA1=numpy.mean(sampleEstListA1)
sA1=numpy.std(sampleEstListA1,dtype=numpy.float64)    
errorA1=(sA1)/math.sqrt((mA1)-1)
 
sampleEstListA2=[] 
for i in range(15):
    MonteInt2(N[1])
    sampleEstListA2.append(buffer2)
    mA2=len(sampleEstListA2)
    
bestEstValA2=numpy.mean(sampleEstListA2)
sA2=numpy.std(sampleEstListA2,dtype=numpy.float64)    
errorA2=(sA2)/math.sqrt((mA2)-1)

sampleEstListA3=[] 
for i in range(15):
    MonteInt2(N[2])
    sampleEstListA3.append(buffer2)
    mA3=len(sampleEstListA3)
    
bestEstValA3=numpy.mean(sampleEstListA3)
sA3=numpy.std(sampleEstListA3,dtype=numpy.float64)    
errorA3=(sA3)/math.sqrt((mA3)-1)  

sampleEstListA4=[] 
for i in range(15):
    MonteInt2(N[3])
    sampleEstListA4.append(buffer2)
    mA4=len(sampleEstListA4)
    
bestEstValA4=numpy.mean(sampleEstListA4)    
sA4=numpy.std(sampleEstListA4,dtype=numpy.float64)     
errorA4=(sA4)/math.sqrt((mA4)-1)  

sampleEstListA5=[] 
for i in range(15):
    MonteInt2(N[4])
    sampleEstListA5.append(buffer2)
    mA5=len(sampleEstListA5)
    
bestEstValA5=numpy.mean(sampleEstListA5)
sA5=numpy.std(sampleEstListA4,dtype=numpy.float64)    
errorA5=(sA5)/math.sqrt((mA5)-1)   


meanListA=[bestEstValA1,bestEstValA2,bestEstValA3,bestEstValA4,bestEstValA5]
errorListA=[errorA1,errorA2,errorA3,errorA4,errorA5]
print meanListA
print errorListA

#plotting
plt.errorbar(xAxis,meanListA,yerr=errorListA,fmt='*',color='g',label='congruential generator')

#defining labels
plt.xlabel('log N')
plt.ylabel('Pi')
plt.legend()
plt.show()
 
#end
#******************************************************************************************************************