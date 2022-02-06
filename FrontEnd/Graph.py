import pyodbc
import matplotlib.pyplot as plt
import Marks

class Graph(object):
    """description of class"""


if __name__=='__main__':
    x1=[1,2,3,4,5,6]

    y1=[2,4,1,5,2,6]

    plt.plot(x1,y1, label="line 1", linestyle='dashed', markerfacecolor='blue', markersize=12, marker='o')

    plt.ylim(0,10)
    plt.xlim(0,10)

    plt.xlabel('Student')

    plt.ylabel('Marks')
    
    plt.title('Graph')

    plt.show()
