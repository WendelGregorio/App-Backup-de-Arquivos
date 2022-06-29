import os
import shutil
from datetime import date

def Backup_Mult_Files():
    file_type = input("Inisira o Tipo de arquivo(sem o '.' ponto):\n")
    
    path = input("Inisira o nome da pasta do arquivo:\n")
    entries = os.listdir(r"" + path)
    
    dst = input("Inisira o nome da pasta Destino:\n")
    dst = r"" + dst
    
    for file in entries:
        if file.endswith('.txt'):
            if shutil.copy2((path + '/' + file),(dst  + '/' +  file.replace(('.' + file_type),'') + '_' + str(date.today()) + '.' + file_type)):
                print("Backup realizado com sucesso!")
                Check()
            else:
                print("Não foi possível realizar o backup!")
                Check()
                
def Backup_one_File():
    file_type = input("Inisira o Tipo de arquivo(sem o '.' ponto):\n")
    
    path = input("Inisira o nome da pasta do arquivo:\n")
    entries = os.listdir(r"" + path)
    
    file_name = input("Inisira o nome do arquivo desejado:\n")
    
    dst = input("Inisira o nome da pasta Destino: ")
    dst = r"" + dst
    
    for file in entries:
        if file.endswith('.txt'):
            
            print(str(file_name + file_type) + " " + str(file))
            if str(file_name + '.' + file_type) == str(file):
                if shutil.copy2((path + '/' + file),(dst  + '/' +  file.replace(('.' + file_type),'') + '_' + str(date.today()) + '.' + file_type)):
                    print("Backup realizado com sucesso!")
                    Check()
                else:
                    print("Não foi possível realizar o backup!")
                    Check()
            else:
                print("Arquivo não encontrado")
                
                Check()
            
def Check():
    response = int(input("Digite [1] para retornar ao menu\nDigite [2] para SAIR\n"))
    if response == 1:
        Options()
    elif response == 2:
        os._exists(1)
    else:
        print("Opção Inválida!")
def Make_Dir():
    directory = input("Digite o nome do Novo diretório:\n")
    
    
    path = input("Digite o caminho o Diretório será criado:\n")
    
    path_dir = os.path.join(path,directory)
    
    
    
    if os.path.exists(str(path)):
        if os.path.exists(str(path_dir)):
            print("Esse Diretório já existe!")
        else:
            os.mkdir(path_dir)
            if os.path.exists(str(path_dir)):
                print("Diretório criado com sucesso!")
                Check()
            else:
                print("Não foi possível criar o Diretório!")
                Check()
    else:
        print("O caminho inserido não existe!")
        Check()

def Options():
    bkp_type = int(input("Digite [1] para Backup de Arquivos de uma pasta\nDigite [2] para backup de um arquivo específico\nDigite [3] para criar um Diretório\nDigite [4] para SAIR\n"))
    
    if bkp_type == 1:
        Backup_Mult_Files()                
    elif bkp_type == 2:  
        Backup_one_File()
    elif bkp_type == 3:
        Make_Dir()
    elif bkp_type == 4:
        os._exists(1)
    else:
        print("Opção Inválida!")
def main():
    Options()
        
        
if __name__ == "__main__":
    main()
        
        