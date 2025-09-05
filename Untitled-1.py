def main():
    """
    Este programa é um menu simples para cadastro e listagem de usuários.
    Ele permite adicionar nomes e idades, com um limite de 50 usuários.
    """
    
    # Declaração de listas para armazenar nome e idade de até 50 usuários.
    # total_usuarios irá contar quantos usuários foram cadastrados.
    # O limite de 50 é gerenciado pela lógica do código, não pelo tamanho fixo da lista.
    nomes = []
    idades = []
    total_usuarios = 0
    
    # Inicia um loop que continua enquanto o usuário não escolher a opção '3' (Sair).
    while True:
        # Exibe o menu principal para o usuário.
        print("\n--- MENU DE USUÁRIOS ---")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Sair do sistema")
        
        try:
            # Pede a opção e converte a entrada para um número inteiro.
            opcao = int(input("Escolha uma opção: "))
            
            # Usa a estrutura `if/elif/else` para realizar a ação baseada na opção do usuário.
            if opcao == 1:
                # Verifica se ainda há espaço para um novo cadastro (limite de 50).
                if total_usuarios < 50:
                    print("\n--- NOVO CADASTRO ---")
                    nome = input("Digite o nome: ")
                    idade = int(input("Digite a idade: "))
                    
                    # Adiciona os novos dados às listas.
                    nomes.append(nome)
                    idades.append(idade)
                    
                    # Incrementa o contador de usuários após o cadastro.
                    total_usuarios += 1
                    print("Usuário cadastrado com sucesso!")
                else:
                    print("Limite de usuários atingido. Não é possível cadastrar mais.")
            
            elif opcao == 2:
                # Verifica se há usuários cadastrados para listar.
                if total_usuarios > 0:
                    print("\n--- LISTA DE USUÁRIOS ---")
                    # Inicia um loop `for` para percorrer todos os usuários cadastrados.
                    for i in range(total_usuarios):
                        print(f"Usuário {i + 1}:")
                        print(f"  Nome: {nomes[i]}")
                        print(f"  Idade: {idades[i]}")
                else:
                    print("\nNão há usuários cadastrados.")
            
            elif opcao == 3:
                print("\nSaindo do sistema. Até mais!")
                # Sai do loop `while` e finaliza o programa.
                break
            
            else:
                # Ação padrão para opções inválidas.
                print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 3.")
        
        except ValueError:
            # Lida com o erro se o usuário digitar algo que não seja um número para a opção.
            print("\nEntrada inválida. Por favor, digite um número.")

# A linha abaixo garante que a função `main` seja executada quando o script for rodado.
if __name__ == "__main__":
    main()