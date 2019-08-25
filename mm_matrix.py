# -*- coding: utf-8 -*-
'''compute confusion matrix
labels.txt: contain label name.
predict.txt: predict_label true_label
'''
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

'''
数据类型
labels = ['s01','s02','s03','s04','s05']
y_true = [0,1,2,3,4,1,1]
y_pred = [0,4,2,3,4,2,3]
'''
class c_matrix:
    def __init__(self):
        self.labels = list()
        self.y_true = list()
        self.y_pred = list()
    def p_tu(self):
        
        tick_marks = np.array(range(len(self.labels))) + 0.5
        cm = confusion_matrix(self.y_true, self.y_pred)
        np.set_printoptions(precision=2)
        cm_normalized = cm.astype('float')/cm.sum(axis=1)[:, np.newaxis]
        print (cm_normalized)
        plt.figure(figsize=(6,4), dpi=120)
        ind_array = np.arange(len(self.labels))
        x, y = np.meshgrid(ind_array, ind_array)
        for x_val, y_val in zip(x.flatten(), y.flatten()):
            c = cm_normalized[y_val][x_val]
            if (c > 0.01):
                plt.text(x_val, y_val, "%0.2f" %(c,), color='red', fontsize=7, va='center', ha='center')
        plt.gca().set_xticks(tick_marks, minor=True)
        plt.gca().set_yticks(tick_marks, minor=True)
        plt.gca().xaxis.set_ticks_position('none')
        plt.gca().yaxis.set_ticks_position('none')
        plt.grid(True, which='minor', linestyle='-')
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.imshow(cm_normalized, interpolation='nearest', cmap=plt.cm.binary)
        plt.title('Normalized confusion matrix')
        plt.colorbar()
        xlocations = np.array(range(len(self.labels)))
        plt.xticks(xlocations, self.labels, rotation=90)
        plt.yticks(xlocations, self.labels)
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()
        

if __name__ == "__main__":
    labels = [0,2,3,4,1]
    y_true = [0,1,2,3,4,1,1]
    y_pred = [0,4,2,3,4,2,3]
    mm = c_matrix()
    mm.labels=labels
    mm.y_true=y_true
    mm.y_pred=y_pred
    mm.p_tu()
    