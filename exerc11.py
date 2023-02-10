int1: int = int(input("Digite um valor inteiro: "))
int2: int = int(input("Digite outro valor inteiro: "))
float1: float = float(input("Digite um valor real: "))

a = (int1 * 2) + (int2 / 2)
b = (int1 * 3) + float1
c = (float1 ** 3)
print(f"{a}")
print(f"{b}")
print(f"{c}")