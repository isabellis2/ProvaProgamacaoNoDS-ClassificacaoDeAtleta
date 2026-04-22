# Entrada de dados
print("--- Sistema de Classificacao de Atletas ---")
idade = int(input("Digite a idade do nadador: "))

# Logica de classificacao
if idade >= 5 and idade <= 7:
    print("Categoria: INFANTIL")
elif idade >= 8 and idade <= 17:
    print("Categoria: JUVENIL")
elif idade >= 18:
    print("Categoria: ADULTO")
else:
    print("Idade fora da faixa permitida para competicao.")

# Mensagem de encerramento
print("Processo finalizado.")