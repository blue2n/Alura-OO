class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self.likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

jack = Filme('O Estranho Mundo de Jack', 1993, 76)
mansao = Serie('A maldição da mansão Hill', 2018, 1)

jack.dar_like()
jack.dar_like()
jack.dar_like()

mansao.dar_like()
mansao.dar_like()

print (f'{jack.nome} - {jack.ano}- {jack.duracao}: {jack.likes}')
print (f'{mansao.nome} - {mansao.ano} - {mansao.temporadas}: {mansao.likes}')
