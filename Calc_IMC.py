#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Calculadora de IMC

altura = float (input('Altura: '))
peso = float (input('Peso: '))
IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5:
    print(f' seu IMC é {IMC}, é considerdo magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print(f' seu IMC é {IMC}, é considerado Normal')
    
elif IMC >= 25.0 and IMC < 29.9:
    print(f' seu IMC é {IMC}, é considerado Sobrepeso')
    
elif IMC >= 30.0 and IMC < 39.9:
    print(f' seu IMC é {IMC}, é considerado Obesidade')
    
else:
    print(f' seu IMC é {IMC}, é considerado Mórbida')
    
    


# In[ ]:




