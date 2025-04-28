#Importamos todoas as bibliotecas necessárias
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

resets = 0

print("Developed By Lucas Fernandes Di Leone\nPorto Alegre - RS\nFebruary 2025")

#Busca o arquivo CSV, caso não possua o diretório, mude para o seu diretório local
file = pd.read_csv(r'C:\intune\usuarios.csv', dtype=str)
row_count = int(len(file))

#instancia o Google Chrome na sessão do selenium
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

# URLs problemáticas
auth_issue_url = "https://login.microsoftonline.com/common/oauth2/authorize"
login_issue_url = "https://login.microsoftonline.com/common/reprocess"

# Lista para armazenar e-mails que não foram resetados
failed_emails = []

print("Vamos começar os resets agora!!!")

for i in range(row_count):
    cs = file.loc[i]
    mail = str(cs[0])
    senha = cs[1]
    psw = f"{senha}#Educ"

    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    time.sleep(3)

    try:
        # Verificar se a URL de autenticação apareceu
        if auth_issue_url in driver.current_url:
            print("\n!!! ALERTA: O navegador está na página de autenticação do Microsoft Online !!!")
            print("O script será pausado. Faça o login manualmente e depois pressione ENTER para continuar.")
            input("Pressione ENTER após concluir o login...")

        # Verificar se o navegador caiu na página de login indesejada
        if login_issue_url in driver.current_url:
            print("\n!!! ALERTA: O navegador caiu na página de login de reprocessamento !!!")
            print("O script será pausado. Por favor, resolva o problema manualmente e continue.")
            input("Pressione ENTER após resolver para continuar...")

        driver.get("https://admin.microsoft.com/Adminportal/Home")
        time.sleep(3)

        # Hover sobre o botão de redefinir senha
        reset_password_card = driver.find_element(By.ID, "Dashboard,ResetPasswordCard")
        ActionChains(driver).move_to_element(reset_password_card).perform()
        time.sleep(1)

        # Clicar no botão de redefinir senha
        reset_password_card.click()
        time.sleep(1)

        # Buscar usuário
        search_box = driver.find_element(By.XPATH, "//input[@aria-label='Caixa de pesquisa para procurar usuários']")
        search_box.click()
        search_box.clear()
        for char in mail:
            search_box.send_keys(char)
            time.sleep(0.1)
        time.sleep(2)

        # Tentar localizar o usuário
        try:
            user_element = driver.find_element(By.CSS_SELECTOR, ".ms-Persona-initials > span")
            user_element.click()
        except:
            try:
                user_element = driver.find_element(By.CSS_SELECTOR, "span.ms-DetailsHeader-checkTooltip")
                user_element.click()
            except:
                print(f"Usuário {mail} não encontrado. Tentando novamente...")
                driver.refresh()
                time.sleep(5)

                # Segunda tentativa
                search_box = driver.find_element(By.XPATH, "//input[@aria-label='Caixa de pesquisa para procurar usuários']")
                search_box.click()
                search_box.clear()
                for char in mail:
                    search_box.send_keys(char)
                    time.sleep(0.1)
                time.sleep(2)

                try:
                    user_element = driver.find_element(By.CSS_SELECTOR, ".ms-Persona-initials > span")
                    user_element.click()
                except:
                    try:
                        user_element = driver.find_element(By.CSS_SELECTOR, "span.ms-DetailsHeader-checkTooltip")
                        user_element.click()
                    except:
                        print(f"Usuário {mail} não encontrado na segunda tentativa. Pulando...")
                        failed_emails.append(mail)
                        continue

        time.sleep(2)

        # Clicar no botão para redefinir senha
        reset_button = driver.find_element(By.CSS_SELECTOR, '[data-automation-id="bulkResetPasswordPanelRegion,Btn"]')
        reset_button.click()
        time.sleep(2)

        # Inserir nova senha
        password_field = driver.find_element(By.XPATH, "//input[@aria-label='Senha']")
        password_field.click()
        password_field.clear()
        for char in psw:
            password_field.send_keys(char)
            time.sleep(0.1)
        time.sleep(3)

        password_field.click()
        action = ActionChains(driver)
        for _ in range(3):
            action.send_keys(Keys.TAB).perform()
            time.sleep(0.5)


        time.sleep(2)
        action.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        resets = resets+1
        print(f"Senha de {mail} redefinida para {psw}!\n{resets} resetados\n\n----------")
        failed_emails.append(mail)

        driver.get("https://admin.microsoft.com/Adminportal/Home")

    except Exception as e:
        print(f"Erro ao processar o usuário {mail}: {str(e)}")
        failed_emails.append(mail)
        driver.get("https://admin.microsoft.com/Adminportal/Home")

print(f"Processo concluído!\nFoi redefinido um total de {row_count} usuários!")
