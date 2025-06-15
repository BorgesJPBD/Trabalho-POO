import os
import pickle

def salvar_objeto(obj, caminho_arquivo):#Salva um objeto serializado usando pickle.
    
    try:
        with open(caminho_arquivo, "wb") as f:
            pickle.dump(obj, f)
    except Exception as e:
        print(f"Erro ao salvar em {caminho_arquivo}: {e}")

def carregar_objeto(caminho_arquivo, fallback): #Carrega um objeto de um arquivo pickle ou retorna fallback se o arquivo não existir."""
    
    if not os.path.exists(caminho_arquivo):
        return fallback
    try:
        with open(caminho_arquivo, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Erro ao carregar de {caminho_arquivo}: {e}")
        return fallback