def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    return "Aprovado" if media >= 6 else "Reprovado"

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
