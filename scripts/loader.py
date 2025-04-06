# scripts/loader.py
import pandas as pd

def carregarDados():
    df = pd.read_csv('../data/vendas_grande.csv')
    return df
