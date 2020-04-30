import sys
import matplotlib.pyplot as plt
import subprocess

args = sys.argv # 読み込みファイル名の取得
FILES = args[1:] # ファイル名の格納

def NOL(fname): #Number of lines
    num_lines = sum(1 for line in open(fname))
    return num_lines

def getData():
    x, y = [], []
    print("データ読み込み")
    for file_in in FILES:
        tmp_x, tmp_y = [], []
        with open(file_in,"r") as f:
            for i in range(NOL(file_in)):
                lines = f.readline().split(" ")
                try:
                    tmp_x.append(float(lines[0]))
                    tmp_y.append(float(lines[1]))
                except Exception:
                    continue
        x.append(tmp_x)
        y.append(tmp_y)

    name = input("GraphName: ")
    xlabel = input("xlabel: ")
    ylabel = input("ylabel: ")
    xr = input("Xrange: ")
    xr = xr.split(" ")
    yr = input("Yrange: ")
    yr = yr.split(" ")
    # 画像出力
    print("画像出力")
    plot_graph(name,x,y,float(xr[0]),float(xr[1]),float(yr[0]),float(yr[1]),xlabel,ylabel)
    return name
    
def plot_graph(name,x,y,sx,ex,sy,ey,xlabel,ylabel):
    plt.xlim(sx,ex)
    plt.xlabel(str(xlabel))
    plt.ylim(sy,ey)
    plt.ylabel(str(ylabel))
    for i in range(len(x)):
        plt.plot(x[i],y[i], label=FILES[i].split("/")[3])#markersize=0.5)
    plt.legend()
    plt.savefig("./"+str(name)+".pdf")
    plt.delaxes()

def openGraph(name):
    cmd = ["open", str(name)+".pdf"]
    subprocess.check_call(cmd)

if __name__ == "__main__":
    name = getData()
    if(input("画像を表示しますか(Y or N): ")=="y"):
        openGraph(name)
