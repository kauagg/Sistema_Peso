def obter_nome():
    while True:
        nome = input("Digite seu nome (mais de 3 caracteres): ").strip()
        if len(nome) > 3:
            return nome
        print("Nome inválido. Deve ter mais de 3 caracteres.")

def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade (0 a 80): "))
            if 0 <= idade <= 150:
                return idade
            print("Idade inválida. A idade deverá estar entre: 0 e 80.")
        except ValueError:
            print("Error: Insira um número.")

def obter_salario():
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario > 0:
                return salario
            print("Salário inválido. Deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_sexo():
    while True:
        sexo = input("Digite seu sexo ('F' para feminino, 'M' para masculino): ").strip().lower()
        if sexo in ['f', 'm']:
            return sexo
        print("Sexo inválido. Por favor, insira 'F' ou 'M'.")

def obter_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").strip().lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        print("Estado civil inválido. Por favor, insira 's', 'c', 'v' ou 'd'.")

def main():
    print("Bem-vindo! Vamos coletar suas informações.")
    
    nome = obter_nome()
    idade = obter_idade()
    salario = obter_salario()
    sexo = obter_sexo()
    estado_civil = obter_estado_civil()

    print("\nInformações coletadas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {estado_civil}")

if __name__ == "__main__":
    main()
