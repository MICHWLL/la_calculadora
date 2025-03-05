# Este codigo ha sido generado por el modulo psexport 20230904-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	while True:# no hay 'repetir' en python
		print("bienvenido a la calculadora automatica ")
		print("que operacion quieres realizar el dia de hoy")
		print("1. suma")
		print("2. resta")
		print("3. multiplicacion ")
		print("4. division")
		print("5. todas las operaciones disponibles")
		opcion = float(input())
		if opcion==1:
			print("ingresa el primer numero para la suma :")
			num1 = float(input())
			print("ingresa el segundo numero para la suma :")
			num2 = float(input())
			suma = num1+num2
			print("el resultado de la suma es :",suma)
		elif opcion==2:
			print("ingresa el primer numero para la resta :")
			num1 = float(input())
			print("ingresa el segundo numero para la resta :")
			num2 = float(input())
			resta = num1-num2
			print("el resultado de la resta es :",resta)
		elif opcion==3:
			print("ingresa el primer numero para la multiplicacion :")
			num1 = float(input())
			print("ingresa el segundo numero para la multiplicacion :")
			num2 = float(input())
			multiplicacion = num1*num2
			print("el resultado de la multiplicacion es :",multiplicacion)
		elif opcion==4:
			print("ingresa el primer numero para la division :")
			num1 = float(input())
			print("ingresa el segundo numero para la division:")
			num2 = float(input())
			if num1==0 or num2==0:
				print("division no valida")
			else:
				division = num1/num2
				print("el resultado de la division es :",division)
		elif opcion==5:
			print("ingresa el primer numero :")
			num1 = float(input())
			print("ingresa el segundo numero :")
			num2 = float(input())
			suma = num1+num2
			print("el resultado de la suma es :",suma)
			resta = num1-num2
			print("el resultado de la resta es :",resta)
			multiplicacion = num1+num2
			print("el resultado de la multiplicacion es :",multiplicacion)
			if num1==0 or num2==0:
				print("division no valida")
			else:
				division = num1/num2
				print("el resultado de la division es :",division)
		else:
			print("numero invalido, por favor intenta nuevamente")
		print("desea realizar otra operacion? si (0) no (1)")
		salida = input()
		if salida !=0  : break

