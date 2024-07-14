# Passo 1: Entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
# Passo 2: Fazer login
# Passo 3: Pegar/Importar a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o cadastro até cadastrar todos o produtos

import pyautogui
import time

# pyautogui.click - clica com o mouse
# pyautogui.write - escreve um texto
# pyautogui.press - aperta uma tecla
# pyautogui.hotkey - combinação de teclas
# pyautogui.scroll - rola a tela

pyautogui.PAUSE = 0.5 # a cada comento há uma pausa de 0.5 segundos

# Passo 1: Entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) #espera de 3 segundos 

# Passo 2: Fazer login
pyautogui.click(x=1040, y=473)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("luana@gmail.com")

pyautogui.press("tab")
pyautogui.write("senhaluana123")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto

for linha in tabela.index:

  codigo = str(tabela.loc[linha, "codigo"])
  pyautogui.click(x=930, y=325)
  pyautogui.write(codigo)

  marca = str(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
  pyautogui.write(marca)

  tipo = str(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
  pyautogui.write(tipo)

  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.press("tab")
  pyautogui.write(categoria)

  preco = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.press("tab")
  pyautogui.write(preco)

  custo = str(tabela.loc[linha, "custo"])
  pyautogui.press("tab")
  pyautogui.write(custo)

  pyautogui.press("tab")
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":    
    pyautogui.write(obs)

  #enviar formulario
  pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(5000)