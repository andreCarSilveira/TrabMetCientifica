import time
import psutil
import os

lista1 = ['A', 'D', 'H', 'I', 'K', 'M', 'O', 'R', 'S', 'U', 'W', 'Y', 'Z']
lista2 = ['V', 'X', 'B', 'G', 'J', 'C', 'Q', 'L', 'N', 'E', 'F', 'P', 'T']

def cifra(frase, decifrando):
    cifrada = ''
    frase = frase.upper()
    for letra in frase:
        ver = 0
        for elem in lista1:
            if letra == elem:
                letra = lista2[lista1.index(elem)]
                ver = 1
        if ver == 0:
            for elem in lista2:
                if letra == elem:
                    letra = lista1[lista2.index(elem)]
                    ver = 1
            
        cifrada += letra
    
    if decifrando:
        cifrada = cifrada.lower()
    
    return cifrada


def get_app_usage(pid):
    process = psutil.Process(pid)
    cpu_usage = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    memory_bytes = memory_info.rss  # Resident Set Size (memória residente em bytes)
    return cpu_usage, memory_bytes


# ... (seu código acima)

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
            cifrada = cifra(frase, False)
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
