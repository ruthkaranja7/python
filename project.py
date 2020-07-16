'''IMAGE PROCESSIING USING SVD DECOMPOSITION

This program analyzes the effects that SVD decomposition has on an
image. An image is composed of pixels, where every pixel is a number 
depicting the color. Hence an image of m by n pixels can be thought of
 as an array of size (m,n). We will use SVD to decompose this array and
filter out some of the information stored in the image.

We will use Python Image Library to enable us to process and view the
image.'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Open image and covert to grayscale for a better view any changes.
#Image was downloaded from http://www.gimp.org/tutorials/Color2BW/
im=Image.open ("myimage.jpg")
imn=im.convert( "L" )
#imn.show() #shows the grayscale image

#Converting to numpy array
A = np.asarray(imn)
#Converting to float
A = A.astype('float')

'''The fundamental concept of the SVD-based image compression scheme is to
 use a smaller number of rank to approximate the original matrix. 
This operation can be expressed as below:
first, let us reconstruct the original matrix with full SVD
Original Image: 	A = USVt,
			where U is M by N,
			      V is M by N,
			      and S = diag(r1, r2,...,rk,0,...,0)
			      (r represents the singular values)'''
M, N = A.shape
U, s, V = np.linalg.svd(A,full_matrices = True)
S = np.zeros(A.shape)
t = min(A.shape)#for an M*N matrix where M>N, the s diagonal matrix has
					   #N*N dimension. N is lesser than M
S[:t, :t] = np.diag(s)
Aorig = np.dot(U, np.dot(S, V))
#Converting back to image
i_mprocessed= Image.fromarray(Aorig)
i_mprocessed.show() #shows original image

#plot of the singular values of A using a log scale:
n = len(s)
#print n
y = np.linspace(-3, 4.5, num = n)
#t = range(1,n+1)
plt.plot(np.log10(s),y)
plt.xlabel('singular values (log10 scale)')
plt.title('Line plot of the singular values of matrix A')
plt.show()

''' Now let us reconstruct the original matrix based on a reduced SVD.
Re-constructed Image:  A1 = US1VH,
			where U is m by k1,
			      V is k1 by n,
			      and S1 = 
			      diag(r1, r2,...,rk1)
	k actually indicates that a certain no of singular values has been 
	removed. We will do the reconstruction for at least 5 different k 
	values and see if there any changes in the image. '''
	
L = range(10,160,30)
#import time			     
for k1 in L[::-1]: #reversing the values to have k in increasing order.
					#This is just a preference for comparison purposes.
	U1, s1, V1 = np.linalg.svd(A, full_matrices=False)
	S1 = np.diag(s1[0:k1+1])
	k = len(s1[k1+1::]) # no. of removed singular values
	Anew = np.dot(U1[:M, :k1+1], np.dot(S1, V1[:k1+1, :N]))
	i_mprocessed1= Image.fromarray(Anew)
	i_mprocessed1.show() #Shows the five reconstructed images
	#time.sleep(2) #This can be turned on to be able to slow down the
				  #image appearance

'''Let us now develop a quantitative metric that could be a measure of 
the image quality. Two commonly used measures are the Mean-Squared Error 
and Peak Signal-to-Noise Ratio. 

 	The 'Mean Squared Error' between the two images is the
	sum of the squared difference between the two images;
	NOTE: the two images must have the same dimension.
	It can be evaluated in the following operations:
	
	MSE = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	MSE /= float(imageA.shape[0] * imageA.shape[1])

	The peak signal-to-noise ratio (PSNR) is an expression for the ratio
	between the maximum possible value (power) of a signal and the power
	of distorting noise that affects the quality of its representation.
	It can be evaluated as follows:
	
	PSNR = -10*np.log10(MSE/(np.max(imageA))**2)'''

#using the same iterations as above, we will measure the image quality 
#of the images produced with different k values

kList = []
psnrList = []

for k1 in L[::-1]: #reversing the values to have k in increasing order
	U1, s1, V1 = np.linalg.svd(A, full_matrices=False)
	S1 = np.diag(s1[0:k1+1])
	k = len(s1[k1+1::]) # no. of removed singular values
	kList.append(k)
	print k
	Anew = np.dot(U1[:M, :k1+1], np.dot(S1, V1[:k1+1, :N]))
	MSE = np.sum((A - Anew) ** 2) #the data had already been converted 
	MSE /= (M * N)				  #to float above
	#print MSE
	PSNR = -10*np.log10(MSE/(np.max(A))**2)
	print PSNR
	psnrList.append(PSNR)
	
#Plotting the metric as a function of k to demonstrate its performance.
plt.plot(kList,psnrList)
plt.xlabel('"k" - the no. removed singular values')
plt.ylabel('PSNR-meausure of image quality')
plt.title('Plot of image quality as a function of removed singular values')
plt.show()
