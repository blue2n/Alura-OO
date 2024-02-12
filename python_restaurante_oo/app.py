from oo.restaurante import Restaurante


restaurante_casa = Restaurante('Casa', 'Caseiro')
#restaurante_carne = Restaurante('Churras', 'Churrascaria')
#restaurante_japa = Restaurante('Japa top', 'Japonesa')

#restaurante_casa.mudar_status()

restaurante_casa.receber_avaliacao('Anna', 4)
restaurante_casa.receber_avaliacao('Carol', 2)
restaurante_casa.receber_avaliacao('Io', 5)

def main():
    Restaurante.lista_restaurante()

if __name__ == '__main__':
    main()