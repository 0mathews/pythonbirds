class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    mathews = Pessoa(nome = 'mathews')
    luciano = Pessoa(mathews, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' #adicionando um atributo especifico para a def criada, serve apenas para este nome.
    del luciano.filhos
    print(luciano.__dict__)
    print(mathews.__dict__)