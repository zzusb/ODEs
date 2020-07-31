# -*-coding= utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
import numpy as np


def func(y, t):
    return y-2*t*y

def forward_Euler(x0,y0,N,h):
	# Forward Euler/Explicit time-forward
	x=np.zeros((N+1,1))
	y=np.zeros((N+1,1))
	y[0]=y0
	x[0]=x0
	for i in range(1,N+1):
		x[i]=x0+i*h#here,x==t
		y[i]=y[i-1]+func(y[i-1],x[i-1])*h
	return y

def back_Euler(x0,y0,N,h):
	# Backward Euler/Implicit time-forward
	#预报-校正法
	x=np.zeros((N+1,1))
	y=np.zeros((N+1,1))
	y_=np.zeros((N+1,1))
	x[0]=x0
	y[0]=y0
	y_[0]=y0
	for i in range(1,N+1):
		x[i]=x0+i*h#here,x==t
		y_[i]=y_[i-1]+func(y_[i-1],x[i-1])*h
		y[i]=y[i-1]+func(y_[i],x[i])*h
	return y
if __name__=='__main__':
	# 初始条件
	x0=0
	y0=1
	# x的范围
	xn=2
	# 精度调节
	h=0.01
	N=int((xn-x0)/h)
	#-----------------------------
	# 生成自变量t
	t=np.zeros((N+1,1))
	#----------------------------
	# Explicit solution
	for ii in range(1,N+1):
		t[ii]=x0+ii*h
	t=t.flatten()
	YS=odeint(func,y0=1,t=t)
	#-----------------------------
	y_back=back_Euler(x0,y0,N,h)
	#-----------------------------
	y_for=forward_Euler(x0,y0,N,h)
	# draw
	plt.plot(t,y_for, label='Euler-forward')
	plt.plot(t,y_back, label='Euler-backward')
	plt.plot(t, YS, label='Explicit')
	plt.legend()
	plt.show()

