apetece_helado = input("¿Te apetece un helado? (Si / No): ")
tiene_dinero = input("¿Tienes dinero para un helado? (Si / No): ")
esta_el_senor_helados = input("¿Esta el señor de los helados? (Si / No): ")
esta_tu_tia = input("¿Estás con tu tia? (Si / No): ")

if apetece_helado == "Si" and (tiene_dinero == "Si" or esta_tu_tia == "Si") and esta_el_senor_helados == "Si":
    print("Entonces disfruta un helado")
else:
    print("Pues tú te lo pierdes")
