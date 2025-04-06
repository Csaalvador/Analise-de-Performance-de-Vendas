from loader import carregarDados
import matplotlib.pyplot as plt

df = carregarDados()

maisVendidos = df.groupby('produto')['quantidade'].count()
graficoMaisVendidos = maisVendidos.plot(kind='bar')

plt.xticks(rotation=45)

plt.tight_layout() 
plt.savefig('../outputs/grafico/graficoMaisVendidos.jpg')
plt.show()