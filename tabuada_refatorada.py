tabuada = int(input("Vou mostrar a tabuada do: "))
inicio = int(input("Iniciar em: "))
final = int(input("Finalizar em: ")) + 1

if int(inicio) < int(final):
    for n in range(int(inicio), int(final)+1):
    print(tabuada, "X", n, "=", int(tabuada)*n)
else:
    print("Erro, o inicio deve ser menor que o fim")