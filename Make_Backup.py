import os
import shutil
from datetime import date

def Backup_Mult_Files():
    file_type = input("Insira o Tipo de extensão do arquivo:\n")
    
    path = input("Insira o caminho o diretório do arquivo:\n")
    entries = [f for f in os.listdir(r"" + path)]
    
    dst = input("Insira o caminho o diretório Destino:\n")
    dst = r"" + dst
    
    for file in entries:
        
        if file_type:
            if file.endswith(file_type):
                if shutil.copy2((path + '/' + file),(dst  + '/' +  file.replace((file_type),'') + '_' + str(date.today()) + file_type)):
                    print("Backup realizado com sucesso para " + file + "!\n")
                    
                else:
                    print("Não foi possível realizar o backup para " + file + "!\n")
    else: 
        teste = path.split("\\")
        dst = dst + "/" + teste[-1] + "_" + str(date.today())
        if shutil.copytree(path, dst):
            print("Backup realizado com sucesso!\n")
        else:
            print("Não foi possível realizar o backup!\n")
        
    Check()
def Backup_one_File():
    file_type = input("Insira o Tipo de extensão do arquivo:\n")
    
    path = input("Insira o caminho o diretório do arquivo:\n")
    entries = os.listdir(r"" + path)
    
    file_name = input("Insira o nome do arquivo desejado:\n")
    
    dst = input("Insira o caminho o diretório Destino:\n")
    dst = r"" + dst
    
    for file in entries:
        if file.endswith(file_type):
            
            if str(file_name + file_type) == str(file):
                if shutil.copy2((path + '/' + file),(dst  + '/' +  file.replace((file_type),'') + '_' + str(date.today()) + file_type)):
                    print("Backup realizado com sucesso!\n")
                    Check()
                else:
                    print("Não foi possível realizar o backup!\n")
                    Check()
            else:
                print("Arquivo não encontrado\n")
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
            print("Esse Diretório já existe!\n")
        else:
            os.mkdir(path_dir)
            if os.path.exists(str(path_dir)):
                print("Diretório criado com sucesso!\n")
                Check()
            else:
                print("Não foi possível criar o Diretório!\n")
                Check()
    else:
        print("O caminho inserido não existe!\n")
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
        print("Opção Inválida!\n")
def main():
    Options()
        
        
if __name__ == "__main__":
    main()
        
        
