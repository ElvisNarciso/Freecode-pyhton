# Função para adicionar uma despesa à lista de despesas
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Função para imprimir todas as despesas na lista
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Função para calcular o total de todas as despesas na lista
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Função para filtrar as despesas por categoria
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Função principal do programa
def main():
    # Lista para armazenar as despesas
    expenses = []

    # Loop principal que permite ao usuário interagir com o programa
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        # Solicitar a escolha do usuário
        choice = input('Enter your choice: ')

        if choice == '1':
            # Adicionar uma nova despesa
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Imprimir todas as despesas
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            # Imprimir o total de todas as despesas
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            # Filtrar despesas por categoria e imprimir
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            # Sair do programa
            print('Exiting the program.')
            break

# Se o script estiver sendo executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    # Chama a função principal
    main()
