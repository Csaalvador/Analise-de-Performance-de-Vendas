from loader import carregarDados  

df = carregarDados()

receitaTotal = df['valor'].sum()

# print(f"R$ {receitaTotal:.2f}")
qntdProdutos = df.groupby('produto')['quantidade'].count()
melhoresVendedores = df['vendedor'].value_counts()

participacoesDeUF = df['estado'].value_counts()

print(participacoesDeUF)