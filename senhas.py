import re  # Importa o módulo de expressões regulares para correspondência de padrões
import secrets  # Importa o módulo secrets para geração segura de números aleatórios
import string  # Importa o módulo string para operações de manipulação de strings

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define os caracteres possíveis para a senha
    letters = string.ascii_letters  # Letras maiúsculas e minúsculas
    digits = string.digits  # Dígitos numéricos
    symbols = string.punctuation  # Caracteres especiais

    # Combina todos os caracteres
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Gera a senha
        for _ in range(length):
            password += secrets.choice(all_characters)  # Escolhe um caractere aleatório de all_characters
        
        # Define as restrições para a composição da senha
        constraints = [
            (nums, r'\d'),  # Pelo menos `nums` dígitos numéricos
            (special_chars, fr'[{symbols}]'),  # Pelo menos `special_chars` caracteres especiais
            (uppercase, r'[A-Z]'),  # Pelo menos `uppercase` letras maiúsculas
            (lowercase, r'[a-z]')  # Pelo menos `lowercase` letras minúsculas
        ]

        # Verifica as restrições
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break  # Sai do loop se todas as restrições forem atendidas
    
    return password  # Retorna a senha gerada

if __name__ == '__main__':
    # Se o script for executado como programa principal (não importado como módulo)
    new_password = generate_password()  # Gera uma senha usando parâmetros padrão
    print('Senha gerada:', new_password)  # Imprime a senha gerada
