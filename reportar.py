import webbrowser
import os 




def repo(lista,nota_max,nota_min,media,aprobados,reprobados,listasc,listdesc):
    report =open("reporte_generado.html","w")
    report.write(
        "<!DOCTYPE html>"
    +"<html lang=\"en\">"
    +"<head>"
        +"<meta charset=\"UTF-8\">"
        +"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
        +"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
        +"<title>REPORTE ALUMNOS</title>"
    +"</head>"
    +"<style>"
        +"body {"
        +"background-image: url('fondo.jpg');"
        +"}"
        +"table, th {"
    +"border: 1px solid black;"
    +"background-color: azure;"
    +"font-size: xx-large;"
    +"font-style: oblique;"
            
    +"}"
        +"h1{"
            +"background-color: rgb(220, 207, 20);"
            +"font-style: italic;"
        +"}"
    +"</style>"
    +"<body >"
    
        +"<h1 style=\"text-align:center\">REPORTE ESTUDIANTES </h1>"
        +"<table Align=\"center\">" 
           + "<tr> "
                +"<th> Nombre </th>"
                +"<th>Punteo </th>"
            +"</tr>"

    )


    for x in lista:

        if int(x[1])>=61:
            
            report.write(
            "<tr>"
            + " <td> "+x[0]+" </td>"

            + " <td bgcolor= \"blue\"> "+"<font color=\"white\">"+str(x[1])+"</font>"+" </td>"
            )
        else:
            
            report.write(
            "<tr>"
            + " <td> "+x[0]+" </td>"

            + " <td bgcolor= \"red\"> "+"<font color=\"white\">"+str(x[1])+"</font>"+" </td>"

            )
    report.write(
            "<tr>"
            + " <td> NOTA MAXIMA </td>"

            + " <td >" + str(nota_max)+ "</td>"

            )     
    report.write(
            "<tr>"
            + " <td> NOTA MINIMA </td>"

            + " <td >" + str(nota_min)+ "</td>"

            ) 
    
    report.write(
            "<tr>"
            + " <td> PROMEDIO</td>"

            + " <td >" + str(media)+ "</td>"

            ) 
    
    report.write(
            "<tr>"
            + " <td> NUMERO APROBADOS</td>"

            + " <td >" + str(aprobados)+ "</td>"

            ) 
    report.write(
            "<tr>"
            + " <td> NUMERO REPROBADOS</td>"

            + " <td >" + str(reprobados)+ "</td>"

            ) 
    for x in listasc: 
        report.write(  
            "<tr>"
            + " <td> NOTA ASCENDENTE: </td>"

            + " <td >" + str(x) + "</td>"

            )

    for x in listdesc: 
        report.write(  
            "<tr>"
            + " <td> NOTA DESCENDENTE</td>"

            + " <td >" + str(x) + "</td>"

            )  
       
    
    report.write(
    "</tbody>"
    + "</table>"

    +"</body>"
    +"</html>"

    )
    
    report.close()
    webbrowser.open("reporte_generado.html")