import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def plot_3d_data(X_r, y, figsize=(16,16)):
    fig = plt.figure(figsize=figsize)
    ax1 = fig.add_subplot(111, projection='3d')
    for i in range(len(y)):
        if y[i][0] == 1:
            ax1.scatter(X_r[i,0], X_r[i,1], X_r[i,2], c='r', marker='o')
        else:
            ax1.scatter(X_r[i,0], X_r[i,1], X_r[i,2], c='b', marker='o')
    ax1.set_xlabel = '1st Component'
    ax1.set_ylabel = '2nd Component'
    ax1.set_zlabel = '3rd Component'
    plt.show()

def plot_2d_data(X_r, y, figsize=(8,6)):
      plt.figure(figsize=figsize)
      
      for i in range(len(y)):
        if y[i][0] == 1:
            plt.scatter(X_r[i,0], X_r[i,1], color='red', alpha=.8,
                  s=130, edgecolors='k')
        else:
            plt.scatter(X_r[i,0], X_r[i,1],color='blue', alpha=.8,
                  s=130, edgecolors='k')


      plt.title("Red: HoF  <---->  Blue: NoHoF")
      plt.xlabel('1st Dimension')
      plt.ylabel('2nd Dimension')
      
      plt.show()   