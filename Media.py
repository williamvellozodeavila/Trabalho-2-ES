def calcular_media(lista):
    soma = 0
    contador = 0
    for numero in lista:
        soma += numero
        contador += 1
    media = soma / contador
    return media

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = []
    while True:
        nota = float(input("Digite uma nota (ou digite -1 para encerrar): "))
        if nota == -1:
            break
        notas.append(nota)
    
    media = calcular_media(notas)
    resultado = verificar_aprovacao(media)
    
    print(f"A média das notas é {media:.2f} e o aluno está {resultado}.")

if __name__ == "__main__":
    main()
