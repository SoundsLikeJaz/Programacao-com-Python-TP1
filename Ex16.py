num = int(input("Digite um número: "));

def odd_or_even(num):
    return "ímpar" if num % 2 else "par";

print(f"O número {num} é {odd_or_even(num)}.");