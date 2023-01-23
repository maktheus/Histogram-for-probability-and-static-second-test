import matplotlib.pyplot as plt

# Dados para a variável Idade
idade = [25, 27, 35, 27, 24, 41, 46, 21, 46, 26]

# Gerando histograma para a variável Idade
plt.hist(idade, bins=8, density=False, histtype='bar', color='c', edgecolor='black', linewidth=1.2)
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Histograma - Idade')
plt.grid(True)

# Salvando histograma em arquivo svg
plt.savefig('histograma_idade.svg')

# Dados para a variável Peso
peso = [117.47, 96.72, 72.03, 73.45, 117.88, 93.23, 94.41, 86.84, 102.19, 74.63]

# Gerando histograma para a variável Peso
plt.hist(peso, bins=8, density=False, histtype='bar', color='g', edgecolor='black', linewidth=1.2)
plt.xlabel('Peso')
plt.ylabel('Frequência')
plt.title('Histograma - Peso')
plt.grid(True)

# Salvando histograma em arquivo svg
plt.savefig('histograma_peso.svg')

