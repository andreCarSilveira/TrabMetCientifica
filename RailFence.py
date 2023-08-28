import time
import psutil
import os


def get_app_usage(pid):
    process = psutil.Process(pid)
    cpu_usage = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    memory_bytes = memory_info.rss  # Resident Set Size (memória residente em bytes)
    return cpu_usage, memory_bytes

def cifrar_rail_fance(frase):
    cifrada = ''
    aux = frase
    frase = frase.replace(' ', '')
    str1 = ''
    str2 = ''
    cont = 0
    

    for letra in frase:
        if cont % 2 == 0:
            str1 += letra
        else:
            str2 += letra
        cont += 1

    str1 += str2
    cont = 0

    for letra in aux:
        if letra != ' ':
            cifrada += str1[cont]
            cont += 1
        else:
            cifrada += ' '
    
    cifrada = cifrada.upper()
    
    return cifrada


def decifrar_rail_fance(cifrada):
    aux = cifrada
    cifrada = cifrada.replace(' ', '')
    fraseSemEsp = ''
    fraseComEsp = ''
    cont1 = 0
    cont2 = 0
    tam = len(cifrada)

    str1 = cifrada[0 : round(tam / 2)]
    str2 = cifrada[round(tam / 2) : tam]
    
    for letra in cifrada:
        if cont1 % 2 == 0:
            fraseSemEsp += str1[cont2]
        else:
            fraseSemEsp += str2[cont2]
            cont2 += 1
        cont1 += 1

    cont1 = 0
    
    for letra in aux:
        if letra != ' ':
            fraseComEsp += fraseSemEsp[cont1]
            cont1 += 1
        else:
            fraseComEsp += ' '

    return fraseComEsp

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
            cifrada = cifrar_rail_fance(frase)
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