import requests

# Função para realizar a consulta e alterar os campos na janela principal


def consultar(self, cep):
    # Fazendo o Request
    self.cep = cep
    Web = "https://cep.awesomeapi.com.br/JSON/{}".format(cep)
    # |- Verificar TimeOut
    try:
        resposta = requests.get(Web)
    except TimeoutError as e:
        print(f"Error: Servidor Demorou a Responder")
        self.status.config(text="Servidor Demorou a Responder. Tente mais Tarde", fg="Red")

    # Tratamento de Resposta
    # |- Code 200 = Consultado com Sucesso. Segundo a Documentação da API
    if resposta.status_code == 200:
        # |- Tratamento
        dados = resposta.content.decode("utf-8").split(',')
        cep = dados[0].split(':')[1].replace('"', '')
        rua = dados[3].split(':')[1].replace('"', '')
        bairro = dados[4].split(':')[1].replace('"', '')
        cidade = dados[5].split(':')[1].replace('"', '')
        estado = dados[6].split(':')[1].replace('"', '')
        # |- Alterando Campos
        self.status.config(text="Consultado Com Sucesso!", fg="green")
        self.lbRua.config(text=rua)
        self.lbBairro.config(text=bairro)
        self.lbCidade.config(text=cidade)
        self.lbEstado.config(text=estado)
        # |- Salvar no Historico
        Historico(rua, bairro, cidade, estado)
        
    # Erros: Code 400 = CEP Invalido, Code 404 = CEP Não encontrado
    else:
        if resposta.status_code == 400:
            self.status.config(text="Cep Invalido!", fg="yellow")
        elif resposta.status_code == 404:
            self.status.config(text="Cep nao encontrado!", fg="Red")
        else:
            self.status.config(
                text="Resposta Inexperada. Favor entrar em contato com o desenvolvedor!")
        cleanFields(self)

# Limpa a consulta os campos da consulta anterior
def cleanFields(self):
    self.lbRua.config(text="")
    self.lbBairro.config(text="")
    self.lbCidade.config(text="")
    self.lbEstado.config(text="")

# Salvar as consultar em um arquivo txt. O formato como foi salvo, é de maneira a facilitar a leitura de dados automaticamente caso necessário.

def Historico(rua, bairro, cidade, estado):
    with open("Historico.txt", "a+") as arquivo:
        arquivo.write(f"['Rua': '{rua}'', 'Bairro': '{bairro}', 'Cidade': '{cidade}', 'Estado': '{estado}']\n")
    arquivo.close()