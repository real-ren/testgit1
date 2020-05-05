# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:25:07 2020

@author: Administrator
"""


# this is pygit test  

import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
#画布设置
plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None)
#字体设置
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
#轴负号设置
plt.rcParams['axes.unicode_minus']= False
#变量设置
x=np.linspace(-5,5,10)
y1=3*x+1
y2=x**2

plt.plot(x,y1,label='一次函数')
plt.plot(x,y2,label='二次函数',linestyle='--',lw=1.5)
plt.legend()
#设置坐标轴标题
plt.xlabel('x轴')
plt.ylabel('y轴',fontsize=10)
#设置坐标轴刻度
plt.xticks(np.linspace(-5,5,9))
#在指定位置展示坐标刻度
plt.yticks([-10,-5,3,8,15,],['很低',r'$bad$',r'$better\ \alpha$',r'$best$','很高'])
#图表标题
plt.title('图表标题',color='r',fontsize=14)
#图例
plt.legend()


#获取图像主干
ax=plt.gca()
#设置图像上、右边框颜色为空
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
#设置左、下边框为主坐标轴
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
#设置移动后的图表坐标轴刻度
ax.spines['bottom'].set_position(('data',0))  #0是交叉点
ax.spines['left'].set_position(('data',0))  #0是交叉点

#被标注的点坐标
x0=1
y0=3*x0+1
###此处annocate是作为复习备注用的，未在下图中体现
plt.annotate(r'$y=2x+1$',#标注内容
             xy=(x0,y0),#被标注的坐标点
             xycoords='data',
             xytext=(30,-30),#标注所在的位置
             textcoords='offset points',  #标注所在的位置方向
             # fontsize = 16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')  #牵引线形式
             )
###
x1=sympy.symbols('x1')
a=sympy.solve([(3*x1+1)-(x1**2)],[x1])
a0=3/2 - math.sqrt(13)/2
a1=3/2 + math.sqrt(13)/2
plt.fill_between(x,y1,y2,where=(y1>=y2), facecolor='purple')
plt.text(3,5,'值域',fontsize=12,c='c')
plt.scatter([a0,a1],[a0**2,a1**2],lw=6,c='r',edgecolors='c',marker='o')
#plt.axhline(y=a1**2,ls='--',c='grey')
#plt.axhline(y=a0**2,ls='--',c='grey')
plt.show()
