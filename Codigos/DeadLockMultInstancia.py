#!/usr/bin/env python
# coding: utf-8

# In[25]:


# autor: Felipe Marcelo, Henrique Tostes
# data: 16 de maio de 2020
# Algoritmo para verificar se multiplos processos estao em deadlock


# In[1]:


import numpy as np
import operator


# In[23]:


qntRecursosAloc = input("Quantidade de tipos de recursos:")
qntProcAloc = input("Quantidade de processos:")

qntProcAloc = int(qntProcAloc)
qntRecursosAloc = int(qntRecursosAloc)

recDisponivel = []

for i in range(qntRecursosAloc):
    recDisponivel.append(int(input("Quantidade de recursos disponives do recurso {0}: ".format(i + 1))))

listaProc = []
for i in range(qntProcAloc):
    listaProc.append(i)
    


# In[19]:


# criando matriz de alocacao e de requisicao
alocacao = np.zeros((qntProcAloc, qntRecursosAloc), dtype = "int64")
requisicao =  np.zeros((qntProcAloc, qntRecursosAloc), dtype = "int64")


# In[20]:


# preenchendo quantidade de recursos para cada processo 
for i in range(qntProcAloc):
    for j in range(qntRecursosAloc):
        if j == 0:
            alocacao[i][j] = input("Entre com a quantidade de recurso A que o processo {0} tem alocado:".format(i + 1))
        elif j == 1:
            alocacao[i][j] = input("Entre com a quantidade de recurso B que o processo {0} tem alocado:".format(i + 1))
        elif j == 2:
            alocacao[i][j] = input("Entre com a quantidade de recurso C que o processo {0} tem alocado:".format(i + 1))
        elif j == 3: 
            alocacao[i][j] = input("Entre com a quantidade de recurso D que o processo {0} tem alocado:".format(i + 1))


# In[21]:


# preenchendo quantidade de recursos para cada processo 
for i in range(qntProcAloc):
    for j in range(qntRecursosAloc):
        if j == 0:
            requisicao[i][j] = input("Entre com a quantidade de recurso A que o processo {0} requisitou:".format(i + 1))
        elif j == 1:
            requisicao[i][j] = input("Entre com a quantidade de recurso B que o processo {0} requisitou:".format(i + 1))
        elif j == 2:
            requisicao[i][j] = input("Entre com a quantidade de recurso C que o processo {0} requisitou:".format(i + 1))
        elif j == 3: 
            requisicao[i][j] = input("Entre com a quantidade de recurso D que o processo {0} tem alocado:".format(i + 1))


# In[107]:


'''
Caso vc queira trabalhar com mais tipos de recurso,
adicionar mais condições 'elif' nos 'for' do preen-
chimento da matriz de requisicao e alocacao.
'''


# In[24]:


count = 0

# verifa quais processos estao finalizados
while(not listaProc == False and count < len(listaProc)):
    
    # comparando se lista de requisicao de recurso eh menor que recursos disponiveis
    if (all(i <= j for i, j in zip(requisicao[count], recDisponivel))) == True:
        
        # finaliza processo 
        print("Processo {0} finalizou execucao e liberou recurso".format(listaProc[count] + 1))
        
        print("Recurso disponivel + recurso liberado:\n ", recDisponivel, "+", alocacao[count] )
        # atualiza valor de recursos
        recDisponivel = list(map(operator.add, recDisponivel, list(alocacao[count])))
        
        # retira processo finalizado da lista de processo
        listaProc.pop(count)
        count = 0

    else:
        count+=1

# processos que não tem recurso para terminar execucao
if((not listaProc) == False):
    print(listaProc)
    
    for i in listaProc:
        print("Processo {0} esta em deadlock".format(i + 1))
else:
    print("O sistema não esta em deadlock")
        


# In[ ]:




