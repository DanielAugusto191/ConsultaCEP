"""
1. Software Desenvolvido para a consulta de endereço via CEP ultilizando um request em API.
2. Daniel.augusto191@gmail.com
3. Intuito exclusivamente academico
4. Documentação da API ultilizada: https://docs.awesomeapi.com.br/api-cep
"""

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
import _Function.Consultar


class Application:
    def __init__(self, windows):
        # Configurações Padrão Janela
        windows.title("CEP")
        windows.geometry("600x200")
        windows.resizable(0, 0)

        # Configurações de Elementos Iniciais
        # |- Titulo
        self.titulo = Label(windows, text="Buscar CEP",
                            font=("Arial", 30), fg="darkblue")
        self.titulo.grid(row=0, column=0, stick='ew', columnspan='2')
        # |- Caixa de Entrada
        self.inp = Entry(windows)
        self.inp.grid(row=1, column=0, columnspan='2')
        # |- Botão de Enviar
        self.enviar = Button(windows, text="Consultar Endereço",
                             command=lambda: _Function.Consultar.consultar(self, self.inp.get()))
        self.enviar.grid(row=2, column=0, columnspan='2')
        # |- Contato do Desenvolvedor
        self.contato = Label(
            windows, text="daniel.augusto191@gmail.com", fg="darkblue")
        self.contato.grid(row=6, column=0, columnspan="2")

        # Configurações de Elementos Variveis
        # |- Nesse campo ficará o status da consulta - "Cep Encontrado", "Não Encontrado", "Invalido"
        self.status = Label(windows, width='75')
        self.status.grid(row=3, column=0, columnspan='2')
        # |- Rua
        self.lbRua = Label(windows)
        self.lbRua.grid(row=4, column=0)
        # |- Bairro
        self.lbBairro = Label(windows)
        self.lbBairro.grid(row=4, column=1)
        # |- Cidade
        self.lbCidade = Label(windows)
        self.lbCidade.grid(row=5, column=0)
        # |- Estado
        self.lbEstado = Label(windows)
        self.lbEstado.grid(row=5, column=1)


# Iniciaçização, caso seja importado modulos, nao cria a janela
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()

# Thanks! :)
