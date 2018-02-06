# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

def radar(country, p, e, s, t):
    # Set data
##    df = pd.DataFrame({
##    'group': ['A','B','C','D'],
##    'var1': [38, 1.5, 30, 4],
##    'var2': [29, 10, 9, 34],
##    'var3': [8, 39, 23, 24],
##    'var4': [7, 31, 33, 14],
##    'var5': [28, 15, 32, 14]
##    })
    df = pd.DataFrame({
        'country': [country],
        'Political Sector': [p],
        'Economical Sector':[e],
        'Socio-cultural Sector':[s],
        'Technological Sector':[t]
        })
     
    # number of variable
    categories=list(df)[:-1]
    N = len(categories)
     
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.loc[0].drop('country').values.flatten().tolist()
    values += values[:1]
    ##values
     
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
     
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
     
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
     
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1,2,3,4,5,6,7,8,9], ["1","2","3","4","5","6","7","8","9"], color="grey", size=7)
    plt.ylim(0,10)
     
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
     
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    ax.legend([country], bbox_to_anchor=(0.99, 0.99))
    plt.show()

