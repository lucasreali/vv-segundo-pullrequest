def cifra_de_cesar(texto, deslocamento):

    resultado = ""
    
    for char in texto:
        if char.isalpha():
            if char.isupper():
                numero = ord(char) - ord('A')
                novo_numero = (numero + deslocamento) % 26
                novo_char = chr(novo_numero + ord('A'))
            else:
                numero = ord(char) - ord('a')
                novo_numero = (numero + deslocamento) % 26
                novo_char = chr(novo_numero + ord('a'))
            
            resultado += novo_char
        else:
            resultado += char
    
    return resultado


if __name__ == "__main__":
    resultado1 = cifra_de_cesar("abc", 2)
    print(f'cifra_de_cesar("abc", 2) = "{resultado1}"')
    
    resultado2 = cifra_de_cesar("xyz", 3)
    print(f'cifra_de_cesar("xyz", 3) = "{resultado2}"')
    
    resultado3 = cifra_de_cesar("Ataque ao Amanhecer!", 5)
    print(f'cifra_de_cesar("Ataque ao Amanhecer!", 5) = "{resultado3}"')
    
    print("\nTestes adicionais:")
    
    resultado4 = cifra_de_cesar("def", -2)
    print(f'cifra_de_cesar("def", -2) = "{resultado4}"')
    
    resultado5 = cifra_de_cesar("Teste123!@#", 1)
    print(f'cifra_de_cesar("Teste123!@#", 1) = "{resultado5}"')