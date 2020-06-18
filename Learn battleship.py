# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:58:32 2020

@author: RENÊ MICHEL
"""
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
import pickle

def create_matriz(arquivo):
    path='C:\\Users\\RENÊ MICHEL\\Desktop\\'+arquivo
    arq=open(path,'r')
    st=''
    matriz=[]
    classes=[]
    for line in arq:
        st=line.replace('\n','')
        st=st.split()
        matriz.append(st)
    arq.close()
    
    matriz=matriz[1:]
    
    for i in range(0,len(matriz)):
        matriz[i]=matriz[i][1:]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=int(matriz[i][j])
        cl=matriz[i][len(matriz[i])-1]
        classes.append([cl])
        matriz[i]=matriz[i][0:len(matriz[i])-1]
        
    new_matriz=[]
    
    for row in matriz:
        soma=sum(row)
        new_matriz.append([soma])
        
    return new_matriz,classes

matriz,cl1=create_matriz('m1.txt')
matriz2,cl2=create_matriz('m2.txt')
matriz3,cl3=create_matriz('m3.txt')
matriz4,cl4=create_matriz('m4.txt')
matriz5,cl5=create_matriz('m5.txt')
zero,cl0=create_matriz('zero.txt')

teste,cl_teste=create_matriz('m7.txt')


data=matriz+matriz2+matriz3+matriz4+matriz5+zero
cl_data=cl1+cl2+cl3+cl4+cl5+cl0


modelo=GaussianNB()
modelo.fit(data,cl_data)

previsoes=modelo.predict(teste)
accuracy_score(cl_teste, previsoes)

confusao = ConfusionMatrix(modelo, classes=[0,1,2,3,4])
confusao.fit(data, cl_data)
confusao.score(teste, cl_teste)
confusao.poof()

with open(r'C:\Users\RENÊ MICHEL\nv.pickle','wb')as f:
    pickle.dump((modelo),f)