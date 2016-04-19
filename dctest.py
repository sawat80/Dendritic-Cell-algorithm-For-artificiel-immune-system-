import numpy as np
import random
##
Antigen_Vector       =list(range(0,10))
Antigen_Mature_Count    =[0] *10
Antigen_presented_Count =[0] *10
Weight_Matrix           = np.array([[2, 1, 2], [0, 0 ,1 ], [2, 1, -1.5]]);
##
def list_Generator(a, k):
   L= ([random.choice(a) for e in range(k)])
   L.sort()
   return L
##
def Remove_from_population (L,L1):
   L=[i for i in L if not i in L1 or L1.remove(i)]
   return L
##
def count_antigen(l_list, l_sample):
   l_count=[0]* 10
   for i in l_sample:
      if i in l_list:
         l_count[i]+=1
   return l_count
##  
class DC:
   i=75
   k=100
   DC_Antigen_Vector= []  
##
   def __init__ (self):
      self.DC_Input_Signals_Matrix = []
      self.DC_Antigen_Vector = []
      self.Output_Cms=0
      self.Output_DC_mature             = 0
      self.Output_DC_Semi_mature        = 0
      self.Migration_threshold          = random.randrange(0,1000)
      self.Context                      = 0
##
   def Samples_Antigen(self, A):
      self.DC_Antigen_Vector = random.sample(A, random.randrange(DC.i,DC.k))
      global Antigen_presented_Count
      Antigen_presented_Count = count_antigen(Antigen_Vector, t.DC_Antigen_Vector)
      return self.DC_Antigen_Vector
##
   def update_interim_output():
      global Antigen_Mature_Count
      Remove_from_population(t.DC_Antigen_Vector,L)
      while (self.Output_Cms > self.Migration_threshold):
         self.Output_Cms            += (w[0,0]* self.DC_Input_Signals_Matrix[i,0])+ (w[0,1]* self.DC_Input_Signals_Matrix[i,1])+ (w[0,2]* self.DC_Input_Signals_Matrix[i,2])
         self.Output_DC_Semi_mature += (w[1,0]* self.DC_Input_Signals_Matrix[i,0])+ (w[1,1]* self.DC_Input_Signals_Matrix[i,1])+ (w[1,2]* self.DC_Input_Signals_Matrix[i,2])
         self.Output_DC_mature      += (w[2,0]* self.DC_Input_Signals_Matrix[i,0])+ (w[2,1]* self.DC_Input_Signals_Matrix[i,1])+ (w[2,2]* self.DC_Input_Signals_Matrix[i,2])
         if(self.Output_DC_mature>self.Output_DC_Semi_mature):
            self.Context = 1
            Antigen_Mature_Count += count_antigen(Antigen_Vector, t.DC_Antigen_Vector)
            break
         else:
            i+=1



         
      ''' DC Migration **************************************************'''

            
   '''*********************************************************************'''
   def detection():
   		self.Samples_Q
'''**********************************************************************'''
'''**********************************'''
 
L= list_Generator(Antigen_Vector, 100)
print L
c= dict((i, L.count(i)) for i in L)
print c
t=DC()
'''print " Migration_threshold = "+ str(t.Migration_threshold)'''
print t.Samples_Antigen(L) 

print Antigen_presented_Count
'''Remove_from_population(t.DC_Antigen_Vector, L)
print L, len(L)'''
