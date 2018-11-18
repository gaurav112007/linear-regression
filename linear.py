import numpy as np 
import matplotlib.pyplot as plt 

def coefficient(x, y): 
	#number of observations 
	n = np.size(x) 

	#mean of x and y 
	m_x, m_y = np.mean(x), np.mean(y) 

	#calculating deviation  
	a_xy = np.sum(y*x - n*m_y*m_x) 
	a_xx = np.sum(x*x - n*m_x*m_x) 

	#calculating coefficients 
	b_1 = a_xy / a_xx 
	b_0 = m_y - b_1*m_x 
	return(b_0, b_1) 

def plot_line(x, y, b): 
	#plotting the actual points as scatter plot 
	plt.scatter(x, y, color = "r",marker = "o", s = 80)  		 
	y_pred = b[0] + b[1]*x  
	plt.plot(x, y_pred, color = "b") 
	plt.xlabel('x') 
	plt.ylabel('y') 
	plt.show() 

def main(): 
	
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]) 
	y = np.array([4, 7, 2, 5, 7, 8, 3, 9, 13, 12,11,14,17,19,12,11]) 
	b = coefficient(x, y) 
	print("coefficients:\nb_0 = {} \
                            \nb_1 = {}".format(b[0], b[1])) 
	plot_line(x, y, b) 

if __name__ == "__main__": 
	main() 
