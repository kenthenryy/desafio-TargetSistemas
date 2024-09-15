1)
def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False


num = int(input("Digite um número: "))
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de fibonacci.")
else: print(f"{num} não pertence a sequência de fibonacci.")

2)
def count_a(s):
    s = s.lower()
    count = s.count("a")
    if count > 0:
        print(f"A letra 'a' está presente {count} vezes na string.")
    else:
        print("A letra 'a' não existe na string.")


string_input = input("Informe a string: ")
count_a(string_input)

3)
#int INDICE = 12,
#  SOMA = 0,
#  K = 1;
#  enquanto K < INDICE 
# faça { K = K + 1; SOMA = SOMA + K; } 
# imprimir(SOMA)


INDICE = 12
SOMA = 0
K = 1

while K <= INDICE:
    SOMA = SOMA + K
    K = K + 1

print(SOMA)

#R:78

4)a) 1, 3, 5, 7, 9
    b) 2, 4, 8, 16, 32, 64, 128
    c) 0, 1, 4, 9, 16, 25, 36, 49
    d) 4, 16, 36, 64, 100
    e) 1, 1, 2, 3, 5, 8, 13
    f) 2,10, 12, 16, 17, 18, 19, 200

5)Ligaria o primeiro interruptor e deixaria ligado por alguns minutos.
   Desligaria o primeiro interruptor e ligaria o segundo.
   Então iria  para a sala das lâmpadas.
       A lâmpada que está acesa está sendo controlada pelo segundo interruptor.
       A lâmpada que está apagada mas ficou quente quente é controlada pelo primeiro interruptor.
      A lâmpada que está apagada e mas ainda está fria é controlada pelo terceiro interruptor.
