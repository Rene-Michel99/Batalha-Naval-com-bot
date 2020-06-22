# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:58:32 2020

@author: RENÊ MICHEL
"""
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
import pickle

def create_matriz(arquivo):
    path='C:\\Users\\RENÊ MICHEL\\Desktop\\Codigos\\Python\\Batalha Naval\\'+arquivo
    arq=open(path,'r')
    st=''
    matriz=[]
    classes=[]
    for line in arq:
        if line=='\n':
            continue
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
        new_row=[]
        if row.count(1)>0:
            ini=row.index(1)
            if ini==0:
                new_row=row[ini:ini+6]
            elif ini==1:
                new_row=row[ini-1:ini+5]
            else:
                new_row=row[ini-2:ini+4]
            
            if len(new_row)<6:
                new_row=[0]*(6-len(new_row))+new_row
        else:
            new_row=[0 for _ in range(0,6)]
        soma=sum(new_row)
        new_matriz.append([soma])
        
    return new_matriz,classes

#matriz,cl1=create_matriz('m1.txt')
#matriz2,cl2=create_matriz('m2.txt')
#matriz3,cl3=create_matriz('m3.txt')
#matriz4,cl4=create_matriz('m4.txt')
#matriz5,cl5=create_matriz('m5.txt')
#zero,cl0=create_matriz('zero.txt')

teste,cl_teste=create_matriz('m7.txt')


#data=matriz+matriz2+matriz3+matriz4+matriz5+zero
#cl_data=cl1+cl2+cl3+cl4+cl5+cl0
data,cl_data=create_matriz('Matriz total.txt')


modelo=GaussianNB(var_smoothing=1e-10)
modelo.fit(data,cl_data)

previsoes=modelo.predict(teste)
accuracy_score(cl_teste, previsoes)

confusao = ConfusionMatrix(modelo, classes=[0,1,2,3,4])
confusao.fit(data, cl_data)
confusao.score(teste, cl_teste)
confusao.poof()

with open('C:\\Users\\RENÊ MICHEL\\Desktop\\Codigos\\Python\\Batalha Naval\\nv.pickle','wb')as f:
    pickle.dump((modelo),f)
