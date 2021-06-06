usuario = input("Informe o usuário do sistema: ")

flavio = usuario == "Flávio"
douglas = usuario == "Douglas"
nico = usuario == "Nico"

if(flavio):
    print("Seja bem-vindo Flávio!")
elif(douglas):
    print("Seja bem-vindo Douglas!")
elif(nico):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")