#Nos han pedido desarrollar una aplicación móvil para reducir comportamientos
#inadecuados para el ambiente.
#a) Te toca escribir un programa que simule el proceso de Login.

#Para ello el programa debe preguntar al usuario la contraseña,
#y no le permita continuar hasta que la haya ingresado correctamente.

contraseña = 54
intentos = 1
print("Este es un programa para simular un logueo\n")

clave = int(input("Ingrese su contraseña: \n"))

while clave != contraseña:
            print("la contraseña es incorrecta.")            
            clave = int(input("Ingrese su contraseña: \n"))            
            intentos = intentos + 1
            if intentos >= 4:
                print("Intente loguearse más tarde.\n")
                break
            
else:
       print("siga con las operaciones a realizar...")
#comentario para probar modificación en git
#COMENTARIOPARAPROBRPULL     


                  
           

