def verifica_digito(caractere):
    digito = ord(caractere)
    return 48 <= digito <= 57

print(verifica_digito(input()))
