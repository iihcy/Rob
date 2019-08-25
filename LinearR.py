# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 15:47:01 2015

@author: Administrator
"""

from sklearn import linear_model
from sklearn.linear_model import ElasticNet 
import numpy as np 
'''
    最小二乘法
'''
class liner :
    def __init__(self ):
        
        self.clf = linear_model.LinearRegression()        
        
    def train (self , X , Y):
                
        self.clf.fit(X , Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
        
    def test (self , input):
        
        self.clf.predict(input)
        

'''
    Ridge回归
'''
class Ridge :
    def __init__(self , alpha):
        
        self.alpha = alpha        
        
        self.clf = linear_model.Ridge(self.alpha)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)
        
'''
    RidgeCV回归
'''
class RidgeCV :
    def __init__(self , alpha , C , V):
        
        self.alpha = alpha
        
        self.C = C

        self.V = V        
        
        self.clf = linear_model.RidgeCV(alphas = np.array[self.alpha,self.C,self.V])
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)


'''
    Lasso回归
'''        
class Lasso :
    def __init__(self , alpha ):
        
        self.alpha = alpha
                       
        self.clf = linear_model.Lasso(self.alpha)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)


'''
    LassoCV回归
'''        
class LassoCV :
    def __init__(self , alpha , C , V):
        
        self.alpha = alpha
        
        self.C = C

        self.V = V        
        
        self.clf = linear_model.LassoCV(alphas = np.array[self.alpha,self.C,self.V])
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)

'''
    ElasticNet回归
'''        
class ElasticNetl :
    def __init__(self , alpha , beta):
        
        self.alpha = alpha
        
        self.beta = beta
               
        self.clf = ElasticNet(alpha = self.alpha , l1_ratio = self.beta)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)

'''
    MultitaskLasso回归
'''        
class MultitaskLasso :
    def __init__(self , alpha):
        
        self.alpha = alpha
                       
        self.clf = linear_model.MultiTaskLasso(alpha = self.alpha)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)
        
'''
   Least Angle Regression
'''        
class LeastAngleRegression :
    def __init__(self , coefs):
        
        self.coefs = coefs
                       
        self.clf = linear_model.Lars(n_nonzero_coefs = self.coefs)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)        
        
'''
    LARS Lasso 
'''        
class LARSLasso  :
    def __init__(self , alpha):
        
        self.alpha = alpha
                       
        self.clf = linear_model.LassoLars(alpha = self.alpha)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)              

'''
    Bayesian Regression 
'''        
class BayesianRegression :
    def __init__(self):
                               
        self.clf = linear_model.BayesianRidge()
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)

'''
    Automatic Relevance Determination 
'''        
class ARD :
    def __init__(self):
                               
        self.clf = linear_model.ARDRegression(compute_score=True)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)

'''
    LogisticRegression
'''        
class LogisticRegression:
    def __init__(self , C):
                               
        self.C = C 
        
        self.clf = linear_model.ARDRegression(C=self.C, penalty='l1', tol=0.01)
        
    def train (self , X ,Y):
        
        self.clf.fit(X,Y)
        
        self.w = self.clf.coef_
        
        self.error = self.clf.intercept_
    
    def test (self , input):
        
        self.clf.predict(input)




           