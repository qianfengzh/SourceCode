#coding=utf-8
"""
Namede:  Priciple Component Analysis
@Author: Qian Feng
Created: 2016/03/30
"""

'''
PCA 实现：
	1、去除平均值；
	2、计算协方差矩阵；
	3、计算协方差矩阵的特征值和特征向量；
	4、将特征值从大到小排序；
	5、保留最上面的 N 个特征向量；
	6、将数据转换到上述 N 个特征向量构建的新空间中。
'''

import numpy as np

def loadDataSet(filename, delim='\t'):
	with open(filename) as fr:
		stringArr = [line.strip().split(delim) for line in fr.readlines()]
		datArr = [map(float,line) for line in stringArr]
	return np.mat(datArr)

def pca(dataMat, topNfeat=9999999):
	meanVals = np.mean(dataMat, axis=0)
	meanRemoved = dataMat - meanVals  # 去平均值
	covMat = np.cov(meanRemoved, rowvar=0)
	eigVals,eigVects = np.linalg.eig(np.mat(covMat))
	eigValInd = np.argsort(eigVals)
	eigValInd = eigValInd[:-(topNfeat):-1]
	redEigVects = eigVects[:,eigValInd]
	lowDDatMat = meanRemoved * redEigVects
	reconMat = (lowDDatMat * redEigVects.T) + meanVals
	return lowDDatMat, reconMat





def PCA_for_tianchi(dataFrame, topNfeat):
	import numpy as np
	import pandas as pd
	operate_dataFrame = dataFrame.drop(['date','item_id','store_code','cate_id','cate_level_id','brand_id','supplier_id'], axis=1)
	meanVals = operate_dataFrame.mean(axis=0)
	meanRemoved = operate_dataFrame-meanVals
	covDataFrame = meanRemoved.cov()
	covMat = np.mat(covDataFrame.value)
	eigVals, eigVects = np.linalg.eig(covMat)
	eigValInd = np.argsort(eigVals)
	eigValInd = eigValInd[:-(topNfeat):-1]
	redEigVects = eigVects[:,eigValInd]















operate_dataFrame = dataFrame.drop(['date','item_id','store_code','cate_id','cate_level_id','brand_id','supplier_id'], axis=1)
meanVals = operate_dataFrame.mean(axis=0)
meanRemoved = operate_dataFrame-meanVals
covDataFrame = meanRemoved.cov()
covMat = np.mat(covDataFrame.value)
eigVals, eigVects = np.linalg.eig(covMat)
eigValInd = np.argsort(eigVals, reverse=True)
eigSort = sorted(eigVals,reverse=True)
fig=plt.Figure()
plt.plot()









item_store_feature_date = item_store_feature.