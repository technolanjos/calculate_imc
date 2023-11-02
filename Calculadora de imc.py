peso=float(input("imforme seu peso:"))
altura=float(input("informe sua altura:"))
imc=peso/(pow(altura ,2))
print(f"seu imc é:{imc :.2f}")

if imc <=18.5:
    print("baixo")
elif 18.5 < imc <=24.9:
    print("normal")
elif 25.0 < imc <=29.9:
    print("sobrepeso")
elif 30.0 < imc <=34.9:
    print("obesidade")
elif 35.0 < imc <= 39.9:
     print("obesidade Morbida")
else:
    print("obesidade Morbida muito grave")