import matplotlib.pyplot as plt

def stats_bar_plot(hall, no_hall, features, row=8, col=6, figsize=(20,20)):
    
    _, axes = plt.subplots(row,col, figsize=figsize)
    ax = axes.ravel()
    i = 0
    for feat_n in features:                  # for each of the features
        bins = 15
        #---plot histogram for each feature---
        ax[i].hist(hall[feat_n], bins=bins, color='r', alpha=.9)
        ax[i].hist(no_hall[feat_n], bins=bins, color='b', alpha=0.4)
        #---set the title---
        ax[i].set_title(feat_n, fontsize=12)    
        #---display the legend---
        ax[i].legend(['hall','no_hall'], loc='best', fontsize=8)
        i +=1

    plt.tight_layout()
    plt.show()