'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

file = pd.read_csv(r'C:\intune\teste.csv')

print("Digite a posição do CSV")
posicao = int(input())

cs = file.loc[posicao]
mail = cs[0]
psw = cs[1]

print(mail)
print(psw)

# Inicializar o WebDriver do Chrome
driver = webdriver.Chrome()

# Acessar uma página web
driver.get("http://localhost:8080/control/Form.html")

email_field = driver.find_element(By.ID, "email")
email_field.send_keys(mail)

senha_field = driver.find_element(By.ID, "senha")
senha_field.send_keys(psw)

senha_field.send_keys(Keys.RETURN)

input("pressione enter para fechar o navegador")'''

import pandas as pd

# Lê o arquivo CSV
file = pd.read_csv(r'C:\intune\teste.csv')

# Conta as linhas corretamente
row_count = int(len(file))

# Loop para percorrer cada linha do DataFrame
for i in range(row_count):
    cs = file.loc[i]  # Acessa a linha correta pelo índice
    mail = cs[0]  # Primeira coluna
    psw = cs[1]  # Segunda coluna

    print(f"Email: {mail}, Senha: {psw}")  # Exemplo de saída


