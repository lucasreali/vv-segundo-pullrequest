from collections import Counter

def sao_anagramas(string1: str, string2: str) -> bool:

	# Normaliza: remove espaços em branco e passa para minúsculas
	s1 = "".join(string1.split()).lower()
	s2 = "".join(string2.split()).lower()

	# Compara contagens de caracteres
	return Counter(s1) == Counter(s2)

if __name__ == "__main__":
	# Testes rápidos
	print(sao_anagramas("amor", "roma"))             # True
	print(sao_anagramas("A gentleman", "Elegant man"))  # True
	print(sao_anagramas("gato", "cabra"))            # False