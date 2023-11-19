def consulta_saldo():

    print("Su saldo actuales de:$")

def  consulta_datos():
 
    print("La cantidad de datos restantes es de:")

def consulta_prestamo():

    print ("El saldo de prestamo es de:")

def compra_paquete():
    print("1: 4G por solo $1.10.")
    print("2: 6G por solo $2.10.")
    print("3: 8G por solo $3.10.")
    try:
        print("\t") 
        opc=int(input("Ingrese la cantidad que desea:"))
        print("\t") 
        
        if opc > 3 or opc <=0:
            raise ValueError("Opción no valida, debe de ser un valor del 1 al 3.") 
        elif opc==1:
            
            print("Su paquete de: 4G más faceboock y youtube.Esta casi listo,espere el SMS de confirmación.")
        elif opc==2:

            print("Su paquete de: 6G más faceboock y youtube,más 10 días de whatssap. Esta casi listo,espere el SMS de confirmación.")
        else:
            
            print("Su paquete de: 8G más faceboock y youtube, más 10 días de whatssap con titok incluido. Esta casi listo,espere el SMS de confirmación.")    
    except ValueError as ve:
        print("\t") 
        print(f"Eror:{ve}")


def atencion_cliente():
     print("\t") 
     print("1.Numero de télefono")
     print("2.Planes pospago")
     print("3.Paquete duo SIM")

     try:
        print("\t") 
        cion = int(input("Ingrese la opcion que desea aplicar:"))
        print("\t") 
        
        if cion > 3:
            
            raise ValueError("Opción no valida, debe de ser un valor del 1 al 3.")
        elif cion==1:
            
            print("Si desea saber su numero llame al:12345678")
        elif cion==2:

            print("Para mayor información llame al:98765432")
        else:
            
            print("Puedes llamar al 43215678 para mayor información:")
     except ValueError as ve:
        print("\t") 
        print(f"Eror:{ve}")

def mostrar_menu():
  print("\t") 
  print("1_Consulta de saldo")
  print("2_Consulta de datos")
  print("3_Consulta de prestamo")
  print("4_Compra de paquetes")
  print("5_Atencion al cliente") 
  print("Oproma 0 si desea salir.")
  print("\t") 
while True:
    mostrar_menu()

    try:
        print("\t") 
        opcion=int(input("Elija la opcion que desea:"))
        print("\t") 
        
        if opcion==0:
            print("Mucahas gracias por prefrirnos.¡Hasta luego! ")
            break
        elif opcion==1:

            consulta_saldo()
        elif opcion==2:

            consulta_datos()
        elif opcion==3:

            consulta_prestamo()
        elif opcion==4:

            compra_paquete()

        elif opcion==5:

            atencion_cliente()
        elif opcion>5 or opcion <0:
            raise ValueError("Opcion no valida.Debe de elejir entre 1 y 5.")
    except ValueError as ve:
      print("\t") 
      print(f"Error:¨{ve}")
