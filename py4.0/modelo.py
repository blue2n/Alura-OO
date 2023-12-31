class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__ (self):
        return f'{self._nome} - {self.ano} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__ (self):
        return f'{self._nome} - {self.ano} - {self.duracao} - Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__ (self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - Likes: {self._likes}'
    
class Playlists:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
   
    def __len__(self):
        return len(self._programas)

jack = Filme('O Estranho Mundo de Jack', 1993, 76)
tudo = Filme('Tudo em todo o lugar ao mesmo tempo', 2022, 139)
mansao = Serie('A maldição da mansão Hill', 2018, 1)
licao = Serie('A lição', 2022, 1)

jack.dar_like()
jack.dar_like()
jack.dar_like()
tudo.dar_like()
tudo.dar_like()
tudo.dar_like()
tudo.dar_like()
mansao.dar_like()
mansao.dar_like()
licao.dar_like()
licao.dar_like()

listinha = [jack, mansao, tudo, licao]
playlist_bom_gosto = Playlists('Bom gosto', listinha)

print(f'Tamanho da playlist: {len(playlist_bom_gosto)}')

for programa in playlist_bom_gosto:
    print(programa)
