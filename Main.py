from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\gabriel\downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

caminho = os.getcwd()
arquivo = caminho + r"\login.html"
navegador.get(arquivo)

navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys("exemplo@gmail.com")
navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys("123456")
navegador.find_element(By.XPATH, '/html/body/div/form/button').click()

tabela = pd.read_excel("NotasEmitir.xlsx")
display(tabela)

for linha in tabela.index:
    # nome/razao social
    navegador.find_element(By.NAME, 'nome').send_keys(tabela.loc[linha, "Cliente"])

    # endereco
    navegador.find_element(By.NAME, 'endereco').send_keys(tabela.loc[linha, "Endereço"])

    # bairro
    navegador.find_element(By.NAME, 'bairro').send_keys(tabela.loc[linha, "Bairro"])

    # municipio
    navegador.find_element(By.NAME, 'municipio').send_keys(tabela.loc[linha, "Municipio"])

    # cep
    navegador.find_element(By.NAME, 'cep').send_keys(str(tabela.loc[linha, "CEP"]))

    # UF
    navegador.find_element(By.NAME, 'uf').send_keys(tabela.loc[linha, "UF"])

    # CPF/CNPJ
    navegador.find_element(By.NAME, 'cnpj').send_keys(str(tabela.loc[linha, "CPF/CNPJ"]))

    # Inscricao estadual
    navegador.find_element(By.NAME, 'inscricao').send_keys(str(tabela.loc[linha, "Inscricao Estadual"]))

    # descrição
    texto = tabela.loc[linha, "Descrição"]
    navegador.find_element(By.NAME, 'descricao').send_keys(texto)

    # quantidade
    navegador.find_element(By.NAME, 'quantidade').send_keys(str(tabela.loc[linha, "Quantidade"]))

    # valor unitario
    navegador.find_element(By.NAME, 'valor_unitario').send_keys(str(tabela.loc[linha, "Valor Unitario"]))

    # valor total
    navegador.find_element(By.NAME, 'total').send_keys(str(tabela.loc[linha, "Valor Total"]))

    # clicar em emitir nota fiscal
    navegador.find_element(By.CLASS_NAME, 'registerbtn').click()

    # recarregar a página para limpar o formulário
    navegador.refresh()