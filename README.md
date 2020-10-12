# Cálculo de IMC
## Calculando IMC de População gerada Randomicamente

Este pequeno programa foi construído para gerar um arquivo csv com uma população aleatória, seu peso, altura e força de ponderação.

Com os dados gerados é possível calcular o IMC, indice de Massa Corpória dos indivíduos.

O IMC é uma medida utilizada internacionalmente par medir o nível de gordura de cada pessoa.  

Calibramos o índice de acordo com a tabela de IMC:  

  
  |RESULTADO|           SITUAÇÃO         |
  |:---------:|:----------------------------:|
  |IMC < 16 | Muito Magro                |
  |IMC < 17 |Magro Moderdo               |
  |IMC < 18.5| Magro                 
  |IMC < 25| Saudável
  |IMC < 30| Sobrepeso
  |IMC < 35| Obesidade grau 1
  |IMC < 40| Obesidade Grau II (Severa)
  |IMC > 40| Obesidade Grau III (Mórbida)
  
*Fonte: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal*

O cálculo utilizado foi: peso / altura ** 2

Os dados apurados nesta população de 140 indivíduos foram:

- Min:  11.07535807764753: Muito Magro
- Max:  49.021529106193306: Obesidade Grau III (Mórbida)
- Max - Min:  37.94617102854578: Obesidade Grau II (Severa)
- Média:  24.072179761609966: Saudável
- Média Ponderada:  25.685476229547668: Sobrepeso
- Média Aritmética:  25.685476229547668: Sobrepeso
- Desvio Padrão:  9.010788651002157
- Variância:  81.19431211302927

### Análise dos Percentis da População:
---
#### Percentil

* IMC Mérdio do 1ºPercentil 15.97826636688736: Muito Magro
* IMC Mérdio do 2ºPercentil 21.932645259793148: Saudável
* IMC Mérdio do 3ºPercentil 26.620071990435658: Sobrepeso
* IMC Mérdio do 4ºPercentil 38.945346043506: Obesidade Grau II (Severa)


