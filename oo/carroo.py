
     voce deve criar um classe carro que vai possuir dois atributos compostos por duas classes:

1)Motor
2)Direcao

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3)métado frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direcao.Ela oferece os seguintes atributos:
1)Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita
3)Método girar a esquerda

    N
  L   O
    S
    EXEMPLO:
    >>>#testando motor
    >>> motor = Motor()
    0
    >>> motor.velocidade
    1
    >>>motor = acelerar()
    >>>motor.velocidade
    2
    >>>motor= acelerar()
    >>>motor.velocidade
    3
    >>>motor = frear ()
    >>>motor.velocidade
    1
    >>>motor = frear ()
    >>>motor.velocidade
    0
>>> # Testando a direcao
>>> direcao = direcao
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'leste'
>>> direção.girar_a_direita()
>>> direção.valor
'sul'
>>> direção.girar_a_direita()
>>> direção.valor
'oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'norte'

>>> direcao.girar_a_esquerda()
>>>direcao.valor
'oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'norte'
>>> carro = Carro(direcao,motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frar()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
'leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'oeste'


class carro :
    def __init__(self,direcao,motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frar(self):
        self.motor.frear()

    def calcular_direcao(self):
        self.direcao.valor()

        


  NORTE = 'norte'
  SUL = 'sul'
  LESTE = 'leste'
  OESTE = 'oeste'

  class direcao:

     rotacao_a_direita_dct= {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
     rotacao_a_esquerda_dct= {NORTE:OESTE,OESTE:SUL,SUL:LESTE,LESTE:NORTE}

      def __init__(self):
          self.valor = NORTE
      def girar_a_direita(self):
          self.valor = self.rotacao_a_direita_dct[self.valor]
      def girar_a_esquerda(self):
          self.valor= self.rotacao_a_esquerda_dct[self.valor]
         

  class Motor :
      def __init__(self):
          self.velocidade = 0
      def acelerar(self):
          self.velocidade += 1
      def frear(self):
          self.velocidade -= 2
          self.velocidade = max(0,self.velocidade)


