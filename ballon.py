import matplotlib.pyplot as plt
import pandas as pd

#Dados que serão mostrados no gráfico
data = {
    'animal': ['Tenrec', 'Star-nosed mole', 'Squirrel monkey', 'Pig', 'European hedgehog',
               'Short-nosed echidna', 'Little brown bat', 'Giant armadillo', 'Eastern american mole',
               'Big brown bat', 'House mouse', 'Giraffe', 'Eastern american chipmunk', 'Cow', 'Cotton rat',
               'Pilot whale', 'Jaguar', 'Genet', 'Domestic cat', 'Caspian seal'],
    'awake': [8, 13, 14, 14, 13, 15, 4, 5, 15, 4, 11, 22, 8, 20, 12, 21, 13, 17, 11, 20],
    'sleep_rem': [2, 2, 1, 2, 3, 0, 2, 6, 2, 3, 1, 4, 0, 7, 1, 1, 6, 3, 3, 4],
    'sleep_total': [15, 10, 9, 9, 11, 8, 19, 18, 8, 19, 12, 1, 15, 4, 11, 2, 6, 6, 12, 3],
    'vore': ['omni', 'omni', 'omni', 'omni', 'omni', 'insecti', 'insecti', 'insecti', 'insecti', 'insecti',
             'herbi', 'herbi', 'herbi', 'herbi', 'herbi', 'carni', 'carni', 'carni', 'carni', 'carni'],
}

#Aqui é onde cria o DataFrame
df = pd.DataFrame(data)

# Cores que vão ser usadas no gráfico
colors = {
    'omni': '#DA70D6',    # Roxo
    'insecti': '#00CED1', # Azul
    'herbi': '#9ACD32',   # Verde
    'carni': '#FF6347',   # Vermelho
}

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 8))

df = df.iloc[::-1]

# Iterar sobre as colunas do gráfico (awake, sleep_rem, sleep_total)
columns = ['awake', 'sleep_rem', 'sleep_total']
for i, column in enumerate(columns):
    # Tamanho do balão (valor) será proporcional à área do círculo
    sizes = df[column] * 20
    ax.scatter([i]*len(df), df['animal'], s=sizes, c=df['vore'].map(colors), alpha=0.6, edgecolors="w", linewidth=2)
    for j, value in enumerate(df[column]):
        ax.text(i + 0.1, df['animal'].iloc[j], f'{value}', fontsize=8, va='center', ha='left', color=colors[df['vore'].iloc[j]])

# Configurações do eixo x
ax.set_xticks(range(len(columns)))
ax.set_xticklabels(columns)

# Configurações do eixo y
ax.set_yticks(range(len(df)))
ax.set_yticklabels(reversed(df['animal']))

# Cria listas vazias para os marcadores de legenda
legend_markers_value = []
legend_markers_vore = []

# For para criar a legenda para 'value'
for value in [5, 10, 15, 20]:
    legend_markers_value.append(ax.scatter([], [], s=value * 20, c='gray', alpha=0.6, label=f'{value}'))

# For para criar a legenda para 'vore'
for label in colors:
    legend_markers_vore.append(ax.scatter([], [], c=colors[label], label=label, alpha=0.6, s=100, edgecolors="w", linewidth=2))

# Combinar as legendas (valor antes da legenda de 'vore')
legend1 = ax.legend(legend_markers_value, [f'{value}' for value in [5, 10, 15, 20]], title="value", bbox_to_anchor=(1.05, 1), loc='upper left')
legend2 = ax.legend(legend_markers_vore, colors.keys(), title="vore", bbox_to_anchor=(1.05, 0.6), loc='upper left')

ax.add_artist(legend1)  

# Tirar a borda porque no exemplo não tem
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Título e layout
ax.xaxis.tick_top()
plt.tight_layout()

# Exibir o gráfico
plt.show()