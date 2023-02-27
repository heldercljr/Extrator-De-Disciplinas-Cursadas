class Disciplina:

    def __init__(self, codigo, nome, tipo, creditos, carga_horaria, media, situacao, periodo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.creditos = creditos
        self.carga_horaria = carga_horaria
        self.media = media
        self.situacao = situacao
        self.periodo = periodo

    def __str__(self):
        return "Código: " + self.codigo + "\n" + \
            "Nome: " + self.nome + "\n" + \
            "Tipo: " + self.tipo + "\n" + \
            "Créditos: " + self.creditos + "\n" + \
            "Carga horária: " + self.carga_horaria + "\n" + \
            "Média: " + self.media + "\n" + \
            "Situação: " + self.situacao + "\n" + \
            "Período: " + self.periodo + "\n"
