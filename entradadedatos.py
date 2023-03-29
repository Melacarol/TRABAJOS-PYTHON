num1=int(input("ingresar primer numero: "))
num2=int(input("ingresar el segundo numero: "))

x=num1 == num2
#opcion 1
print("los numeros: " + str(num1) + " y " + str(num2) + " son iguales: " + str(x))
#opcion 2
print("los numeros:" , (num1), "y", (num2),"son iguales:",(x))
#opcion 3
print(f"los numeros: {num1} y {num2} son iguales: {x}")
#opcion 4
print("los numeros: {} y {} son iguales: {}\n".format(num1,num2,x))

y=num1 != num2
#opcion 1
print("los numeros: " + str(num1) + " y " + str(num2) + " son diferentes: " + str(y))
#opcion 2
print("los numeros:" , (num1), "y", (num2),"son diferentes:",(y))
#opcion 3
print(f"los numeros: {num1} y {num2} son diferentes: {y}")
#opcion 4
print("los numeros: {} y {} son diferentes: {}\n".format(num1,num2,y))

z=num1>num2
#opcion 1
print("entre los numeros: " + str(num1) + " y " + str(num2) + " el primer numero es mayor: " + str(z))
#opcion 2 
print("entre los numeros:" , (num1), "y", (num2),"el primer numero es mayor:",(z))
#opcion 3
print(f"entre los numeros: {num1} y {num2} el primer numero es mayor: {z}")
#opcion 4
print("entre los numeros: {} y {} el primer numero es mayor: {}\n".format(num1,num2,z))

a=num1<=num2
#opcion 1
print("entre los numeros: " + str(num1) + " y " + str(num2) + " el segundo es mayor o igual que el primero: " + str(a))
#opcion 2
print("entre los numeros:" , (num1), "y", (num2),"el segundo es mayor o igual que el primero:",(a))
#opcion 3
print(f"entre los numeros: {num1} y {num2} el segundo es mayor o igual que el primero: {a}")
#opcion 4
print("entre los numeros: {} y {} el segundo es mayor o igual que el primero: {}".format(num1,num2,a))
