#   Fazendo a importação da biblioteca requests e a importação do tkinter
import requests
from tkinter import *


#   Deinindo a função e conecatando com o link dos dados que serão utilizados
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    # Dando o nome a cotação de cada MOEDA
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    # Texto que irá apercer ao clicar no botão
    texto_resposta['text'] = f'''
    Dólar:{cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

# Criando a janela com a biblioteca tkinter
janela = Tk()
janela.title("Cotação Atual Das Suas Moedas")
janela.configure(bg="Gray")
janela.geometry('480x480')


#   Editando o texto que irá aparecer dentro da janela.
texto = Label(janela, text="Clique no botão para obter a cotação atual das Moedas", bg="Gray", font="Times 12 bold")
texto.grid(column=1, row=0, padx=10, pady=10)


#   Editando as caracteristicas do botão dentro da janela
botao = Button(janela, text="Buscar Cotações", font="none 15 bold underline italic", command=pegar_cotacoes, bd=0)
botao.grid(column=1, row=1, padx=0, pady=10)


#   Editando o tetxo que irá aparecer os resultado da Cotação na Janela.
texto_resposta = Label(janela, text="", bg="gray", font="Arial 15 bold")
texto_resposta.grid(column=1, row=10, padx=10, pady=10)


janela.mainloop()
