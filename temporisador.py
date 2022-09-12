import time

def temp(tempo):
    while tempo > 0 : 
        minutos = int(tempo/60)
        segundos = int(tempo%60)
        tempFormat = f'{minutos}:{segundos}'
        #print(tempFormat)
        print(tempFormat, end = "\r")
        time.sleep(1)
        tempo -= 1
    print("tempo esgotado!!!")

tempo = input("qual é o seu tempo??? em segundos")
temp(int(tempo))