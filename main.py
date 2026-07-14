import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Fase 1: Análise Exploratória de Dados (EDA)
df = pd.read_csv('credit_risk_dataset.csv')

print(df.head(5))
print(df.shape)
print(df.info())
print(df.describe())

df['person_age'].hist(bins=30)
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()