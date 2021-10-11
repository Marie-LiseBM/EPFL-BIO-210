import matplotlib.pyplot as plt
import itertools
import sklearn.metrics as metrics

import warnings
warnings.filterwarnings("ignore")


def plot(x, y, color, plot_type):
    
    if plot_type == 'line':
        plt.plot(x,y,c=color)
    
    elif plot_type == 'scatter':
        plt.scatter(x,y,c=color)

    elif plot_type == 'confusion_matrix':
        target = x
        labels = y
        label_names = ['0:Malign', '1:Benign']
        matrix = metrics.confusion_matrix(target, labels)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(matrix, vmin=0, vmax=40)
        plt.title('Confusion matrix of Kmeans')
        for i, j in itertools.product(range(matrix.shape[0]), range(matrix.shape[1])):
            plt.text(j, i, "{:,}".format(matrix[i, j]),horizontalalignment="center")
        ax.set_xticklabels([''] + label_names)
        ax.set_yticklabels([''] + label_names)
        plt.xlabel('Predicted by algorithm')
        plt.ylabel('True')
    
    else:
        print('This plot type is not valid :(')
    