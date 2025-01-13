# PARTE 2: PARTE 3: ESTRUTURAS REPETITIVAS
# Exercício 3.2:
# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações conforme exemplo (use a palavra "in" para dentro do intervalo, e "out" para fora do intervalo).

import random

def main():
    
    dentro_intervalo = 0
    fora_intervalo = 0
    conjunto = set()

    for i in range(5):

        gerar = random.randint(1, 30)

        print(f"Valor {i+1}: {gerar}")

        conjunto.add(gerar)

        if 10 <= gerar <= 20:
            dentro_intervalo += 1
        else:
            fora_intervalo += 1

    print(conjunto)
    print(f"\n{dentro_intervalo} in")
    print(f"{fora_intervalo} out")


if __name__ == "__main__":
    main()