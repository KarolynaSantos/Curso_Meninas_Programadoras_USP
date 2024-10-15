import matplotlib.pyplot as plt

# Dados fictícios
carreiras = ['Advogado', 'Médico', 'Contador', 'Engenheiro', 'Arquiteto']
salarios_sp = [8000, 12000, 6000, 10000, 9000]
salarios_rj = [7500, 11000, 5800, 9500, 8800]
salarios_sc = [7800, 11500, 6200, 9800, 9200]

impostos = [15, 20, 10, 18, 12]  # Porcentagem de imposto retido

# Gráfico de média salarial por carreira e região
fig, ax = plt.subplots(figsize=(10, 6))
for i, carreira in enumerate(carreiras):
    ax.bar(carreira, [salarios_sp[i], salarios_rj[i], salarios_sc[i]], label=carreira)

ax.set_ylabel('Salário Médio')
ax.set_title('Média Salarial por Carreira e Região')
ax.legend()
plt.show()

# Gráfico de imposto retido na nota por carreira
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(carreiras, impostos)
ax.set_ylabel('Percentual de Imposto Retido')
ax.set_title('Percentual de Imposto Retido na Nota por Carreira')
plt.show()

# Tabela com documentos para abrir CNPJ
documentos = {
    'Advogado': ['Diploma', 'OAB', 'CPF', 'RG', 'Comprovante de Residência'],
    'Médico': ['Diploma', 'CRM', 'CPF', 'RG', 'Comprovante de Residência'],
    'Contador': ['Diploma', 'CRC', 'CPF', 'RG', 'Comprovante de Residência'],
    'Engenheiro': ['Diploma', 'CREA', 'CPF', 'RG', 'Comprovante de Residência'],
    'Arquiteto': ['Diploma', 'CAU', 'CPF', 'RG', 'Comprovante de Residência']
}

# Imprimir tabela
print("GUIA PARA ABERTURA DE EMPRESA POR REGIÃO E PROFISSÃO")
print("\nDocumentos necessários para abrir CNPJ:\n")
for carreira, doc_list in documentos.items():
    print(f"{carreira}: {', '.join(doc_list)}")

# Gráfico de tempo médio para abrir uma empresa por região
tempos_medios = [30, 40, 25]  # Tempo em dias
regioes = ['SP', 'RJ', 'SC']

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(regioes, tempos_medios, color='green')
ax.set_ylabel('Tempo Médio (dias)')
ax.set_title('Tempo Médio para Abrir uma Empresa por Região')
plt.show()

