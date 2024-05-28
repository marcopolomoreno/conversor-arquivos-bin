import numpy as np

def read_agilent_bin(filename):
    with open(filename, 'rb') as f:
        # Lendo os cabeçalhos
        header_length = 100  # Defina o comprimento do cabeçalho conforme necessário
        header = f.read(header_length)

        # Lendo os dados binários
        data = np.fromfile(f, dtype=np.float32)

    return header, data

def save_as_txt(filename, data):
    with open(filename, 'w') as f:
        for value in data:
            f.write(f"{value}\n")

def save_as_csv(filename, data):
    np.savetxt(filename, data, delimiter=",")

if __name__ == "__main__":
    filename = 'scope_1.bin'  # Substitua com o nome do seu arquivo binário
    header, data = read_agilent_bin(filename)
    
    # Escolha um dos métodos de salvamento abaixo:
    
    # Salvar como texto simples (.txt)
    save_as_txt('dados_convertidos.txt', data)
    
    # OU
    
    # Salvar como CSV (.csv)
    # save_as_csv('dados_convertidos.csv', data)
