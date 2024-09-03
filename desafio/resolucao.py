#1)

INDICE = 13
SOMA = 0
K = 0

while (K < INDICE):
    K = K + 1
    SOMA = SOMA + K
 
print(SOMA)

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13
# 91


#2)
n = 5

a = 0
b = 1

cont = 0

while (cont < n):
    f = a + b
    print(f)
    a = b
    b = f
    
    cont = cont + 1

print("fim")

if (a == n):
    print("O número pertence à sequência de Fibonacci.")
else:
    print("O número não pertence à sequência de Fibonacci.")


#3 e 4) Infelizmente eu não entendi e não soube como fazer, mas go


#5)
string = "Hello"
stringInvertida = string[::-1]
print(stringInvertida)
