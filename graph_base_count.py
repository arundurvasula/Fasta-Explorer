import numpy as np
print "Importing matplotlib...",
import matplotlib.pyplot as plt
print "Done."

def graph_base_count(num_a, num_c, num_g, num_t):
    
    N = 4
    countData = (num_a, num_c, num_g, num_t)

    ind = np.arange(N)
    width = 0.5

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, countData, width, color='r')
    
    #add to graph
    ax.set_ylabel('Counts')
    ax.set_title('DNA Base Counts')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('A', 'C', 'G', 'T') )

    #autolabel(rects1)
    plt.show()

def autolabel(rects):
    #attach some labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')

