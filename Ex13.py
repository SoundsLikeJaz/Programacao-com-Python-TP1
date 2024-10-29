palavra = input("Digite uma palavra: ");

def is_palindrome(palavra):
    for i in range(len(palavra)):
        if palavra[i] != palavra[-i-1]:
            return False;
        
    return True;

print(f"A palavra {palavra} {'é' if is_palindrome(palavra) else 'não é'} um palíndromo.");