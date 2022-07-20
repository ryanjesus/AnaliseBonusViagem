import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC70f67626891e1ad6817ddc34a4554021"
# Your Auth Token from twilio.com/console
auth_token = "4af02ddd3fea9bb0145d213c7aa3416e"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_venda = pd.read_excel(f'{mes}.xlsx')

    if (tabela_venda['Vendas'] > 55000).any():
        vendedor = tabela_venda.loc[tabela_venda['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_venda.loc[tabela_venda['Vendas'] > 55000, 'Vendas'].values[0]

        message = client.messages.create(
            to="+5511962242391",
            from_="+19104690833",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo:
# Verificar se algum valor na coluna venda do arquivo é mai or que 55.000


# Se for maior do que 55.000 Enviar um sms com o Nome, o mês e as vendas dele

# Caso não seja maior do que 55.000 não quero fazer nada
