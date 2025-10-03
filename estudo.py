class Cliente:
    def __init__(self, nome, idade, email=None):
        self.nome = nome 
        self.senha = None
        self.cadastro = False

    def cadastrar(self, email, senha):
        if not email:  
            print("Erro: O email é obrigatório para realizar o cadastro.")
            return  
        if "@" not in email:  # verifica se o @ está no email
            print("Erro: O email precisa conter '@'.")
            return
        if not senha:  
            print("Erro: A senha é obrigatória para realizar o cadastro.")
            return  

        self.email = email
        self.senha = senha
        self.cadastro = True
        print(f"Cadastro de {self.nome} realizado com sucesso!")


cliente1 = Cliente("Pedro", 20)
cliente1.cadastrar("pedro123@gmail.com", "12345")
