import string

def encontrar_maior_palavra(frase):

    if not frase or not frase.strip():
        return ""
    
    palavras = frase.split()
    maior_palavra = ""
    
    for palavra in palavras:
        # Remove pontuação do início e fim da palavra
        palavra_limpa = palavra.strip(string.punctuation)
        
        # Se a palavra limpa for maior que a atual maior palavra
        if len(palavra_limpa) > len(maior_palavra):
            maior_palavra = palavra_limpa
    
    return maior_palavra


# Testes para verificar se a função está funcionando corretamente
if __name__ == "__main__":
    # Exemplos fornecidos
    print(encontrar_maior_palavra("O rato roeu a roupa do rei de Roma"))  # Esperado: "roupa"
    print(encontrar_maior_palavra("A jornada de mil milhas começa com um único passo."))  # Esperado: "jornada"
    print(encontrar_maior_palavra("Seja forte e corajoso"))  # Esperado: "forte"
    
    # Testes adicionais
    print(encontrar_maior_palavra(""))  # Esperado: ""
    print(encontrar_maior_palavra("a"))  # Esperado: "a"
    print(encontrar_maior_palavra("palavra, com! pontuação?"))  # Esperado: "pontuação"