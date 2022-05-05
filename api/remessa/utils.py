class CNAB:

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.transacoes = []

        self.get_info()

    def get_info(self):

        if self.arquivo:
            file = self.arquivo
            rows = file.readlines()

            for row in rows:
                row = row.decode()
                if isinstance(row, str):
                    transacao = Transacao(row)

                    self.transacoes.append(
                        {
                            'tipo': transacao.get_tipo(),
                            'dt_cadastro': transacao.get_data(),
                            'valor': transacao.get_valor(),
                            'cpf': transacao.get_cpf(),
                            'cartao': transacao.get_cartao_usado(),
                            'hora': transacao.get_hora(),
                            'nome_representante': transacao.get_nome_representante_loja(),
                            'nome_loja': transacao.get_nome_loja(),
                        }
                    )


class Transacao:

    def __init__(self, transacao):
        self.transacao = transacao

    def get_tipo(self):
        return self.transacao[0]

    def get_data(self):
        return self.transacao[1:9]

    def get_valor(self):
        valor = self.transacao[10:19]
        return int(valor) / 100

    def get_cpf(self):
        return self.transacao[20:30]

    def get_cartao_usado(self):
        return self.transacao[30:42]

    def get_hora(self):
        return self.transacao[42:48]

    def get_nome_representante_loja(self):
        return self.transacao[48:62]

    def get_nome_loja(self):
        return self.transacao[62:80]
