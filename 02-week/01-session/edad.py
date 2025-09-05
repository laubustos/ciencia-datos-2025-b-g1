edad = int(input("Digite la edad de la persona: "))

if edad > 0 and edad < 130:
  if edad >= 18:
    print("Mayor de edad")
  else:
    print("Menor de edad")
else:
  print("Edad incorrecta")