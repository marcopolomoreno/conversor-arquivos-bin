import numpy as np
import matplotlib.pyplot as plt

def read_agilent_bin(filename):
    with open(filename, 'rb') as f:
        # Lendo os cabeçalhos
        header_length = 100  # Defina o comprimento do cabeçalho conforme necessário
        header = f.read(header_length)

        # Lendo os dados binários
        data = np.fromfile(f, dtype=np.float32)

    return header, data

def plot_data(header, data):
    # Aqui você pode processar os cabeçalhos se precisar
    # Por exemplo, extrair informações sobre a taxa de amostragem, número de pontos, etc.

    # Plotando os dados
    plt.plot(data)
    plt.xlabel('Amostras')
    plt.ylabel('Tensão')
    plt.title('Dados do Osciloscópio Agilent')
    plt.show()

if __name__ == "__main__":
    filename = 'scope_1.bin'  # Substitua com o nome do seu arquivo binário
    header, data = read_agilent_bin(filename)
    plot_data(header, data)
