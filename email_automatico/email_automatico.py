import streamlit as st
import yfinance as yf
from plotly import graph_objs as go
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import openpyxl as xl
import pdfplumber
import os
import pandas as pd
import pyautogui
import pyperclip

opcoes_radio = ['Anexar arquivo', 'E-mail sem arquivo']

def email():
    st.subheader("Você deve estar logado!")
    st.subheader("Informe o endereço do email: ")
    endereco = st.text_input("Endereço")
    assunto = st.text_input("Assunto")
    mensagem = st.text_area("Mensagem")
    #mensagem = st.text_input("Mensagem")
    option = st.radio('Complemento', opcoes_radio,horizontal=True)
    if option == "Anexar arquivo":
        st.write("Arquivo deve estar na pasta padrão do gmail ao clicar em anexar")
        nome_arquivo = st.text_input("Nome do arquivo")
        button_email = st.button("Enviar e-mail")
        if button_email:
            if len(endereco) != 0 and len(assunto) != 0 and len(mensagem) != 0 and len(nome_arquivo) != 0:
                pyautogui.hotkey("ctrl", "t")
                pyperclip.copy("www.gmail.com")
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("enter")
                time.sleep(4)
                pyautogui.click(x=72, y=171)
                time.sleep(2)
                pyperclip.copy(endereco)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("tab")
                time.sleep(1)
                pyperclip.copy(assunto)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("tab")
                time.sleep(1)
                pyperclip.copy(mensagem)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("tab")
                time.sleep(1)
                pyautogui.click(x=961, y=692)             
                pyperclip.copy(nome_arquivo)
                time.sleep(1)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("enter")
                time.sleep(2)
                pyautogui.click(x=845, y=695)  
            else:
                st.write("!!! Preencha todos os campos !!!")

    elif option == 'E-mail sem arquivo':
        button_email = st.button("Enviar e-mail")
        if button_email:
            if len(endereco) != 0 and len(assunto) != 0 and len(mensagem) != 0:
                pyautogui.hotkey("ctrl", "t")
                pyperclip.copy("www.gmail.com")
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("enter")
                time.sleep(4)
                pyautogui.click(x=72, y=171)
                time.sleep(2)
                pyperclip.copy(endereco)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("tab")
                time.sleep(1)
                pyperclip.copy(assunto)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("tab")
                time.sleep(1)
                pyperclip.copy(mensagem)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.hotkey("tab")
                pyautogui.click(x=845, y=695)              
            else:
                st.write("!!! Preencha todos os campos !!!")

lista_acoes = ["E-mail automático"]

st.markdown("""
# Processos automáticos
### Automatizando processos que facilitam a sua vida
""")

with st.sidebar:
    st.header("Menu")
    op = st.selectbox("Selecione a ação: ", lista_acoes)
    if op == "Consolidar planilhas do mesmo tipo" or op == "Transcrever pdf em excel":
        qtd_arquivos = st.number_input("Quantidade de arquivos", 1, 10, 1)

st.image("logo.jpg")

st.header(f"{op}")

if op == "E-mail automático":
    email()