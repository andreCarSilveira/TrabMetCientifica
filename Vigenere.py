import time
import psutil
import os

def vigenere_c(frase, chave):
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cifrada = ''
    deslocamento = []
    frase = frase.upper()
    chave = chave.upper()
    chave = chave.replace(' ', '')
    cont = 0

    for i in range(len(frase.replace(' ', ''))):
        deslocamento.append(caracteres.index(chave[i % len(chave)]))

    for letra in frase:
        try:
            indice = caracteres.index(letra) + deslocamento[cont]
            cifrada += caracteres[indice % 26]
            cont += 1
        except ValueError:
            cifrada += letra

    return cifrada


def get_app_usage(pid):
    process = psutil.Process(pid)
    cpu_usage = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    memory_bytes = memory_info.rss  # Resident Set Size (memória residente em bytes)
    return cpu_usage, memory_bytes



def vigenere_d(cifrada, chave):
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    frase = ''
    deslocamento = []
    cifrada = cifrada.upper()
    chave = chave.upper()
    chave = chave.replace(' ', '')
    cont = 0

    for i in range(len(cifrada.replace(' ', ''))):
        deslocamento.append(caracteres.index(chave[i % len(chave)]))

    for letra in cifrada:
        try:
            indice = caracteres.index(letra) - deslocamento[cont]
            frase += caracteres[indice % 26]
            cont += 1
        except ValueError:
            frase += letra

    return frase

if __name__ == '__main__':
    pid = os.getpid()
    start_time = time.time()

    initial_cpu_time = os.times().user + os.times().system  # Tempo de CPU antes do loop
    initial_memory = psutil.Process(pid).memory_info().rss  # Uso de RAM antes do loop

    for i in range(10):
        arq = open('file.txt')
        arq2 = open('resultado.txt', 'w')
        linhas = arq.readlines()
        for linha in linhas:
            frase = linha
            cifrada = vigenere_c(frase, 'DEAD')
            arq2.write(cifrada)

    end_time = time.time()

    final_cpu_time = os.times().user + os.times().system  # Tempo de CPU após o loop
    final_memory = psutil.Process(pid).memory_info().rss  # Uso de RAM após o loop

    execution_time = (end_time - start_time) / 10
    cpu_time = (final_cpu_time - initial_cpu_time) / 10
    cpu_percent = ((cpu_time / execution_time) * 100) / 10  # Uso de CPU em percentual
    memory_usage = (final_memory - initial_memory) / 10  # Uso de RAM total

    print(f"Tempo de execução: {execution_time:.6f} segundos")
    print(f"Tempo de CPU usado: {cpu_time:.6f} segundos")
    print(f"Uso de CPU: {cpu_percent:.2f}%")
    print(f"Uso de RAM: {memory_usage} bytes")