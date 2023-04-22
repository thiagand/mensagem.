import time

# Especifique o caminho para o arquivo txt que você deseja ler
file_path = "C:/Users/thiag/Desktop/roger.txt"

# Especifique o tempo de espera em segundos antes de começar a escrever cada linha
wait_time = 5

# Abra o arquivo em modo de leitura
with open(file_path, 'r') as file:

    # Leia e envie linha por linha com um intervalo de tempo
    for line in file:
        time.sleep(wait_time)
        print(line.strip())
