alfabeto = 'abcdefghijklmnopqrstuvwxyzãáàóôòéêè,.'

def cifrar(texto, chave):
    texto_cifrado = ''

    i = 0
    for letra in texto:
        soma = alfabeto.find(letra) + alfabeto.find(chave[i % len(chave)])
        if alfabeto.find(letra) == -1:
            texto_cifrado += " "
        else:
            modulo = int(soma) % len(alfabeto)
            texto_cifrado += str(alfabeto[modulo])
        i += 1
    return texto_cifrado

def decifrar(texto, chave):
    texto_cifrado = ''

    i = 0
    for letra in texto:
        soma = alfabeto.find(letra) - alfabeto.find(chave[i % len(chave)])
        if alfabeto.find(letra) == -1:
            texto_cifrado += " "
        else:
            modulo = int(soma) % len(alfabeto)
            texto_cifrado += str(alfabeto[modulo])
        i += 1
    return texto_cifrado

def main():
    c = str(input('Texto a criptografar: ')).lower()
    chave = str(input('Chave: ')).lower()
    print (cifrar(c, chave))
    c = str(input('Texto a descriptografar: ')).lower()
    chave = str(input('Chave: ')).lower()
    print (decifrar(c, chave))

if __name__ == '__main__':
    main()