def soma(numero1, numero2):
    return numero1 + numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def filtro_espaco(frase):
    resposta = ''
    for letra in frase:
        if letra != ' ':
            resposta += letra
    return resposta