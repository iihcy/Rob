# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:28:51 2016

@author: Administrator
"""

import numpy as np
import numpy.random as r
import sklearn.metrics as m
import pylab as pl

class proc:
    def __init__(self):
        self.y_true = list()
        self.y_pred = list()
        self.labels = list()
    
    def mroc(self):
        y_true = np.array(self.y_true)
        y_pred = np.array(self.y_pred)
        #self.rocv = m.classification_report(y_true, y_pred)
        #print self.recall
        num=0
        for lab in self.labels:
            num = num+1
            precision, recall, th = m.precision_recall_curve(y_true, y_pred, pos_label=lab)
    
            ax = pl.subplot(len(self.labels), 1, num)
            ax.plot(recall, precision)
            ax.set_ylim([0.0, 1.0])
            ax.set_title('Precision ['+str(lab)+'] recall curve')
        pl.show()

if __name__ == '__main__':
    size = 50
    y_true = ([ 5 if i >= 0.3 else 2 for i in r.random(size) ])
    print (y_true)
    y_pred = ([ 5 if i >= 0.3 else 2 for i in r.random(size) ])
    oc = proc()
    oc.y_true = y_true
    oc.y_pred = y_pred
    oc.mroc(2)
    
    