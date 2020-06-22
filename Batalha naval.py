import pickle

class Matriz:
    def __init__(self,name):
        self.name=' ___________________________________________\n|               '+name+' '*(28-len(name))+'|'
        self.identifier=' ___________________________________________           ___________________________________________\n|               '+name+' '*(28-len(name))+'|'+'         |                 '+'Esquadra Inimiga'+' '*(26-len('Esquadra Inimiga'))+'|'
        self.matriz=[['  ','A','B','C','D','E','F','G','H','I','J','K','L','M','N']]
        self.m_check=[['  ','A','B','C','D','E','F','G','H','I','J','K','L','M','N']]
        self.map_navios=[]
        for i in range(0,15):
            if i+1<=9:
                self.matriz.append([' '+str(i+1),'▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒'])
                self.m_check.append([' '+str(i+1),'▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒'])
            else:
                self.matriz.append([str(i+1),'▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒'])
                self.m_check.append([str(i+1),'▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒'])

    def draw(self):
        print(self.name)
        for row in self.matriz:
            for col in row:
                print(col,' ',end='')
            print()

    def create_arq(self):
        arq=open('Matriz.txt','w',encoding='utf-8')
        for row in self.matriz:
            for col in row:
                arq.write(col+' ')
            arq.write('\n')
        arq.close()

    def count_erros(self):
        count=0
        for row in self.m_check:
            for col in row:
                if col=='N':
                    count+=1
        return count
    
    def draw_two(self):
        print(self.identifier)
        for row1,row2 in enumerate(self.matriz):
            for col1 in row2:
                print(col1,' ',end='')
            print('        ',end='')
            for col2 in self.m_check[row1]:
                print(col2,' ',end='')
            print()
    
    def map_navs(self):
        for row in self.matriz:
            soma=0
            for col in row:
                if col=='█':
                    soma+=1
            self.map_navios.append(soma)

    def verify_lose(self):
        cont=0
        for i,row in enumerate(self.matriz):
            soma=0
            for col in row:
                if col=='X':
                    soma+=1
            if i==len(self.map_navios):
                break
            if soma==self.map_navios[i]:
                cont+=1

        if cont==len(self.map_navios):
            return True
        else:
            return False


    
    def verify_pos(self,location):
        x=self.matriz[0].index(location[0])
        y=location[1]

        if self.matriz[y][x]=='█':
            return True
        else:
            return False

    def get_erro(self,location):
        x=self.matriz[0].index(location[0])
        y=location[1]

        self.m_check[y][x]='N'

    def kill_pos(self,location):
        x=self.matriz[0].index(location[0])
        y=location[1]

        self.matriz[y][x]='X'

    def insert_on_mcheck(self,location):
        x=self.m_check[0].index(location[0])
        y=location[1]
        if x==0:
            x=1
        if y==0:
            y=1
        self.m_check[y][x]='X'
    
    def insert(self,navio,location,rotate):
        x=self.matriz[0].index(location[0])
        y=location[1]

        if x==16:
            x=15
        if y==16:
            y=15
        if x==0:
            x=1
        if y==0:
            y=1
        tipo=navio[1]
        navio=navio[0]
        
        normal=['couraçado','cruzador','destroyer']
        if tipo in normal:
            end=len(navio)          
            if y<=1 and rotate>=90:
                end=end+1
            elif rotate>=90 and y>=15:
                y=16-len(navio)
                end=16
            elif rotate>=90 and y>1:
                navio+=navio
            elif rotate==0 and x+len(navio)>15:
                x=15-len(navio)
            
            if rotate==0:
                self.matriz[y][x:len(navio)+x]=navio 
            else:
                for i in range(y,end):
                    self.matriz[i][x]=navio[0]
        elif tipo=='submarino':
            if x+2>15:
                x=15-2
            if y+2>15:
                y=15-1
            self.matriz[y][x]=navio[0]
            self.matriz[y][x+1]=navio[0]
            self.matriz[y+1][x]=navio[0]
            self.matriz[y+1][x+1]=navio[0]
        elif tipo=='hidroaviao':
            if rotate==0 or rotate==180:
                if x<=1:
                    x=2
                if x+3>15:
                    x=15-2
                if y+2>15:
                    y=15-1
            elif rotate==90 or rotate==270:
                if x<=1 and rotate==270:
                    x=2
                if y-1==0:
                    y+=1
                if x+2>15 and rotate==90:
                    x=15-2
                if y+3>15:
                    y=15-1
            if rotate==0:
                self.matriz[y][x]=navio[1]
                self.matriz[y+1][x-1]=navio[1]
                self.matriz[y+1][x+1]=navio[1]
            elif rotate==90:
                self.matriz[y][x+1]=navio[1]
                self.matriz[y-1][x]=navio[1]
                self.matriz[y+1][x]=navio[1]
            if rotate==180:
                self.matriz[y+1][x]=navio[1]
                self.matriz[y][x-1]=navio[1]
                self.matriz[y][x+1]=navio[1]
            elif rotate==270:
                self.matriz[y][x-1]=navio[1]
                self.matriz[y-1][x]=navio[1]
                self.matriz[y+1][x]=navio[1]

def choose_navios():
    from random import randint
    navios=[]

    couraçados=1  #0
    cruzadores=2  #1
    destroyers=3  #2
    submarino=1   #3
    hidroavioes=3 #4

    for _ in range(0,10):
        x=randint(0,4)
        if x==0 and couraçados>0:
            couraçados-=1
            navios.append(x)
        elif x==1 and cruzadores>0:
            cruzadores-=1
            navios.append(x)
        elif x==2 and destroyers>0:
            destroyers-=1
            navios.append(x)
        elif x==3 and submarino>0:
            submarino-=1
            navios.append(x)
        elif x==4 and hidroavioes>0:
            hidroavioes-=1
            navios.append(x)
    
    if len(navios)<10:
        for _ in range(len(navios),10):
            if couraçados>0:
                couraçados-=1
                navios.append(0)
            elif cruzadores>0:
                cruzadores-=1
                navios.append(1)
            elif destroyers>0:
                destroyers-=1
                navios.append(2)
            elif submarino>0:
                submarino-=1
                navios.append(3)
            elif hidroavioes>0:
                hidroavioes-=1
                navios.append(4)

    return navios        

def is_collide(nav,pos):
    if nav=='hidroaviao':
        if pos[0]>'A' and pos[0]<'N' and pos[1]>0 and pos[1]<15:
            return False
        else:
            return True
    if nav=='submarino':
        if pos[1]>0 and pos[1]<14:
            return False
        else:
            True
    else:
        return False

def try_put_in(positions):
    couraçado=('█████','couraçado')#1
    cruzador=('████','cruzador')#2
    destroyer=('██','destroyer')#3
    submarino=('██\n██','submarino')#1
    hidroaviao=(' █ \n█ █','hidroaviao')#3

    navios=[[hidroaviao,3],[submarino,1],[couraçado,1],[destroyer,3],[cruzador,2]]

    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

    selected_pos=[]
    solucao=[]
    for navio in navios:
        for _ in range(navio[1]):
            for pos in positions:
                if not pos in selected_pos and not is_collide(navio[1],pos):
                    selected_pos.append(pos)
                    solucao.append((navio[0],pos))
                    if navio[0][1]=='hidroaviao':
                        index=letters.index(pos[0])
                        selected_pos.append((letters[index+1],pos[1]+1))
                        selected_pos.append((letters[index-1],pos[1]+1))
                    elif navio[0][1]=='submarino':
                        index=letters.index(pos[0])
                        selected_pos.append((letters[index+1],pos[1]+1))
                        selected_pos.append((pos[0],pos[1]+1))
                    break
    
    return solucao

def choice_pos():
    import os
    #x=subprocess.call (['Rscript', '--vanilla', 'GA.R'],shell=False).re
    x=os.popen('Rscript GA.R').read()
    x=x[x.find('x1'):]
    x=x.split()
    saida=[]
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    letters.reverse()
    for item in x:
        if item.isnumeric():
            saida.append((letters.pop(),int(item)))
    return saida

def choice_pos_p1():
    couraçado=('█████','couraçado')#1
    cruzador=('████','cruzador')#2
    destroyer=('██','destroyer')#3
    submarino=('██\n██','submarino')#1
    hidroaviao=(' █ \n█ █','hidroaviao')#3

    navios=[[hidroaviao,3],[submarino,1],[couraçado,1],[destroyer,3],[cruzador,2]]

    qntd=[1,2,3,1,3]
    for _ in range(0,10):
        print('Couraçado = ',0,'qntd:',qntd[0],'/Cruzador = ',1,'qntd:',qntd[1])
        print('Destroyer = ',2,'qntd:',qntd[2],'/Submarino = ',3,'qntd:',qntd[3],'/Hidroaviao = ',4,'qntd:',qntd[4])
        navio=int(input('Digite qual navio: '))
        pos=str(input('Digite a posição: '))
        pos=pos.upper()
        if len(pos)==2:
            pos=pos[0]+' '+pos[1]
        else:
            pos=pos[0]+' '+pos[1]+pos[2]
        pos=pos.split()

        pos[1]=int(pos[1])
        if navio==0:
            qntd[0]-=1
        elif navio==1:
            qntd[1]-=1
        elif navio==2:
            qntd[2]-=1
        elif navio==3:
            qntd[3]-=1
        elif navio==4:
            qntd[4]-=1

    m_player.insert(navios[navio],pos,0)
    m_player.draw()

def count_equals(lista):
    new_list=[]

    for item in lista:
        x=lista.count(item)
        if x>1:
            new_list.append((item,x))

    print(new_list,len(new_list))

def get_pos_player():
    while True:
        pos=str(input('Digite a posição: '))
        pos=pos.upper()
        if len(pos)==2:
            pos=pos[0]+' '+pos[1]
        else:
            pos=pos[0]+' '+pos[1]+pos[2]
        pos=pos.split()

        pos[1]=int(pos[1])
        if pos[0]>='A'and pos[0]<='N' and pos[1]>=1 and pos[1]<=15:
            return pos
        else:
            print('Posição não existe')


pos=choice_pos()
solucao=try_put_in(pos)
m_enemy=Matriz('Sua Esquadra')

for item in solucao:
    m_enemy.insert(item[0],item[1],0)
m_enemy.map_navs()

m_player=Matriz('Sua Esquadra')
pos2=choice_pos()
solucao2=try_put_in(pos2)

for item in solucao2:
    m_player.insert(item[0],item[1],0)
m_player.map_navs()

from Modelos import *

p1=Dralar()
p2=Aelos()
rounds=0

from copy import deepcopy
import time

while True:
    if m_player.verify_lose():
        print(p2.name,'Venceu')
        m_player.create_arq()
        count_equals(p2.Choicer.last_choices)
        break
    if m_enemy.verify_lose():
        print(p1.name,'Venceu')
        m_player.create_arq()
        count_equals(p1.Choicer.last_choices)
        break

    
    pos=get_pos_player()
    if m_enemy.verify_pos(pos):
        m_player.insert_on_mcheck(pos)
    else:
        m_player.get_erro(pos)
    '''    
    pos=p1.atack_ia(deepcopy(m_player.m_check))
    if m_enemy.verify_pos(pos):
        m_enemy.kill_pos(pos)
        p1.get_turn((True,pos[0],pos[1]))
        m_player.insert_on_mcheck(pos)
    else:
        p1.get_turn((False,pos[0],pos[1]))
        if p1.Choicer.gotchas!=[]:
            m_player.get_erro(pos)
    '''
    pos_ia=p2.atack_ia(deepcopy(m_enemy.m_check))
    if m_player.verify_pos(pos_ia):
        m_player.kill_pos(pos_ia)
        p2.get_turn((True,pos_ia[0],pos_ia[1]))
        m_enemy.insert_on_mcheck(pos_ia)
    else:
        p2.get_turn((False,pos_ia[0],pos_ia[1]))
        if p2.Choicer.gotchas!=[]:
            m_enemy.get_erro(pos_ia)
    rounds+=1
    print('Rounds: ',rounds)
    print('##### P1 #####')
    m_player.draw_two()