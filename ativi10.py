x = int(input("Digite a sua idade"))
if  x > 0 and x < 12:
    print("criança")
elif x > 12 and x <= 17:
    print("adolescente")
elif x >= 18 and x <= 59:
    print("adulto")
else:
    print("idoso")