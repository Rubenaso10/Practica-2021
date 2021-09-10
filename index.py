from archivo1 import Estudiante, alumnos, aprobar, ordenarAs, ordenarDes, reprobar, splitear,contar_elementos,promedio,maximo,minimo,crear_reporte

from colorama import init
from colorama import Fore, Back, Style
import easygui as eg



contenido_archivo=[]
contenido_nombrepunteo = []
notas= []

init(autoreset=True)





def cargarArchivo():
    
    global contenido_archivo
    global contenido_nombrepunteo,notas
    global sep1,sep2
    global lista2,lista3,listanueva

    contenido_archivo.clear()
    extension = ["*.py","*.lfp"]

    archivo = eg.fileopenbox(msg="Abrir archivo",title="Control: Practica Lenguajes",default='',filetypes=extension)
    efe = open (archivo,"r",5,"utf-8")                       
    for linea in efe.readlines():
        if linea != "\n":
            contenido_archivo.append(linea)
            print(Fore.RED+linea.rstrip())

    efe.close()

    fila=0
    col=0

    contenido_archivo[-1]=contenido_archivo[-1] +"#"

    sep1, fila, col = splitear(contenido_archivo, "=", fila, col)
    lista1 = alumnos(sep1,"=")
    #print(lista1)
    print(sep1)

    
    while True:
        sep2,fila,col=splitear(contenido_archivo,"<",fila,col)

        sep2,fila,col=splitear(contenido_archivo,">",fila,col+1)

        lista2=alumnos(sep2,";")
        #print(lista2[0])
        listanueva = Estudiante(lista2[0],lista2[1])
        
        print(sep2)
        

        #print(lista2)
        contenido_nombrepunteo.append(lista2) #Para contar cuantos alumnos hay 
        
        

        
        if "<" not in contenido_archivo[fila+1] :
            break

    for x in range(len(contenido_nombrepunteo)):
        notas.append(contenido_nombrepunteo [x][1])
            
  
    
  
    
    

      
    
    sep3,fila,col = splitear(contenido_archivo, "}",fila,col)
    sep3,fila,col = splitear(contenido_archivo, "#",fila,col+1)
    
    lista3 = alumnos(sep3,",")
    print(sep3)

    print(contenido_nombrepunteo)
    for x in contenido_nombrepunteo:
        print(x[0])
        print(x[1])
       
    print(lista3)
    #print(lista3)
    #print(lista3[2])
    
    #print (notas)
  

def mostrar_datos():
    print("NOMBRE DEL CURSO: " ,sep1)
    print( "TOTAL DE ALUMNOS:  " ,contar_elementos(contenido_nombrepunteo) )
    

    if "ASC" in lista3:
        print("ORDEN ASCENDENTE")
        ordenarAs(notas)
        print(notas)
    if "DESC" in lista3:
        print("ORDEN DESCENDENTE")
        ordenarDes(notas)
        print(notas)

    if "AVG" in lista3:
        promedio(notas)
       

    if "MIN" in lista3:
        minimo(notas)

    if "MAX" in lista3:
        
        maximo(notas)
    
    if "REP" in lista3:
        reprobar(notas)

    if "APR" in lista3:
        aprobar(notas)



        





    
  
    




    

def menu():
    funcion = True
    while funcion:

     
        print ( Fore.GREEN+"\t1 -Cargar Archivo" + " \U0001F4C1")
        print (Fore.LIGHTYELLOW_EX+"\t2 -Mostrar reporte en consola"+ "\U0001F4DD")
        print (Fore.CYAN +"\t3 -Exportar reporte"+"  \U0001F4E4")
        print (Fore.RED+"\t4 -Salir"+ " \U0001F44B")
        

        

        opcion = input("Ingrese opcion---->   ")
        if  opcion=="1":
            cargarArchivo()
            pass
        elif opcion=="2":
            mostrar_datos()
            pass
        elif opcion =="3":
            crear_reporte(contenido_nombrepunteo)
            
        elif opcion =="4":
            break
        
             
        else:
            print("")
            input("No ha pulsado ninguna opción correcta, pulse enter para regresar al menú principal")
            
#primersplit = splitear (contenido_archivo,'=')


menu()


