contrasena_correcta = "python123"

while True:
    contrasena_usuario = input("dame una contraseña: ")
    if contrasena_correcta == contrasena_usuario:
        print("correcto")
        break
    else:
        print("contraseña incorrecta")
