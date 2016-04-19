import numpy as np
import random
import os,subprocess
def clear():
    if os.name == ('nt','dos'):
        subprocess.call("cls")
    elif os.name == ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print "\n"*120
"""Antigen vector """
clear()
a=[1,2,3, 4, 5, 6, 7,	8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ];
""" Signal matrix """
s= np.array([[2, 1, 2], [0, 0 , 3], [2, 1, -1.5]]);
""" Weight matrix """
w=np.array([[2, 1, 2], [0, 0 ,1 ], [2, 1, -1.5]]);
'''print "Original:",  a;'''

""" DCm Samples Q antigen from A """
'''r= random.sample(a, random.randrange(0,7)); '''
'''print "Sample:",  r;
""" Shuffle list to get difirent list randomly"""
r.sort()
print "Reshuffled sample list:",  r;
a1=[i for i in a if not i in r or r.remove(i)]
"""a1=[x for x in a if x not in r]"""
print "Updated list:",  a1;'''
""" Compute the Output Csm, Semi mature and Mature Dendritic cell"""
def random_Sampling(L, i, k):
    r= random.sample(L, random.randrange(i,k));
    if (k < i):
        k=i+1
    r.sort()
    return r
    

def list_Generator(a, k):
   L= ([random.choice(a) for e in range(k)])
   L.sort()
   return L
        
def Substruct_List(L, L1):
    L=[i for i in L if not i in L1 or L1.remove(i)]
    return L

L=list_Generator(a, 100)
print "liste =", L, len(L)
r=[]
User = raw_input('Press enter to exit...')
running = 1
while running == 1:
    if len(L)!=0 and len(L)>len(r):
        r=random_Sampling(L, 10, 14)
        print "liste =", r, len(r)
        L= Substruct_List(L, r)
        print "liste l=", L, len(L)
        User = raw_input('Press enter to exit...')
    else:
        print "Erreur "
        break
    if User == "":
        break
    else:
        running = 1

    

'''
threshold = 100
PAMP= 20
SS = 50
DS = 40
def Compute_output(PAMP, SS, DS):
    Csm=0
    while (Csm < threshold):
        Csm = Csm + (w[0,0]* PAMP)+ (w[0,1]* SS)+ (w[0,2]* DS)
    Csmdc =(w[1,0]* PAMP)+ (w[1,1]* SS)+ (w[1,2]* DS)
    Cmdc =(w[2,0]* PAMP)+ (w[2,1]* SS)+ (w[2,2]* DS)
    Output=[Csm, Csmdc, Cmdc];
    print Output;
Compute_output(PAMP, SS,DS)'''
