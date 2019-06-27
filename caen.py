import matplotlib.pyplot as plt
from numpy import fromfile,dtype

def parseBinary(filename, header=True):
    with open(filename, mode='rb') as f:
        if not header:
            return fromfile(f,dtype=dtype("<I"),count=-1)
        d=list(fromfile(f,dtype=dtype("<I"),count=-1))
        trace=[]
        length=1030
        offset=6
        for i in range(len(d)//length):
            trace.append(d[i*length+offset:(i+1)*length])
        return trace
def parseAscii(filename):
    with open(filename,mode='r') as f:
        return [float(n) for n in f.parse().split('\n')[:-1]]
def parse(filename):
    if '.dat' in filename[-4:]: return parseBinary(filename)
    else: return parseAscii(filename)


def checkTruncateOffset(data,truncate,offset):
    if offset >= len(data):
        offset=0
        print("offset %d greater than the size of the dataset %d."%(offset,len(data)))
    truncate=truncate+offset
    if truncate >= len(data) or truncate==-1: truncate=len(data)
    return truncate,offset

def plot(filename,truncate=1000,offset=0):
    data=parse(filename)
    truncate,offset=checkTruncateOffset(data,truncate,offset)
    plt.plot(range(truncate-offset),data[offset:truncate],linestyle='none',marker='.')
    return plt

def plotEvent(data,event=1):
    plt.plot(range(len(data[event])),data[event],linestyle="None",marker=".")
    plt.show()
if __name__=='__main__':
    #data=parseBinary('no_head.dat')
    #print(data[:10])
    data=parseBinary('wave_0.dat',True)
    plotEvent(data,2)
