import numpy as np
import matplotlib.pyplot as plt


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

print('='*50)
print('Percentil')
print('='*50)
print('IMC Mérdio do 1ºPercentil', tabela(np.median(np.percentile(imc, q=range(0, 25)))))
print('IMC Mérdio do 2ºPercentil', tabela(np.median(np.percentile(imc, q=range(26, 50)))))
print('IMC Mérdio do 3ºPercentil', tabela(np.median(np.percentile(imc, q=range(51, 75)))))
print('IMC Mérdio do 4ºPercentil', tabela(np.median(np.percentile(imc, q=range(76, 100)))))


y = []
x = [1, 2, 3, 4]

y.append(np.median(np.percentile(imc, q=range(0, 25))))
y.append(np.median(np.percentile(imc, q=range(26, 50))))
y.append(np.median(np.percentile(imc, q=range(51, 75))))
y.append(np.median(np.percentile(imc, q=range(76, 100))))
         
plt.plot(x,y)
plt.title('Persentis do IMC da população')
plt.ylabel('Valor')
plt.xlabel('Percentil')
plt.show()