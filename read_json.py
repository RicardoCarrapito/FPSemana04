import json
try:
    caminho=input()
    file= open(caminho,"rt",encoding="utf8")
    data= file.read()

    data= json.loads(data)
    print(data)
    file.close()

except Exception:
    print("Ocorreu um erro!")
finally:
    print("Processo concluído!")