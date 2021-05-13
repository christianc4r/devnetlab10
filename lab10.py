equipos = []   

def ShowHostnames():
    for i in equipos:
        print(i["hostname"])

def ShowMac():
    for i in equipos:
        print(i["dir_mac"])

def ShowIp():
    for i in equipos:
        print(i["dir_ip"])
def ShowDesc():
    for i in equipos:
        print(i["desc"])


cond = True
print("######                                                                                                 ")
print(" #     # # ###### #    # #    # ###### #    # # #####   ####                                           ") 
print(" #     # # #      ##   # #    # #      ##   # # #    # #    #                                          ")
print(" ######  # #####  # #  # #    # #####  # #  # # #    # #    #                                          ") 
print(" #     # # #      #  # # #    # #      #  # # # #    # #    #                                          ") 
print(" #     # # #      #   ##  #  #  #      #   ## # #    # #    #                                          ") 
print(" ######  # ###### #    #   ##   ###### #    # # #####   ####                                           ") 
print("                                                                                                        ")
print(" ###                                                                                                    ")
print("  #  #    #  ####  #####  ######  ####  ######     ####  #    #    ######  ####  #    # # #####   ####  ")
print("  #  ##   # #    # #    # #      #      #         #      #    #    #      #    # #    # # #    # #    # ")
print("  #  # #  # #      #    # #####   ####  #####      ####  #    #    #####  #    # #    # # #    # #    # ")
print("  #  #  # # #  ### #####  #           # #              # #    #    #      #  # # #    # # #####  #    # ")
print("  #  #   ## #    # #   #  #      #    # #         #    # #    #    #      #   #  #    # # #      #    # ")
print(" ### #    #  ####  #    # ######  ####  ######     ####   ####     ######  ### #  ####  # #       ####  ")

                                                                                                     
while cond:
    hostname=input("Ingrese el nombre: ")
    dir_ip=input("Ingrese su direccion IP: ")
    dir_mac=input("Ingrese la direccion MAC: ")
    desc=input("Ingrese la descripcion: ")
    disp={}
    disp["hostname"] = hostname
    disp["dir_ip"] = dir_ip
    disp["dir_mac"] = dir_mac
    disp["desc"] = desc
    equipos.append(disp)
    option=input("Desea ingresar otro equipo?").upper()
    opt = ["S","SI","Y","YES"]
    if option in opt:
        continue
    else:
        break
print(" _ __ ___   ___ _ __  _   _ ")
print(" | '_ ` _ \ / _ \ '_ \| | | |")
print(" | | | | | |  __/ | | | |_| |")
print(" |_| |_| |_|\___|_| |_|\__,_|")
print(" 1 - Ver todos los nombres de los equipos.")                     
print(" 2 - Mostrar todas las direcciones MAC")
print(" 3 - Mostrar todas las IPs.")
print(" 4 - Mostrar todas las descripciones.")

opt2 = int(input())
if opt2 == 1:
    ShowHostnames()
elif opt2 == 2:
    ShowMac()
elif opt2 == 3:
    ShowIp()
elif opt2 == 4:
    ShowDesc()
else:
    print("Opcion Invalida")



