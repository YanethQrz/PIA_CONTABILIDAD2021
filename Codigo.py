import sys
import datetime
import math

separador=("*"*50)
menu=1
listanombreproduc=[]
listaunidadavender=[]
listaprecioventa=[]
listatotal=[]
listaimportedeventa1=[]
listaimportedeventa2=[]
lista_invfinal1=[]
lista_invfinal2=[]
lista_invinicial1=[]
lista_invinicial2=[]
lista_total_unidades1=[]
lista_total_unidades2=[]
lista_unidad_producir=[]
lista_suma_camisas_producir=[]
lista_nombre_material=[]
lista_total_materiales=[]
lista_req=[]
lista_total_total_materiales=[]
listamat1=[]
listamat2=[]
compras_totales=[]
lista8_1=[]
lista8_2=[]
listareu=[]
listanom8=[]
lista_importeMOD_1=[]
lista_total_horas_1=[]
lista_importeMOD_2=[]
lista_total_horas_2=[]
lista9_1=[]
lista9_2=[]
contadorp=1
contadoru=0
contador3=0
contador4=0
contador5=0
contador6=0
contador7=0
contador8=0
contador9=0
contador10=0
contador11=0
contador12=0
contador13=0
contador14=0
contador15=0
contador16=0
contador17=0
contador18=0
contador19=0
contador20=0
contador21=0
contador22=1
contador23=0
contador24=0
contador26=0
contador27=0
contador28=0
contadorespecial=0
primer="Primer Semestre"
segundo="Segundo Semestre"
try:
    while menu==1:
        print(separador+" Bienvenido al Programa "+separador)
        print("")
        print("-"*15+" Este programa realiza el Presupuesto Maestro "+"-"*15)
        print("")
        #Preguntar datos y agregar a variables
        año=int(input("Dime el año 1 : "))
        año2=int(input("Dime el año 2: "))
        print(separador)
        productocon=int(input("Dime cuantos productos son :"))
        print(separador)
        for producto in range(productocon):
            nombre=input(f"Dime el nombre del Producto {contadorp} :")
            listanombreproduc.append(nombre)
            contadorp=contadorp+1
        print(separador)
        #TABLA 1
        print("-"*15+"1-Presupuesto de Ventas"+"-"*15)
        print("")
        for producto in listanombreproduc:
            unidadavender=int(input(f"Dime las unidades a vender de el producto {listanombreproduc[contadoru]} del {primer} : "))
            listaunidadavender.append(unidadavender)

            preciodeventa=float(input(f"Dime el precio de Venta de el producto {listanombreproduc[contadoru]} del {primer} : "))
            listaprecioventa.append(preciodeventa)
            print(separador)
            listaimportedeventa1.append(unidadavender*preciodeventa)

            unidadavender2=int(input(f"Dime las unidades a vender de el producto {listanombreproduc[contadoru]} del {segundo} : "))
            listaunidadavender.append(unidadavender2)

            preciodeventa2=float(input(f"Dime el precio de Venta de el producto {listanombreproduc[contadoru]} del {segundo} : "))
            listaprecioventa.append(preciodeventa2)
            print(separador)
            listaimportedeventa2.append(unidadavender2*preciodeventa2)
            
            contadoru=contadoru+1
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"1-Respuestas del Presupuesto de Ventas"+"-"*15 +"\n" )
        archivoA.write("\n" )
        archivoA.write("-"*30 +"\n" )

        for nombre in listanombreproduc:
            texto1=str(nombre)
            archivoA.write(texto1+":" +"\n" )

            archivoA.write("\n" )
            archivoA.write("PRIMER SEMESTRE:" +"\n" )

            texto2=str(listaunidadavender[contador3])
            archivoA.write("UNIDADES A VENDER: "+texto2+"\n" )

            texto3=str(listaprecioventa[contador3])
            archivoA.write("PRECIO DE VENTA: "+texto3+"\n" )

            texto4=str(listaimportedeventa1[contador4])
            archivoA.write("IMPORTE DE VENTA: "+texto4+"\n" )

            contador3=contador3+1
            archivoA.write("\n" )
            archivoA.write("SEGUNDO SEMESTRE: "+"\n" )

            texto5=str(listaunidadavender[contador3])
            archivoA.write("UNIDADES A VENDER: "+texto5+"\n" )


            texto6=str(listaprecioventa[contador3])
            archivoA.write("PRECIO DE VENTA: "+texto6+"\n" )

            texto7=str(listaimportedeventa2[contador4])
            archivoA.write("IMPORTE DE VENTA: "+texto7+"\n" )
            archivoA.write("-"*30 +"\n" )

            
            contador3=contador3+1
            contador4=contador4+1
        totalventasS1=(sum(listaimportedeventa1))
        totalventasS2=(sum(listaimportedeventa2))
        VENTASTOTALES=(totalventasS1+totalventasS2)
        archivoA.write("\n" )
        archivoA.write("Totales Primer Semestre: "+str(totalventasS1)+"\n" )
        archivoA.write("Totales Segundo Semestre: "+str(totalventasS2)+"\n" )
        archivoA.write("Total de Ventas por Semestre: "+str(VENTASTOTALES)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        # FINAL TABLA 1
        #TABLA 2
        print(separador)
        print("-"*15+"2-Determinación del saldo de Clientes y Flujo de Entradas"+"-"*15)
        print("")
        saldoCliente=float(input("Dime el saldo de Clientes del Balance General : "))
        totalCliente=(saldoCliente+VENTASTOTALES)

        porcentaje=float(input("Cuanto porcentaje del total de Ventas se va aplicar por cobranza ejemplo(.80) : "))
        cobranza=(VENTASTOTALES*porcentaje)
        totalEntradas=(cobranza+saldoCliente)
        SALDODECLIENTES=(totalCliente-totalEntradas)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("\n" )
        archivoA.write("-"*15+"2-Determinacion de saldo de clientes y flujo de entradas"+"-"*15 +"\n" )
        print("")
        archivoA.write("Saldo de Clientes "+str(año)+": "+str(saldoCliente)+"\n" )

        archivoA.write("Ventas "+str(año2)+": "+str(VENTASTOTALES)+"\n" )

        archivoA.write("Total de Clientes "+str(año2)+": "+str(totalCliente)+"\n" )

        
        archivoA.write("\n" )
        archivoA.write("Entradas de Efectivo: "+"\n" )

        archivoA.write("Por cobranza del "+str(año)+": "+str(saldoCliente)+"\n" )

        archivoA.write("Por cobranza del "+str(año2)+": "+str(cobranza)+"\n" )
        archivoA.write("\n" )
        archivoA.write("Total de Entradas del "+str(año2)+": "+str(totalEntradas)+"\n" )

        
        archivoA.write("Saldo de Clientes del "+str(año2)+": "+str(SALDODECLIENTES)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        #FINAL TABLA 2

         #TABLA 3
        #PRESUPUESTO DE PRODUCCION
        print(separador)
        print("-"*15+"3-Presupuesto de Producción"+"-"*15)

        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("\n" )
        archivoA.write("-"*15+"3-PRESUPUESTO DE PRODUCCION"+"-"*15 +"\n" )
        for producto in listanombreproduc:
            archivoA.write("\n" )
            print("")
            print("PRIMER SEMESTRE")
            print("")
            archivoA.write("PRIMER SEMESTRE :"+"\n" )
            archivoA.write(producto+":"+"\n")
            inv_final_1=float(input(f"Dime le inventario final de {listanombreproduc[contador5]} del primer semestre: "))
            lista_invfinal1.append(inv_final_1)
            archivoA.write("Inventario final de "+str(listanombreproduc[contador5])+" del primer semestre"+": "+str(inv_final_1)+"\n" )
            
            total_unidades1 = listaunidadavender[contador6] + lista_invfinal1[contador7]
            lista_total_unidades1.append(total_unidades1)
            archivoA.write("Total de unidades : "+str(total_unidades1)+"\n" )

            inv_inicial_1=float(input(f"Dime el inventario inicial de {listanombreproduc[contador5]} del primer semestre: "))
            lista_invinicial1.append(inv_inicial_1)
            archivoA.write("Inventario inicial : "+str(inv_inicial_1)+"\n" )

            lista_unidad_producir.append(total_unidades1-inv_inicial_1)
            archivoA.write("Unidades a Producir: "+str(lista_unidad_producir[contador8])+"\n" )
            contador8=contador8+1


            print("")
            print("SEGUNDO SEMESTRE")
            print("")
            archivoA.write("\n" )
            archivoA.write("SEGUNDO SEMESTRE :"+"\n" )
        
            inv_final_2=float(input(f"Dime le inventario final de {listanombreproduc[contador5]} del segundo semestre: "))
            lista_invfinal2.append(inv_final_2)
            archivoA.write("Inventario final de "+str(listanombreproduc[contador5])+" del segundo semestre"+": "+str(inv_final_2)+"\n" )
            
            contador6=contador6+1
            
            total_unidades2 = listaunidadavender[contador6] + lista_invfinal2[contador7]
            lista_total_unidades2.append(total_unidades2)
            archivoA.write("Total de unidades : "+str(total_unidades2)+"\n" )
            

            inv_inicial_2=(lista_invfinal1[contadorespecial])
            contadorespecial=contadorespecial+1
            lista_invinicial2.append(inv_inicial_2)
            archivoA.write("Inventario inicial : "+str(inv_inicial_2)+"\n" )
            print(separador)

            lista_unidad_producir.append(total_unidades2-inv_inicial_2)
            archivoA.write("Unidades a Producir: "+str(lista_unidad_producir[contador8])+"\n" )

            
            x=lista_unidad_producir[contador9]
            contador9=contador9+1
            y=lista_unidad_producir[contador9]
            total=(x+y)
            lista_suma_camisas_producir.append(total)
            archivoA.write("\n" )
            archivoA.write("TOTAL "+str(año2)+" primer semestre y segundo: "+str(lista_suma_camisas_producir[contador10])+"\n" )
            archivoA.write("--------------------------------" +"\n" )


            contador5=contador5+1
            contador6=contador6+1
            contador7=contador7+1
            contador8=contador8+1
            contador9=contador9+1
            contador10=contador10+1
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        print("")
        print(separador)

        #TABLA 4
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("\n" )
        print("-"*15+"4-PRESUPUESTO DE REQUERIMIENTO DE MATERIALES" +"-"*15 +"\n" )
        archivoA.write("-"*15+"4-PRESUPUESTO DE REQUERIMIENTO DE MATERIALES" +"-"*15 +"\n" )

        x=lista_unidad_producir[contador12]
        contador12=contador12+1
        y=lista_unidad_producir[contador12]
        suma=(x+y)

        print("")
        cuantos=int(input("Cuantos materiales tienes :"))
        print("")
        for material in range(cuantos):
            material=input("Dime el nombre del material : ")
            lista_nombre_material.append(material)
        print(separador)

        
        #SEMESTRE 1
        for producto in listanombreproduc:
            print("")
            archivoA.write("\n" )
            print("PRIMER SEMESTRE")
            archivoA.write(producto+":"+"\n" )
            archivoA.write("PRIMER SEMESTRE:"+"\n" )
            archivoA.write("\n" )
            archivoA.write("Unidades a producir:"+str(lista_unidad_producir[contador21])+"\n" )
            archivoA.write("\n" )
            contador13=0
            contador16=0
            for material in lista_nombre_material:
                
                archivoA.write("MATERIAL "+str(lista_nombre_material[contador13])+":"+"\n" )
                

                for req in range(1):
                    print(producto)
                    print("")
                    requerimientoM=float(input(f"Dime el requerimiento de Material {material}: "))
                    lista_req.append(requerimientoM)
                print(separador)
                
                x=(lista_unidad_producir[contador21]*lista_req[contador15])
                lista_total_materiales.append(x)
                archivoA.write("Requerimiento de material:"+str(lista_req[contador14])+"\n" )
                archivoA.write("TOTAL DE MATERIAL "+str(lista_nombre_material[contador16])+":"+str(lista_total_materiales[contador17])+"\n" )
                archivoA.write("\n" )
                listamat1.append(x)
               
                contador13=contador13+1
                contador14=contador14+1
                contador15=contador15+1
                contador16=contador16+1
                contador17=contador17+1
            contador21=contador21+2
                
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.close()
        print("")

        #SEMESTRE 2
        contador25=1
        contador14=0
        contador15=0
        contador17=0
        lista_total_materiales=[]
        archivoA=open("./respuestas.txt" , 'a')
        for producto in listanombreproduc:
            archivoA.write("\n" )
            archivoA.write(producto+":"+"\n" )
            archivoA.write("SEGUNDO SEMESTRE:"+"\n" )
            archivoA.write("\n" )
            archivoA.write("Unidades a producir:"+str(lista_unidad_producir[contador25])+"\n" )
            archivoA.write("\n" )
            contador13=0
            contador16=0
            for material in lista_nombre_material:
                
                archivoA.write("MATERIAL "+str(lista_nombre_material[contador13])+":"+"\n" )
                
                
                x=(lista_unidad_producir[contador25]*lista_req[contador15])
                lista_total_materiales.append(x)
                archivoA.write("Requerimiento de material:"+str(lista_req[contador14])+"\n" )
                archivoA.write("TOTAL DE MATERIAL "+str(lista_nombre_material[contador16])+":"+str(lista_total_materiales[contador17])+"\n" )
                archivoA.write("\n" )
                listamat2.append(x)
               
                contador13=contador13+1
                contador14=contador14+1
                contador15=contador15+1
                contador16=contador16+1
                contador17=contador17+1
            contador25=contador25+2
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )

        archivoA.write("TOTAL DE REQUERIMIENTOS:" +"\n" )
        archivoA.write("\n" )
        listaMateriales=[]
        materialA1=sum(listamat1[0::3])
        listaMateriales.append(materialA1)

        materialB1=sum(listamat1[1::3])
        listaMateriales.append(materialB1)

        materialC1=sum(listamat1[2::3])
        listaMateriales.append(materialC1)

        materialA2=sum(listamat2[0::3])
        listaMateriales.append(materialA2)

        materialB2=sum(listamat2[1::3])
        listaMateriales.append(materialB2)

        materialC2=sum(listamat2[2::3])
        listaMateriales.append(materialC2)

        archivoA.write("PRIMER SEMESTRE :" +"\n" )
        
        archivoA.write("MATERIAL A  :" +str(materialA1)+"\n" )
        archivoA.write("MATERIAL B  :" +str(materialB1)+"\n" )
        archivoA.write("MATERIAL C  :" +str(materialC1)+"\n" )
        archivoA.write("\n" )

        archivoA.write("SEGUNDO SEMESTRE :" +"\n" )
        archivoA.write("MATERIAL A  :" +str(materialA2)+"\n" )
        archivoA.write("MATERIAL B  :" +str(materialB2)+"\n" )
        archivoA.write("MATERIAL C  :" +str(materialC2)+"\n" )
        archivoA.write("\n" )

        archivoA.write("FINALES :" +"\n" )
        materialAT=(materialA1+materialA2)
        materialBT=(materialB1+materialB2)
        materialCT=(materialC1+materialC2)

        archivoA.write("MATERIAL TOTAL A :" +str(materialAT)+"\n" )
        archivoA.write("MATERIAL TOTAL B  :" +str(materialBT)+"\n" )
        archivoA.write("MATERIAL TOTAL C  :" +str(materialCT)+"\n" )

        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n" )
        archivoA.close()
        print("")
        print(separador)
    # FIN TABLA 4

        #TABLA 5 
        #semestre 1
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"5-PRESUPUESTO DE COMPRAS DE MATERIALES" +"-"*15 +"\n" )
        print("-"*15+"5-PRESUPUESTO DE COMPRAS DE MATERIALES" +"-"*15)
        archivoA.write("\n" )
        print("")
        for material in lista_nombre_material:
            archivoA.write("PRIMER SEMESTRE:"+"\n")
            print("PRIMER SEMESTRE : ")
            print("")
            archivoA.write("\n" )
            archivoA.write("MATERIAL "+material+" :"+"\n" )
            archivoA.write("Requerimiento de Materiales: "+str(listaMateriales[contador23])+"\n")
            inventarioFinal=int(input(f"Dime el inventario Final {material} :  "))
            listareu.append(inventarioFinal)

            archivoA.write("Inventario Final: "+str(inventarioFinal)+"\n")
            total_materiales=(listaMateriales[contador23]+inventarioFinal)
            archivoA.write("Total de Materiales: "+str(total_materiales)+"\n")

            inventarioInicial=int(input(f"Dime el inventario Inicial {material} :"))
            archivoA.write("Inventario Inicial: "+str(inventarioInicial)+"\n")

            material_comprar=(total_materiales-inventarioInicial)
            archivoA.write("Material a Comprar : "+str(material_comprar)+"\n")

            precio_compra=int(input(f"Dime el precio de compra {material} : "))
            print(separador)
            archivoA.write("Precio de Compra : "+str(precio_compra)+"\n")

            total_material=(material_comprar * precio_compra)
            compras_totales.append(total_material)
            archivoA.write("TOTAL DE MATERIAL "+material+" en $ : "+str(total_material)+"\n")
            archivoA.write("\n" )
            contador23=contador23+1
        
        archivoA.write("COMPRAS TOTALES DEL PRIMER SEMESTRE : "+str(sum(compras_totales))+"\n")
        archivoA.write("\n" )
        

        # semestre 2
        listapreciocompra=[]
        archivoA.write("\n" )
        print("")
        for material in lista_nombre_material:
            archivoA.write("SEGUNDO SEMESTRE:"+"\n")
            print("SEGUNDO SEMESTRE : ")
            print("")
            archivoA.write("\n" )
            
            archivoA.write("MATERIAL "+material+" :"+"\n" )
            archivoA.write("Requerimiento de Materiales: "+str(listaMateriales[contador23])+"\n")
            
            inventarioFinal=int(input(f"Dime el inventario Final {material} :  "))

            archivoA.write("Inventario Final: "+str(inventarioFinal)+"\n")
            total_materiales=(listaMateriales[contador23]+inventarioFinal)
            archivoA.write("Total de Materiales: "+str(total_materiales)+"\n")

            inventarioInicial=(listareu[contador24])
            contador24=contador24+1
            archivoA.write("Inventario Inicial: "+str(inventarioInicial)+"\n")

            material_comprar=(total_materiales-inventarioInicial)
            archivoA.write("Material a Comprar : "+str(material_comprar)+"\n")

            precio_compra=int(input(f"Dime el precio de compra {material} : "))
            listapreciocompra.append(precio_compra)
            print(separador)
            archivoA.write("Precio de Compra : "+str(precio_compra)+"\n")

            total_material=(material_comprar*precio_compra)
            compras_totales.append(total_material)
            archivoA.write("TOTAL DE MATERIA "+material+" en $ : "+str(total_material)+"\n")
            archivoA.write("\n" )
            contador23=contador23+1
        
        archivoA.write("COMPRAS TOTALES DEL SEGUNDO SEMESTRE : "+str(sum(compras_totales[3::1]))+"\n")
        archivoA.write("\n" )
        # ESTO ES LO QUE USARAS LUIS LA LISTA QUE SE LLAMA  compras_totales que es igual:  $2,141,010 
        archivoA.write(" TOTAL "+str(año2)+" : "+str(sum(compras_totales))+"\n")
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n" )
        archivoA.close()

        #TABLA 6
        print("")
        print(separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"6-Determinacion del saldo de Proveedores y Flujo de Salidas" +"-"*15 +"\n" )
        print("-"*15+"6-Determinacion del saldo de Proveedores y Flujo de Salidas" +"-"*15)
        archivoA.write("\n" )
        print("")
        saldo_proveedores= float(input(f"Dime el saldo de los proveedores {año} :  "))
        archivoA.write("Saldo de los proveedores "+str(año)+" : "+str(saldo_proveedores)+"\n")
        compras_totales_suma=sum(compras_totales)
        archivoA.write("Compras totales "+str(año2)+" : "+str(compras_totales_suma)+"\n")
        total_proveedores= (saldo_proveedores+ (compras_totales_suma))
        archivoA.write("Total de Proveedores "+str(año2)+" : "+str(total_proveedores)+"\n")
        archivoA.write("\n" )
        archivoA.write("Salidas de Efectivo :"+"\n" )
        porcentaje_1= float(input(f"Cuanto porcentaje del Total  de proveedores deseas aplicar {año2}; ejemplo(.30): "))
        por_proveedores= (compras_totales_suma*porcentaje_1)
        archivoA.write("Por provedores del "+str(año)+" : "+str(saldo_proveedores)+"\n" )
        archivoA.write("Por provedores del "+str(año2)+" : "+str(por_proveedores)+"\n" )
        
        total_salidas= (saldo_proveedores + por_proveedores)
        archivoA.write("Total de Salidas "+str(año2)+" : "+str(total_salidas)+"\n" )
        
        saldo_proveedores_totales= (total_proveedores - total_salidas)
        archivoA.write("\n" )
        archivoA.write("Saldo de Proveedores del "+str(año2)+" : "+str(saldo_proveedores_totales)+"\n" )
        archivoA.write("\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n" )
        archivoA.close()
        #Final Tabla 6
        
        
        #TABLA 7
        print("")
        print(separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"7-Presupuesto de Mano de Obra Directa" +"-"*15 +"\n" )
        print("-"*15+"7-Presupuesto de Mano de Obra Directa" +"-"*15)
        archivoA.write("\n" )
        print("")
        listaHorasReq=[]

        for valor in (listanombreproduc):
            print("")
            print("PRIMER SEMESTRE: ")
            archivoA.write("PRIMER SEMESTRE  :"+"\n" )
            print(valor+":")
            print("")
            archivoA.write(str(valor)+" : "+"\n" )
            archivoA.write("\n" )
            u_producir=(lista_unidad_producir[contador27])
            archivoA.write("Unidades a producir : "+str(u_producir)+"\n" )
            h_requeridas= float(input("Cuantas horas se ocuparon por unidad : "))
            listaHorasReq.append(h_requeridas)
            archivoA.write("Horas requeridas por Unidad : "+str(h_requeridas)+"\n" )
    
            cuota_hora= float(input("Cuota por hora: "))
            print(separador)
    
            total_horas= (u_producir*h_requeridas)
            archivoA.write("Total de horas requeridas por unidad : "+str(total_horas)+"\n" )
            archivoA.write("Cuota por hora : "+str(cuota_hora)+"\n" )
        
            lista_total_horas_1.append(total_horas)
    
            importe_MOD= (total_horas*cuota_hora)
            archivoA.write("IMPORTE DE MOD : "+str(importe_MOD)+"\n" )
            archivoA.write("\n" )
    
            lista_importeMOD_1.append(importe_MOD)
    
            T_horas_semestre_1= sum(lista_total_horas_1)
    
            Total_MOD1= sum(lista_importeMOD_1)
            contador27= contador27+2

        archivoA.write("TOTAL DE HORAS REQUERIDAS DEL PRIMER SEMESTRE : "+str(T_horas_semestre_1)+"\n" )
        archivoA.write("TOTAL MOD DEL PRIMER SEMESTRE : "+str(Total_MOD1)+"\n" )
        archivoA.write("------------------------------------------------"+"\n" )
        archivoA.write("\n" )

        contador28=1
        contador29=0
        for valor in (listanombreproduc):
            print("")
            print("SEGUNDO SEMESTRE: ")
            archivoA.write("SEGUNDO SEMESTRE  :"+"\n" )
            print(valor+":")
            print("")
            archivoA.write(str(valor)+" :"+"\n" )
            archivoA.write("\n" )

            u_producir2=(lista_unidad_producir[contador28])
            archivoA.write("Unidades a producir : "+str(u_producir2)+"\n" )

            h_requeridas2=(listaHorasReq[contador29])
            archivoA.write("Horas requeridas por Unidad : "+str(h_requeridas2)+"\n" )
    
            cuota_hora2= float(input("Cuota por hora: "))
            print(separador)
    
            total_horas2=(u_producir2*h_requeridas2)
            archivoA.write("Total de horas requeridas por unidad : "+str(total_horas2)+"\n" )
            archivoA.write("Cuota por hora : "+str(cuota_hora2)+"\n" )
        
            lista_total_horas_2.append(total_horas2)
    
            importe_MOD2= (total_horas2*cuota_hora2)
            archivoA.write("IMPORTE DE MOD : "+str(importe_MOD2)+"\n" )
            archivoA.write("\n" )
    
            lista_importeMOD_2.append(importe_MOD2)
    
            T_horas_semestre_2= sum(lista_total_horas_2)
    
            Total_MOD2= sum(lista_importeMOD_2)
    
            contador28= contador28+2
            contador29=contador29+1
        
        archivoA.write("TOTAL DE HORAS REQUERIDAS DEL SEGUNDO SEMESTRE : "+str(T_horas_semestre_2)+"\n" )
        archivoA.write("TOTAL MOD DEL SEGUNDO SEMESTRE : "+str(Total_MOD2)+"\n" )
        archivoA.write("\n" )

        T_H_Requeridas= T_horas_semestre_1 + T_horas_semestre_2
        T_MOD_porSemestre= Total_MOD1+Total_MOD2

        archivoA.write("------------------------------------------------"+"\n" )
        archivoA.write("TOTAL DE HORAS REQUERIDAS DEL "+str(año2)+" : "+str(T_H_Requeridas)+"\n" )
        archivoA.write("TOTAL DE MOD DEL "+str(año2)+" : "+str(T_MOD_porSemestre)+"\n" )
        archivoA.write("\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n" )
        archivoA.close()
        

        #tabla 8 
        print("")
        print(separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"8-Presupuesto de Gastos Indirectos de Fabricacion" +"-"*15 +"\n" )
        print("-"*15+"8-Presupuesto de Gastos Indirectos de Fabricacion" +"-"*15)
        print("")
        archivoA.write("\n" )
        archivoA.write("PRIMER SEMESTRE:"+"\n")
        archivoA.write("\n" )
        print("")
        depreciacion=int(input("Dime tu Depreciacion Total : "))
        divdep=(depreciacion/2)
        lista8_1.append(divdep)
        lista8_2.append(divdep)
        archivoA.write("Depreciacion : "+str(divdep) +"\n" )


        seguro=int(input("Dime tu Seguro Total : "))
        divseg=(seguro/2)
        lista8_1.append(divseg)
        lista8_2.append(divseg)

        archivoA.write("Seguro : "+str(divseg) +"\n" )
        print(separador)
        verdad=input("Tu mantenimiento se divide en partes iguales semestrales: ")

        if verdad=="si" or verdad=="SI" or verdad=="Si" or verdad=="sI":
            print("")
            mantenimiento=int(input("Dime tu Manteniminieto Total : "))
            divmant=(mantenimiento/2)
            lista8_1.append(divmant)
            lista8_2.append(divmant)
            archivoA.write("Mantenimiento: "+str(divmant) +"\n" )
        
        else:
            print("")
            mantenimiento1=int(input("Dime tu Mantenimiento Del Primer Semestre : "))
            lista8_1.append(mantenimiento1)
            archivoA.write("Mantenimiento: "+str(mantenimiento1) +"\n" )

            mantenimiento2=int(input("Dime tu Mantenimiento Del Segundo Semestre : "))
            lista8_2.append(mantenimiento2)
            print(separador)
        print("")

        verdad=input("Tu Energetico se divide en partes iguales semestrales: ")
        if verdad=="si" or verdad=="SI" or verdad=="Si" or verdad=="sI":
            print("")
            energetico=int(input("Dime tu Energetico Total : "))
            divener=(energetico/2)
            lista8_1.append(divener)
            lista8_2.append(divener)
            archivoA.write("Energetico: "+str(divener) +"\n" )
        
        else:
            print("")
            energetico1=int(input("Dime tu Energetico Del Primer Semestre : "))
            lista8_1.append(energetico1)
            archivoA.write("Energetico : "+str(energetico1) +"\n" )

            energetico2=int(input("Dime tu Energetico Del Segundo Semestre : "))
            lista8_2.append(energetico2)
            print(separador)

        varios=int(input("Dime tu Varios Total : "))
        divva=(varios/2)
        lista8_1.append(divva)
        lista8_2.append(divva)
        archivoA.write("Varios : "+str(divva) +"\n" )

        totalGIF=(sum(lista8_1))
        archivoA.write("TOTAL GIF DEL SEMESTRE 1 : "+str(totalGIF) +"\n" )

        archivoA.write("\n" )
        archivoA.write("SEGUNDO SEMESTRE:"+"\n")
        archivoA.write("\n" )
        
        listanom8=["Depreciacion: ","Seguro: ","Mantenimiento: ","Energetico: ","Varios: "]

        for elemento in listanom8:
            archivoA.write(str(elemento)+" : "+str(lista8_2[contador26])+"\n")
            contador26=contador26+1


        totalGIF2=(sum(lista8_2))
        archivoA.write("TOTAL GIF DEL SEMESTRE 2 : "+str(totalGIF2) +"\n" )

        archivoA.write("\n" )
        TOTALGIF=(totalGIF+totalGIF2)
        archivoA.write("\n" )

        archivoA.write("Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion"+"\n" )
        archivoA.write("\n" )
        archivoA.write("TOTAL GIF "+str(año2)+" $: "+str(TOTALGIF) +"\n" )
        archivoA.write("Total horas M.O.D. Anual:"+str(T_H_Requeridas)+"\n" )
        x=(TOTALGIF/T_H_Requeridas)
        z=round(x,2)
        costoH_GIF=(z)
        archivoA.write("(=) Costo por Hora de G.I.F. "+"$ : "+str(costoH_GIF)+"\n" )

        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")




        #TABLA 9 
        contador26=0
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"9-Presupuesto de Gastos de Operacion" +"-"*15 +"\n" )
        print("-"*15+"9-Gastos de Administracion y Ventas:" +"-"*15)
        print("")
        archivoA.write("\n" )
        archivoA.write("PRIMER SEMESTRE:"+"\n")
        archivoA.write("\n" )
        print("")
        depreciacion2=int(input("Dime tu Depreciacion Total : "))
        divdep=(depreciacion2/2)
        lista9_1.append(divdep)
        lista9_2.append(divdep)
        archivoA.write("Depreciacion : "+str(divdep) +"\n" )

        sueldo_salarios=int(input("Dime tu Sueldo y salarios Total : "))
        divsue=(sueldo_salarios/2)
        lista9_1.append(divsue)
        lista9_2.append(divsue)

        archivoA.write("Saldos y Salarios : "+str(divsue) +"\n" )
        
        comision=float(input("Dime la Comision de Ventas Proyectadas (0.001) : "))

        resultadoco1=(totalventasS1*comision)
        resultadoco2=(totalventasS2*comision)
        lista9_1.append(resultadoco1)
        lista9_2.append(resultadoco2)

        archivoA.write("Comisiones : "+str(resultadoco1) +"\n" )
        print("")
        verdad=input("Tus varios se divide en partes iguales semestrales: ")
        if verdad=="si" or verdad=="SI" or verdad=="Si" or verdad=="sI":
            print("")
            vario=int(input("Dime tu Varios Total : "))
            divva1=(divva1/2)
            lista9_1.append(divva1)
            lista9_2.append(divva1)
            archivoA.write("Varios: "+str(divva1) +"\n" )
        
        else:
            print("")
            vario1=int(input("Dime tu Vario Del Primer Semestre : "))
            lista9_1.append(vario1)
            archivoA.write("Varios: "+str(vario1) +"\n" )

            vario2=int(input("Dime tu Vario Del Segundo Semestre : "))
            lista9_2.append(vario2)
            print(separador)
        print("")


        intereses=float(input("Dime los intereses por prestamo Total : "))
        divi=(intereses/2)
        lista9_1.append(divi)
        lista9_2.append(divi)
        archivoA.write("Intereses por obligaciones: "+str(divi) +"\n" )
        archivoA.write("\n" )
        print("")

        totalGIF3=(sum(lista9_1))
        totalGIF4=(sum(lista9_2))
        archivoA.write("TOTAL GIF DEL SEMESTRE 1 : "+str(totalGIF3) +"\n" )

        archivoA.write("\n" )
        archivoA.write("SEGUNDO SEMESTRE:"+"\n")
        archivoA.write("\n" )

        listanom9=["Depreciacion: ","Sueldos y Salarios: ","Comisiones: ","Varios: ","Intereses por prestamo: "]

        for elemento in listanom9:
            archivoA.write(str(elemento)+" : "+str(lista9_2[contador26])+"\n")
            contador26=contador26+1

        archivoA.write("\n" )
        archivoA.write("TOTAL GIF DEL SEMESTRE 2 : "+str(totalGIF4) +"\n" )
        archivoA.write("\n" )
        TOTALGIFF=(totalGIF3+totalGIF4)

        archivoA.write("Total de Gastos de Operacion: "+str(TOTALGIFF)+"\n" )

        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")

    
        #tabla 10
        lista_costo_unitario=[]
        contador=0
        contador1=0
        contador2=0
        contador3=3
        
        
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"10-Determinación del Costo Unitario de Productos Terminados" +"-"*15 +"\n" )
        print("-"*15+"10-Determinación del Costo Unitario de Productos Terminados" +"-"*15)
        print("")

        lista_costo_unitario=[]
        lista_nueva=[]
        listaCUT=[]
        
        contador=0
        contador1=0
        contador2=0
        contador3=3
        contador4=0

 
        for valor in (listanombreproduc):
            archivoA.write("\n")
            contador1=0
            print(listanombreproduc[contador])
            archivoA.write(valor+": "+"\n")
            
            lista_nueva=[]
            
            mano_obra=float(input("Cuanto es de mano de obra: "))
            resultado1= mano_obra*listaHorasReq[contador4]
            
            v_GIF= float(input("Cuanto es de GIF: "))
            resultado2= v_GIF*listaHorasReq[contador4]
            print("")
            
            contador4+=1
            
            x,y,z=(lista_req[contador2:contador3])
            lista_nueva.append(x)
            lista_nueva.append(y)
            lista_nueva.append(z)
            for cantidad in (lista_nueva):
                lista_costo_unitario.append(listapreciocompra[contador1]*cantidad)
                contador1+=1
                
            lista_costo_unitario.append(resultado1)
            lista_costo_unitario.append(resultado2)
            
            COSTOUF=(sum(lista_costo_unitario))
            listaCUT.append(COSTOUF)
            archivoA.write("COSTO UNITARIO FINAL : "+str(COSTOUF)+"\n")

            lista_costo_unitario=[]
            contador2= contador2+3
            contador3=contador3+3
            contador=contador+1

        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")

        #TABLA 11
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"11-Valuacion de Inventarios Finales" +"-"*15 +"\n" )
        print("-"*15+"11-Valuacion de Inventarios Finales" +"-"*15)
        print("")
        archivoA.write("\n")

        lista_total_material=[]
        lista_costo_total=[]
        lista_unidades=[]
        lista_c_unitario=[]
        lista_inventario=[]
        contador5=0
        contador6=0
        for material in lista_nombre_material:
            print(lista_nombre_material[contador5])
            print("")
            total_material= float(input(f"Dime el total de material {lista_nombre_material[contador5]} : "))
            lista_total_material.append(total_material)
            lista_costo_total.append( lista_total_material[contador5]*listapreciocompra[contador5])
            contador5+=1
        total_CU=sum(lista_costo_total)
    
        archivoA.write("Inventario Final de Materiales : "+str(total_CU)+"\n")
        archivoA.write("\n")
        print(separador)

 

        for nombres in (listanombreproduc):
            print(listanombreproduc[contador6])
            print("")      
            unidades_producto= float(input(f"Total de unidades de {listanombreproduc[contador6]} : "))
            lista_unidades.append(unidades_producto)
            
            c_unitario_total= float(input(f"Dime el costo unatio total de {listanombreproduc[contador6]} :"))
            lista_c_unitario.append(c_unitario_total)
            print("")
            v_inventario=(lista_unidades[contador6]*lista_c_unitario[contador6])
            lista_inventario.append(v_inventario)            
            contador6+=1
        inv_final_terminado=sum(lista_inventario)
        print(separador)
        

        archivoA.write("Inventario Final de Producto Terminado : "+str(inv_final_terminado)+"\n")
        archivoA.write("\n")
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")


        # TABLA ESTADO DE COSTO DE PRODUCCION Y VENTAS 
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"Estado de Costo de Produccion y Ventas" +"-"*15 +"\n" )
        print("-"*15+"Estado de Costo de Produccion y Ventas" +"-"*15)
        print("")
        archivoA.write("\n")

        saldoI=float(input("Dime el Saldo Inicial de Materiales : "))
        archivoA.write("Saldo Incial de Materiales : "+str(saldoI)+"\n")

        compras_materiales=(sum(compras_totales))
        archivoA.write("Compra de Materiales : "+str(compras_materiales)+"\n")

        Material_d=(saldoI+compras_materiales)
        archivoA.write("MATERIAL DISPONIBLE : "+str(Material_d)+"\n")

        inventarioF=(total_CU)
        archivoA.write("Inventario Final de Materiales : "+str(inventarioF)+"\n")

        materialU=(Material_d-inventarioF)
        archivoA.write("MATERIALES UTILIZADOS : "+str(materialU)+"\n")

        manodo=(T_MOD_porSemestre)
        archivoA.write("Mano de Obra Directa : "+str(manodo)+"\n")



        gfi=(TOTALGIF)
        archivoA.write("Gasto de Fabricacion Indirectos : "+str(gfi)+"\n")

        COSTOPRO=(materialU+manodo+gfi)
        archivoA.write("COSTO DE PRODUCCION : "+str(COSTOPRO)+"\n")

        inventarioI_terminados=float(input("Dime tu Inventario Inicial de Productos Terminados : "))
        archivoA.write("Inventario Inicial de Productos Terminados : "+str(inventarioI_terminados)+"\n")

        TOTAL_PRO_DIS=(COSTOPRO+inventarioI_terminados)
        archivoA.write("TOTAL DE PRODUCCION DISPONIBLE : "+str(TOTAL_PRO_DIS)+"\n")

        inventarioF_terminados=(inv_final_terminado)
        archivoA.write("Inventario Final de Productos Terminados  : "+str(inventarioF_terminados)+"\n")


        COSTOVENTAS=(TOTAL_PRO_DIS-inventarioF_terminados)
        archivoA.write("COSTO DE VENTAS  : "+str(COSTOVENTAS)+"\n")

        archivoA.write("\n")
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")




        #ESTADO DE RESULTADOS 
        print("")
        print(separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"ESTADO DE RESULTADOS" +"-"*15 +"\n" )
        print("-"*15+"ESTADO DE RESULTADOS " +"-"*15)
        print("")
        archivoA.write("\n" )
        archivoA.write("VENTAS : "+str(VENTASTOTALES)+"\n" )

        archivoA.write("COSTO DE VENTAS : "+str(COSTOVENTAS)+"\n" )
        UB=(VENTASTOTALES-COSTOVENTAS)
        archivoA.write("UTILIDAD BRUTA : "+str(UB)+"\n" )

        archivoA.write("GASTO DE OPERACION : "+str(TOTALGIFF)+"\n" )
        
        UO=(UB-TOTALGIFF)
        archivoA.write("UTILIDAD DE OPERACION : "+str(UO)+"\n" )

        porcentaje=(float(input("Dime el Porcentaje de ISR : ")))
        ISR=(UO*porcentaje)
        z=round(ISR,2)

        archivoA.write("ISR : "+str(z)+"\n" )

        porcentaje2=float(input("Dime el Porcentaje de PTU : "))
        PTU=(UO*porcentaje2)
        x=round(PTU,2)
        
        archivoA.write("PTU : "+str(x)+"\n" )

        UN=(UO-ISR-PTU)
        a=round(UN,2)

        archivoA.write("UTILIDAD NETA  : "+str(a)+"\n" )
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")



        #ESTADO DE FLUJO EN EFECTIVO
        print("")
        print(separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"ESTADO DE FLUJO EN EFECTIVO" +"-"*15 +"\n" )
        print("-"*15+"ESTADO DE FLUJO EN EFECTIVO" +"-"*15)
        print("")
        archivoA.write("\n")

        saldo_inicial=float(input("Dime el saldo inicial en Efectivo : "))
        archivoA.write("Saldo Inicial de Efectivo : "+str(saldo_inicial)+"\n" )
        archivoA.write("\n")

        archivoA.write("ENTRADAS :"+"\n" )
        archivoA.write("COBRANZA "+str(año)+" : "+str(cobranza)+"\n" )
        archivoA.write("COBRANZA "+str(año2)+" : "+str(saldoCliente)+"\n" )
        archivoA.write("\n")
        TE=(cobranza+saldoCliente)
        archivoA.write("Total de entradas :"+str(TE)+"\n" )

        ED=(saldo_inicial+TE)
        archivoA.write("Efectivo Disponible :"+str(ED)+"\n" )
        archivoA.write("\n")
        archivoA.write("SALIDAS :"+"\n" )
        archivoA.write("\n")

        archivoA.write("Provedores del "+str(año)+" : "+str(saldo_proveedores)+"\n" )
        archivoA.write("Provedores del "+str(año2)+" : "+str(por_proveedores)+"\n" )
        archivoA.write("Pago de mano de obra directa : "+str(T_MOD_porSemestre)+"\n" )

        PGIF=(TOTALGIF-depreciacion)
        PGO=(TOTALGIFF-depreciacion2)

        archivoA.write("Pago Gastos Indirectos de Fabricacion : "+str(PGIF)+"\n" )
        

        archivoA.write("Pago de Gastos de Operacion : "+str(PGO)+"\n" )

        CAFM=float(input("Dime tu Compra de Activo Fijo (Maquinaria) : "))
        archivoA.write("Compra de Activo Fijo (Maquinaria): "+str(CAFM)+"\n" )

        PISR=float(input(f"Dime el pago ISR {año} : "))
        archivoA.write("Pago ISR "+str(año)+" : "+str(PISR)+"\n" )
        archivoA.write("\n")

        TS=(saldo_proveedores+por_proveedores+T_MOD_porSemestre+PGO+CAFM+PISR+PGIF)

        archivoA.write("TOTAL SALIDAS : "+str(TS)+"\n" )
        FEA=(ED-TS)
        archivoA.write("FLUJO DE EFECTIVO ACTUAL  : "+str(FEA)+"\n" )
        archivoA.write("\n")
        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")



        # BALANCE GENERAL 
        print("")
        print(separador)
        archivoA=open("./respuestas.txt" , 'a')
        archivoA.write("-"*15+"BALANCE GENERAL" +"-"*15 +"\n" )
        print("-"*15+"BALANCE GENERAL" +"-"*15)
        print("")
        archivoA.write("\n")
        archivoA.write("ACTIVO "+"\n")
        archivoA.write("CIRCULANTE : "+"\n")
        archivoA.write("\n")
        archivoA.write("Efectivo : $ "+str(FEA)+"\n")
        archivoA.write("Clientes : " +str(SALDODECLIENTES)+"\n") #SALDODECLIENTES

        FYE=float(input("Dime los funcionarios y empleados : " ))
        archivoA.write("Funcionarios y Empleados : " +str(FYE)+"\n")

        DD=float(input("Dime los Deudores Diversos : "))
        archivoA.write("Deudores Diversos : " +str(DD)+"\n")
        archivoA.write("Inventario de Materiales : " +str(total_CU)+"\n")
        archivoA.write("Inventario de Producto terminado: " +str(inv_final_terminado)+"\n")


        TAC=(FEA+SALDODECLIENTES+FYE+DD+total_CU+inv_final_terminado)
       
        archivoA.write("TOTAL DE ACTIVO CIRCULANTE : " +str(TAC)+"\n")
        archivoA.write("\n")
        archivoA.write("NO CIRCULANTE : "+"\n")
        archivoA.write("\n")

        terreno=float(input("Dime el Terreno : "))
        archivoA.write("Terreno : " +str(terreno)+"\n")

        plantaye=float(input("Dime la Planta y Equipo : "))
        PYE=(plantaye+CAFM)
        archivoA.write("Planta y Equipo : " +str(PYE)+"\n")

        depreciaciona=float(input("Dime la Depreciacion Acumulada : "))
        DA=(-(depreciaciona+depreciacion+depreciacion2))

        archivoA.write("Depreciacion Acumulada : " +str(DA)+"\n")

        TANC=(terreno+PYE+DA)
        archivoA.write("\n")
        archivoA.write("TOTAL ACTIVO NO CIRCULANTE : " +str(TANC)+"\n")
        archivoA.write("\n")
        AT=(TAC+TANC)
        archivoA.write("ACTIVO TOTAL : " +str(AT)+"\n")
        archivoA.write("\n")

        archivoA.write("PASIVO "+"\n")
        archivoA.write("CORTO PLAZO : "+"\n")
        archivoA.write("\n")
        archivoA.write("Proveedores : " +str(saldo_proveedores_totales)+"\n")
        documentospa=float(input("Dime los Documentos por Pagar : "))
        archivoA.write("Documentos por Pagar : " +str(documentospa)+"\n")

        archivoA.write("ISR por Pagar : " +str(z)+"\n")
        archivoA.write("PTU por Pagar : " +str(x)+"\n")

        archivoA.write("\n")
        TPCP=(saldo_proveedores_totales+documentospa+z+x)
        archivoA.write("TOTAL DE PASIVO CORTO PLAZO : "+str(TPCP)+"\n")
        archivoA.write("\n")

        archivoA.write("LARGO PLAZO : "+"\n")

        obligacionporpagar=float(input("Dime tus Obligaciones por pagar : "))
        archivoA.write("Obligaciones por pagar : "+str(obligacionporpagar)+"\n")
        archivoA.write("\n")

        TPLP=(obligacionporpagar)

        archivoA.write("TOTAL PASIVO LARGO PLAZO : "+str(obligacionporpagar)+"\n")
        archivoA.write("\n")

        PT=(TPCP+TPLP)
        archivoA.write("PASIVO TOTAL : "+str(PT)+"\n")

        archivoA.write("\n")

        archivoA.write("CAPITAL CONTABLE : "+"\n")

        capaportado=float(input("Dime tu Capital Aportado : "))
        archivoA.write("Capital Aportado : "+str(capaportado)+"\n")

        capganado=float(input("Dime tu Capital Ganado : "))
        archivoA.write("Capital Ganado : "+str(capganado)+"\n")


        archivoA.write("Utlidad del Ejercicio : "+str(a)+"\n")


        archivoA.write("\n")

        TCC=(capaportado+capganado+a)
        archivoA.write("TOTAL DE CAPITAL CONTABLE  : "+str(TCC)+"\n")
        archivoA.write("\n")

        SUMAPYC=(PT+TCC)
        archivoA.write("SUMA DE PASIVO Y CAPITAL   : "+str(SUMAPYC)+"\n")
        archivoA.write("\n")
        resultadofinal=(AT-SUMAPYC)
        archivoA.write("\n")
        archivoA.write("RESULTADO FINAL : "+str(resultadofinal)+"\n")

        archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
        archivoA.write("\n")
        archivoA.close()
        print("")
        print(separador)
        print("")

        break



















        





    

        






except:
    print("Intenta respetar lo que se te pide :)")









