import reportar as rp

lista_ascendentes=[]
lista_descendentes=[]
numero_aprobados=0 
numero_reprobados=0
media=0
nota_maxima=0
nota_minima=0



class Estudiante ():
    def __init__ (self,nombre, punteo):
        self.nombre = nombre
        self.punteo = punteo 




def crear_reporte(listanombre_punteo):
    rp.repo(listanombre_punteo,nota_maxima,nota_minima,media,numero_aprobados,numero_reprobados,lista_ascendentes,lista_descendentes)





def splitear(cadena,simbolo,fila,columna):
    #print("Si llego a minimo")
    temporal = ""
    listaTemporal = []
    
    for i in range(fila,len(cadena)): #Obeteniendo el tamaño del contenido del arreglo
        linea = cadena[i]   # capturo la linea de la lista de contenido por el indice i
        if fila != i:
            columna=0  #Para resetear la linea
            fila=i       
        if linea !="":
            for c in range(columna,len(linea)) : #Obeteniendo el tamaño del cadena 
                caracter=linea[c]   #capturo el caracter por el indice c
                if caracter==simbolo :
                    #listaTemporal.append(temporal.strip())
                    #temporal =""
                    return temporal,i,c
                else: 
                    if caracter != "\n" :
                        temporal +=caracter

    
        #if temporal.strip() != "":
            #listaTemporal.append(temporal.strip())
    
   # return listaTemporal # Necesito devolver dos cosas , variable token y un indice
#---------------------------------------------------------------------------------------------------------
def alumnos (cadena,simbolo):
    #listaNueva 
   
        #Laura, 17
        #datos = ['Laura' ,'17']
    lista =[]
    temporal=""
    for s in cadena:
         if s==simbolo:

            lista.append(temporal)
            temporal=""
         else:
            temporal +=s
    lista.append(temporal)

    return lista
#--------------------------------------------------------------------------------------------
def ordenarAs(unaLista):
 
    
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

    global lista_ascendentes 
    lista_ascendentes = unaLista







#--------------------------------------------------------------------------------------------------
def ordenarDes(unaLista):
   for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]<unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

   global lista_descendentes
   lista_descendentes = unaLista
#-----------------------------------------------------------------------------------------------------
def contar_elementos(lista):
    count=0
    for elementos in (lista):
        count+=1
    return count
#------------------------------------------------------------------------------------------------------
def aprobar(lista):
    notas_aprobadas=[]
    lista_elementos= [int(x)for x in lista]
    for x in lista_elementos:
        if x >= 61 :
            notas_aprobadas.append(x)
    print("ESTUDIANTES APROBADOS: ",len(notas_aprobadas))
    global numero_aprobados
    numero_aprobados=len(notas_aprobadas)
    
        
#-----------------------------------------------------------------------------------------------------
def reprobar(lista):
    notas_reprobadas =[]
    lista_elementos= [int(x)for x in lista]
    for x in lista_elementos:
        if x < 61:
            notas_reprobadas.append(x)
    print("ESTUDIANTES REPROBADOS: ",len(notas_reprobadas))
    global numero_reprobados
    numero_reprobados=len(notas_reprobadas)

#------------------------------------------------------------------------------------------------------
def maximo(lista):
    lista_elementos= [int(x)for x in lista]
    print("NOTA MÁXIMA: ",max(lista_elementos))
    global nota_maxima
    nota_maxima = max(lista_elementos)

#---------------------------------------------------------------------------------------------------------
def minimo(lista):
    lista_elementos= [int(x)for x in lista]
    print("NOTA MÍNIMA: ",min(lista_elementos))
    global nota_minima
    nota_minima=min(lista_elementos)
#---------------------------------------------------------------------------------------------------------
def promedio(lista):
  listasuma= [int(x)for x in lista]
  sumarelementos = sum(listasuma)
  num_elementos=len(lista)
  media1= sumarelementos/num_elementos
  #suma=0

  #for i in listasuma:
      #suma+=listasuma[i]
  print("PROMEDIO:", round(media1,2))
  global media
  media= round(media1,2)


  
  

    