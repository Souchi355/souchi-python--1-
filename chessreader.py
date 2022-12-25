import pandas as pd
class chess:
    def __init__(self,moves):
        self.moves=moves

    def splt(self,moves):
        numove=0
        for i in range(len(moves)):
            if moves[i]==".":
                numove+=1

        listm={i:None for i in range(1,numove+1)}

        for i in range(1,numove+1):
            if i<10:
                listm[i]=moves[moves.find(str(i)+".")+2:moves.find(str(i+1)+".")]
            elif 10<=i<=99:
                listm[i]=moves[moves.find(str(i)+".")+3:moves.find(str(i+1)+".")]
            elif 99<i<=999:
                listm[i]=moves[moves.find(str(i)+".")+4:moves.find(str(i+1)+".")]

        for i in range(1,numove+1):
            listm[i]=listm[i].split()
            if len(listm[i])>2:
                if "$" in listm[i][1]:
                    listm[i][0]=listm[i][0],listm[i][1]
                    listm[i].remove(listm[i][1])
                elif "$" in listm[i][2]:
                    listm[i][1]=listm[i][1],listm[i][2]
                    listm[i].remove(listm[i][2])
            if len(listm[i])==1:
                listm[i].append("dead")
            if (type(listm[i][0]) != tuple )and(type(listm[i][1]) != tuple ):
                listm[i][0]=listm[i][0],None
                listm[i][1]=listm[i][1],None
            elif (type(listm[i][0]) != tuple )and(type(listm[i][1]) == tuple ):
                listm[i][0]=listm[i][0],None
            elif (type(listm[i][0]) == tuple )and(type(listm[i][1]) != tuple ):
                listm[i][1]=listm[i][1],None

        return listm
    
    def show(self,moves):
        for i in range(1,len(moves)+1):
            print(moves[i])
            print()


file=open("moves.txt","r")
moves=""
for line in file:
    moves=moves+line
moves=moves[moves.find("1. "):moves.find("#")+1]
chs=chess(moves)
chs.show(chs.splt(chs.moves))

