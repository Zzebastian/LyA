
#Tipos de accesorios
accesorios = {
    "Collar": "Co",
    "Conjunto": "CJ",
    "Pulsera": "Pu"
}

#Tipos de cuentas
cuentas = {
    "4MM": "4m",
    "6MM": "6m",
    "Donita": "Do",
    "Escalla": "Es",
    "Semilla": "Se",
    "Facetada": "Fa"
}

#Tipos de terminaciones
terminaciones = {
    "Elastizada": "El",
    "Con Cierre": "CC"
}
elementos = {}
for accesorio in accesorios:
    for cuenta in cuentas:
        for terminacion in terminaciones:
            # print(accesorio,cuenta,terminacion)
            elemento = f"{accesorio} {cuenta} {terminacion}"
            codigo = f'{accesorios[accesorio]}{cuentas[cuenta]}{terminaciones[terminacion]}'
            elementos[elemento]=codigo

i=30
for elemento in elementos:
    i+=1
    # print(i,"    ",elementos[elemento],"    ",elemento)
    print(f"CR.{i}","    ",elemento)
    
print("########################")