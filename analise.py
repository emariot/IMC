import numpy as np


def tabela(valorIMC):
    if valorIMC < 16:
        return str(valorIMC) + ': Muito Magro'
    elif valorIMC < 17:
         return str(valorIMC) + ': Magro Moderdo'
    elif valorIMC < 18.5:
         return str(valorIMC) + ': Magro'
    elif valorIMC < 25:
         return str(valorIMC) + ': Saudável'
    elif valorIMC < 30:
         return str(valorIMC) + ': Sobrepeso'
    elif valorIMC < 35:
         return str(valorIMC) + ': Obesidade grau 1'
    elif valorIMC < 40:
         return str(valorIMC) + ': Obesidade Grau II (Severa)'
    else:
         return str(valorIMC) + ': Obesidade Grau III (Mórbida)'
    
altura, peso, forca = np.loadtxt(r"C:\Users\Mariot\Documents\PythonFundamentos\Proje_MMC\peso.csv",
                                 delimiter =';',
                                 unpack=True,
                                 dtype='float')

imc = peso / altura ** 2

print('Min: ', tabela(np.amin(imc)))
print('Max: ', tabela(np.amax(imc)))
print( 'Max - Min: ', tabela(np.ptp(imc)))

print('Média: ', tabela(np.median(imc)))
print('Média Ponderada: ', tabela(np.average(imc)))
print('Média Aritmética: ', tabela(np.mean(imc)))

print('Desvio Padrão: ', np.std(imc))
print('Variância: ', np.var(imc))