class Pessoa:
    olhos = 2 #Criando atributo default fora do __init__, para atributos q não mudam muito

    def __init__(self, *filhos, nome = None, idade = 26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa): #Criação de uma herança que herda todos os atributos da classe
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    mathews = Mutante(nome = 'Mathews')
    luciano = Homem(mathews, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' #adicionando um atributo especifico para a def criada, serve apenas para este nome.
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos #apagando apenas o atributo que foi dado acima
    print(luciano.__dict__)
    print(mathews.__dict__) #atributo de instancia, predefinidos dentro do __init__ ou criadas dentro do processo
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(mathews.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(mathews.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(mathews, Pessoa))
    print(isinstance(mathews, Homem))
    print(mathews.olhos)
    print(luciano.cumprimentar())
    print(mathews.cumprimentar())
