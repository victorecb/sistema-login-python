import hashlib
def menu():
    while True:
        opcao = input("Digite a opção (0)SAIR|(1)CADASTRAR|(2)LOGIN): ")
        if opcao == "1":
            usuario = input("Digite o usuário: ").strip().lower()
            senha = input("Digite a senha: ").strip()
            if not usuario or not senha:
                print("Campo não pode estar vazio")
                continue
            cadastro = cadastrar(usuario,senha)
            if cadastro:
                print("Usuário cadastrado")
                continue
            else:
                print("Usuário ja existe")

        elif opcao == "2":
            tentativa = 0
            while tentativa < 3:               
                usuario = input("Digite o usuário: ").strip().lower()
                senha = input("Digite a senha: ").strip()
                if not usuario or not senha:
                    print("O campo não pode estar vazio!")
                    tentativa += 1
                    continue
                resultado = login(usuario, senha)
                if resultado:
                    print("Acesso permitido")
                    break
                else:
                    print("Usuário ou senha incorretos!")
                    tentativa += 1
                    continue
            if tentativa == 3:
                print("Numero de tentativas excedidos!")
                                    
        elif opcao == "0":
            break

        else:
            print("Opção inválida!")
            continue
        
#def autenticar(usuario, senha):
#    usuario = input("Digite o usuario: ").strip().lower()
#    senha = input("digite a senha: ").strip()
#    if not usuario or not senha:
#        return False
#    else:
#        return True
    

def cadastrar(usuario,senha):
    senha_hash = hash_senha(senha)
    existe = False
    try:
        with open("cadastro.txt","r") as f:
            
            for linha in f:
                usuario_arquivo = linha.strip().split(":")[0]
                if usuario_arquivo == usuario:
                    existe = True
                    break
    except FileNotFoundError:
        pass
        
    if existe:
        return False
    else:
        escrita(usuario,senha_hash)
        return True
        
        
def escrita(user,passwd):
    with open("cadastro.txt","a") as f:
        f.write(f"{user}:{passwd}\n")
        
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
        
#def leitura():
    #with open("cadastro.txt", "r") as f:
        
                    
def login(usuario,senha):
    senha_hash = hash_senha(senha)
    try:
            
            with open("cadastro.txt","r") as f:
                
                for linha in f:
                    dados = linha.strip().split(":")
                    if len(dados) == 2:
                        if usuario == dados[0] and senha_hash == dados[1]:
                            return True
                        
            return False
    except FileNotFoundError:
        return False
    
        
        
menu()
    
        
