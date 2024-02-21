import json

with open("wcountries.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def main():


    while True:
        
        print("\n1. Listar países")
        print("2. Listar países que empiezan por letra")
        print("3. Informacion general de pais")
        print("4. Conteo de informacion")
        print("q. Salir")

        opcion = input("Seleccione una opción (1-4) o 'q' para salir: ")

        if opcion == '1':
            listar_pais(data)
        elif opcion == '2':
            mostrar_paises_por_primera_letra(data)
        elif opcion == '3':
            mostrar_info_pais()
        elif opcion == '4':
            contar_info(data)
        elif opcion == 'q':
            print("¡Hasta luego!")
            break
        elif opcion == '5':
            name_paises = [country_data['name']['common'].upper() for country_data in data] + \
                      [name_info['common'].upper() for country_data in data for name_info in country_data['name']['native'].values()]
            name_paises.sort()
            print(name_paises)

    else:
        print("Opción no válida. Inténtelo de nuevo.")

def listar_pais(data):
    for country_data in data:
        common_name = country_data["name"]["common"]
        print(common_name)


def mostrar_paises_por_primera_letra(data):
    letra = input("Ingrese la primera letra para filtrar países: ")
    paises_con_letra = [common_name["name"]["common"] for common_name in data if common_name["name"]["common"].startswith(letra.upper())]
    print(f"Hay '{len(paises_con_letra)}' que empiezan por la letra '{letra.upper()}'.")
    if paises_con_letra:
        print(f"Paises cuyo nombre común comienza con '{letra.upper()}':")
        for nombre in paises_con_letra:
            print(nombre)
    else:
        print(f"No hay países cuyo nombre común comience con '{letra.upper()}'.")




def obtener_informacion_importante(pais):
    currencies = pais["currencies"]
    moneda = next(iter(currencies.values()))
    return {
        "Nombre común": pais["name"]["common"],
        "Nombre oficial": pais["name"]["official"],
        "Capital": ", ".join(pais["capital"]),
        "Región": pais["region"],
        "Subregión": pais["subregion"],
        "Idiomas": ", ".join(pais["languages"].values()),
        "ID Moneda": ", ".join(pais["currencies"].keys()),
        "Moneda": moneda.get("name", ""),
        "Símbolo de moneda": moneda.get("symbol", ""),
        "Coordenadas geográficas": pais["latlng"],
        "Bandera": pais["flag"]
    }

def nada(nombre_pais):
    for pais in data:
        if pais["name"]["common"].lower() == nombre_pais.lower():            
            return obtener_informacion_importante(pais)
    return None

def mostrar_info_pais():

    nombre_pais = input("Introduce el nombre del pais del que quieres los datos:")
    informacion_pais = nada(nombre_pais)

    if informacion_pais:
        print("\nInformación del país:")
        for clave, valor in informacion_pais.items():
            print(f"{clave}: {valor}")
    else:
        print(f"No se encontró información para el país {nombre_pais}.")

def contar_info(data):

    def listar_paises_misma_moneda(data, moneda):
        paises_misma_moneda = []
        for pais in data:
            currencies = pais["currencies"]
            if moneda.lower() in [c.lower() for c in currencies.keys()]:
                paises_misma_moneda.append(pais["name"]["common"])

        if paises_misma_moneda:
            return [(i+1, pais) for i, pais in enumerate(paises_misma_moneda)]
        else:
            return None
        
    def listar_paises_por_idioma(data, idioma):
        paises_por_idioma = []
        for pais in data:
            languages = pais["languages"]
            if idioma.lower() in [l.lower() for l in languages.values()]:
                paises_por_idioma.append(pais["name"]["common"])

        if paises_por_idioma:        
            return [(i+1, pais) for i, pais in enumerate(paises_por_idioma)]
        else:
            return None
        
    while True:
        print("\n1. Numero de países que utilizan la misma moneda")
        print("4. Numero de paises que hablan un mismo idioma")
        opcion = input("Ingrese la opción (1, 2, 3, 4) o 'q' para salir: ")

        if opcion == '1': 
            
            for pais in data:
                currencies = pais["currencies"]
                print(currencies)
            moneda = input("Introduce el ID de la moneda, p.ej. (EUR): ")
            paises_misma_moneda = listar_paises_misma_moneda(data, moneda)
            if paises_misma_moneda:
                print("Países que utilizan la misma moneda:", len(paises_misma_moneda))
                
                seg = input("¿Quieres saber que paises son?[Y/n]")
                if seg.lower == 'y' or seg.lower == 'ye' or seg.lower == 'yes':
                    for numero, pais in paises_misma_moneda:
                        print(f"   {numero}. {pais}")
                else:
                    main()
                    
            else:
                print(f"No se encontraron países que utilicen la moneda {moneda}.")

#        elif opcion == '2':
#        # Listar paises de una región
#            paises_region = listar_paises_por_region(data)
#            print("2. Países en la región 'Africa':")
#            for numero, pais in paises_region:
#                print(f"   {numero}. {pais}")

#        elif opcion == '3':
#        # Listar paises de una subregión
#            paises_subregion = listar_paises_por_subregion(data)
#            print("3. Países en la subregión 'Eastern Africa':")
#            for numero, pais in paises_subregion:
#                print(f"   {numero}. {pais}")

        elif opcion == '4': 
            idioma = input("De que idioma quieres listar los paises?:")
            paises_idioma = listar_paises_por_idioma(data, idioma)
            if paises_idioma:
                print("Países que utilizan el mismo idioma:", len(paises_idioma))
                seg = input("¿Quieres saber que paises son?[Y/n]")
                if seg.lower == 'y' or 'ye' or 'yes':
                    for numero, pais in paises_idioma:
                        print(f"   {numero}. {pais}")
                else:
                   main() 
                   
            else:
                print(f"No se encontraron países que utilicen el idioma {idioma}.")
        
        elif opcion.lower() == 'q':
            break
        else:
            print("Opción no válida. Intente de nuevo.")




if __name__ == "__main__":
    main()