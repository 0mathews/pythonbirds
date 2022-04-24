"""

Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar, que deverá incremetar a velocidade de uma unidade;
3) Método frear, que deverá decrementar a velocidade em duas unidades;

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste;
2) Método girar_a_direita
3) Método girar_a_esquerda

    N
O       L
    S

    Exemplo:
    >>> #Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, Motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'

"""


class Motor:
    pass

    def __init__(self):
        self.velocidade = 0

    def velocidade(self):
        return self.velocidade

    def acelerar(self):
        if self.velocidade >= 0:
            self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade) # retorna o valor maior entre 0 e o maior valor da velocidade


if __name__ == '__main__':
    motor = Motor()
    motor.acelerar()
    motor.velocidade()

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    pass

    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE


    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor] # faz a rotação do próprio valor adicionado ao dct


    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor] # faz a rotação do próprio valor adicionado ao dct