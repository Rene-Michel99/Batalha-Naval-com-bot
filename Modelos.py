import pickle

class Dralar:
    def __init__(self):
        self.name='Dralar'
        self.cont=0
        self.acertos=0
        self.Choicer=ChoicePos()
        
        with open('nv.pickle','rb') as f:
            self.model=pickle.load(f)
        
    def atack_ia(self,matriz=[]):
        if len(self.Choicer.gotchas)==0:
            return self.Choicer.random_pos()
        else:
            return self.get_last_gotcha(matriz)

    def translate_matrix(self,matriz):
        new_matrix=[]
        lines=[]
        for row in matriz:
            st=''
            li=[]
            row=row[1:]
            for col in row:
                st=col
                if st=='▒':
                    st=0
                elif st=='N':
                    st=6
                elif st=='X':
                    st=1
                li.append(st)
            lines.append(li)

        letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

        x=self.Choicer.gotchas[0][0]
        x=letters.index(x)
        y=self.Choicer.gotchas[0][1]

        for i,row in enumerate(lines):
            new_row=[]
            if i==y:
                if x==0:
                    new_row=row[x:x+6]
                elif x==1:
                    new_row=row[x-1:x+5]
                else:
                    new_row=row[x-2:x+4]
                
                if len(new_row)<6:
                    new_row=[0]*(6-len(new_row))+new_row
            else:
                new_row=[0 for _ in range(0,6)]
            soma=sum(new_row)
            new_matrix.append([soma])
        
        return new_matrix

    def get_last_gotcha(self,matriz):
        matrix=self.translate_matrix(matriz)

        y=self.Choicer.gotchas[0][1]
        
        previsao=self.model.predict(matrix)

        previsao=previsao[y]

        pos=self.Choicer.next_state(previsao)
        if pos[0]==' ':
            pos=('A',pos[1])
        return pos
                
        
    def get_turn(self,entry):
        self.Choicer.last_choices.append((entry[1],entry[2]))

        if entry[0]:
            self.Choicer.gotchas.append((entry[1],entry[2]))
            self.acertos+=1
        else:
            self.cont+=1

        if self.cont==8:
            self.cont=0
            self.Choicer.gotchas.clear()


class Tito:
    def __init__(self):
        self.name='Tito'
        self.cont=0
        self.acertos=0
        self.Choicer=ChoicePos()
        
        with open('knn.pickle','rb') as f:
            self.model=pickle.load(f)
    
    def atack_ia(self,matriz=[]):
        if len(self.Choicer.gotchas)==0:
            return self.Choicer.random_pos()
        else:
            return self.get_last_gotcha(matriz)

    def translate_matrix(self,matriz):
        new_matrix=[]
        lines=[]
        
        for row in matriz:
            st=''
            row=row[1:]
            li=[]
            for col in row:
                st=col
                if st=='▒':
                    st=0
                elif st=='N':
                    st=6
                elif st=='X':
                    st=1
                li.append(st)
            lines.append(li)
        
        letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

        x=self.Choicer.gotchas[0][0]
        x=letters.index(x)
        y=self.Choicer.gotchas[0][1]

        for i,row in enumerate(lines):
            new_row=[]
            if i==y:
                if i==0:
                    new_row=row[x:x+5]
                elif i==1:
                    new_row=row[x-1:x+5]
                else:
                    new_row=row[x-2:x+4]
                
                if len(new_row)<6:
                    new_row=[0]*(6-len(new_row))+new_row
            else:
                new_row=[0 for _ in range(0,6)]
            new_matrix.append(new_row)
        return new_matrix

    def get_last_gotcha(self,matriz):
        matrix=self.translate_matrix(matriz)

        y=self.Choicer.gotchas[0][1]
        
        previsao=self.model.predict(matrix)

        previsao=previsao[y]

        pos=self.Choicer.next_state(previsao)
        return pos

    def get_turn(self,entry):
        self.Choicer.last_choices.append((entry[1],entry[2]))

        if entry[0]:
            self.Choicer.gotchas.append((entry[1],entry[2]))
            self.acertos+=1
        else:
            self.cont+=1

        if self.cont==8:
            self.cont=0
            self.Choicer.gotchas.clear()

class Fanzenlos:
    def __init__(self):
        self.name='Fanzenlos'
        self.cont=0
        self.acertos=0
        self.Choicer=ChoicePos()
        
        with open('DCT.pickle','rb') as f:
            self.model=pickle.load(f)
        
    
    def atack_ia(self,matriz=[]):    
        if len(self.Choicer.gotchas)==0:
            return self.Choicer.random_pos()
        else:
            return self.get_last_gotcha(matriz)

    def translate_matrix(self,matriz):
        new_matrix=[]
        lines=[]
        
        for row in matriz:
            st=''
            row=row[1:]
            li=[]
            for col in row:
                st=col
                if st=='▒':
                    st=0
                elif st=='N':
                    st=6
                elif st=='X':
                    st=1
                li.append(st)
            lines.append(li)
        
        letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

        x=self.Choicer.gotchas[0][0]
        x=letters.index(x)
        y=self.Choicer.gotchas[0][1]

        for i,row in enumerate(lines):
            new_row=[]
            if i==y:
                if i==0:
                    new_row=row[x:x+5]
                elif i==1:
                    new_row=row[x-1:x+5]
                else:
                    new_row=row[x-2:x+4]
                
                if len(new_row)<6:
                    new_row=[0]*(6-len(new_row))+new_row
                new_row=[new_row[0]+new_row[1],new_row[2]+new_row[3],new_row[4]+new_row[5]]
                new_row=[new_row[0]+new_row[1],new_row[2]]
                print(letters[x],i)
                print(new_row)
            else:
                new_row=[0 for _ in range(0,2)]
            new_matrix.append(new_row)
        return new_matrix

    def get_last_gotcha(self,matriz):
        matrix=self.translate_matrix(matriz)

        y=self.Choicer.gotchas[0][1]
        
        previsao=self.model.predict(matrix)

        previsao=previsao[y]

        pos=self.Choicer.next_state(previsao)
        return pos
                
    def get_turn(self,entry):
        self.Choicer.last_choices.append((entry[1],entry[2]))

        if entry[0]:
            self.Choicer.gotchas.append((entry[1],entry[2]))
            self.acertos+=1
        else:
            self.cont+=1

        if self.cont==8:
            self.cont=0
            self.Choicer.gotchas.clear()

class Aelos:
    def __init__(self):
        self.name='Aelos'
        self.Choicer=ChoicePos()
        self.cont=0
        self.acertos=0
        self.guess=0
        
        with open('DCT2.pickle','rb') as f:
            self.model=pickle.load(f)
    
    def atack_ia(self,matriz=[]):
        if len(self.Choicer.gotchas)==0:
            return self.Choicer.random_pos()
        else:
            return self.get_last_gotcha(matriz)

    def translate_matrix(self,matriz):
        new_matrix=[]
        lines=[]
        for row in matriz:
            st=''
            row=row[1:]
            li=[]
            for col in row:
                st=col
                if st=='▒':
                    st=0
                elif st=='N':
                    st=6
                elif st=='X':
                    st=1
                li.append(st)
            lines.append(li)
        
        letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

        x=self.Choicer.gotchas[0][0]
        x=letters.index(x)
        y=self.Choicer.gotchas[0][1]

        for i,row in enumerate(lines):
            new_row=[]
            if i==y:
                if i==0:
                    new_row=row[x:x+5]
                elif i==1:
                    new_row=row[x-1:x+5]
                else:
                    new_row=row[x-2:x+4]
                
                if len(new_row)<6:
                    new_row=[0]*(6-len(new_row))+new_row

                print(letters[x],i)
                print(new_row)
            else:
                new_row=[0 for _ in range(0,6)]
            new_matrix.append(new_row)
        return new_matrix

    def get_last_gotcha(self,matriz):
        matrix=self.translate_matrix(matriz)
        
        y=self.Choicer.gotchas[0][1]
        
        previsao=self.model.predict(matrix)

        previsao=previsao[y]

        pos=self.Choicer.next_state(previsao)
        return pos
                
    def get_turn(self,entry):
        self.Choicer.last_choices.append((entry[1],entry[2]))

        if entry[0]:
            self.Choicer.gotchas.append((entry[1],entry[2]))
            self.acertos+=1
        else:
            self.cont+=1

        if self.cont==8:
            self.cont=0
            self.Choicer.gotchas.clear()

class ChoicePos:
    def __init__(self):
        self.last_choices=[]
        self.gotchas=[]

    def random_pos(self):
        from random import randint
        from random import choice

        y=randint(1,15)
        x=choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N'])
        while True:
            y=randint(1,15)
            x=choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N'])
            if self.last_choices.count((x,y))==0:
                return (x,y)
    
    def next_state(self,previsao):
        letters=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N']

        x=letters.index(self.gotchas[0][0])
        y=self.gotchas[0][1]

        if previsao>0 and previsao<3:
            if x+1<15 and self.last_choices.count((letters[x+1],y))==0:
                return (letters[x+1],y)
            elif x+2<15 and self.last_choices.count((letters[x+2],y))==0:
                return (letters[x+2],y)
            elif x+3<15 and self.last_choices.count((letters[x+3],y))==0:
                return (letters[x+3],y)
            elif x+4<15 and self.last_choices.count((letters[x+4],y))==0:
                return (letters[x+4],y)
        elif previsao==-1 or previsao==-2:
            if x-1>0 and self.last_choices.count((letters[x-1],y))==0:
                return (letters[x-1],y)
            elif x-2>0 and self.last_choices.count((letters[x-2],y))==0:
                return (letters[x-2],y)
            elif x-3>0 and self.last_choices.count((letters[x-3],y))==0:
                return (letters[x-3],y)
            elif x-4>0 and self.last_choices.count((letters[x-4],y))==0:
                return (letters[x-4],y)
        elif previsao==3 or previsao==-3:
            if y>2 and x<13 and self.last_choices.count((letters[x+1],y-1))==0:
                return (letters[x+1],y-1)
            elif y<15 and x<13 and self.last_choices.count((letters[x+1],y+1))==0:
                return (letters[x+1],y+1)
            elif y>1 and y<14 and x<12 and self.last_choices.count((letters[x+2],y))==0:
                return (letters[x+2],y)
            elif y>2 and x>1 and self.last_choices.count((letters[x-1],y-1))==0:
                return (letters[x-1],y-1)
            elif y<15 and x>1 and self.last_choices.count((letters[x-1],y+1))==0:
                return (letters[x-1],y+1)
            elif y>1 and x>2 and self.last_choices.count((letters[x-2],y))==0:
                return (letters[x-2],y)
        elif previsao==4:
            if y<15 and x>1 and self.last_choices.count((letters[x],y+1))==0:
                return ((letters[x],y+1))
            elif y<15 and x<14 and self.last_choices.count((letters[x+1],y+1))==0:
                return ((letters[x+1],y+1))
            elif y<15 and x<14 and self.last_choices.count((letters[x-1],y+1))==0:
                return ((letters[x-1],y+1))
            elif y>2 and x>1 and self.last_choices.count((letters[x],y-1))==0:
                return ((letters[x],y-1))
            elif y>2 and x<14 and self.last_choices.count((letters[x+1],y-1))==0:
                return ((letters[x+1],y-1))
            elif y>2 and x<14 and self.last_choices.count((letters[x-1],y-1))==0:
                return ((letters[x-1],y-1))
        return self.random_pos()