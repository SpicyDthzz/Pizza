import os
os.system ("cls")
print("FPY1101_014V_P2_Henríquez_Cristóbal")

nombre_cliente = input("Bienvenido a Don giovanni, Ingrese su nombre: ")
print ("gracias por elegirnos", nombre_cliente + ", Por favor realize su pedido aquí ↓ ")

print ("Tamaños disponibles : (Individual, Mediana, Familiar) ")
tamaño_pizza = input("Que tamaño desearia : ")

print ("Pizzas disponibles : (Pepperoni, Margarita, Cuatro quesos) ")
variedad_pizza =input ("Que pizza desearia llevar : ")

print ("bebidas disponibles: Limon soda, Pepsi, Kem piña, Bilz, Pap, Canada dry") 
bebida = input ("Elija su bebida : ")

palitos_pregunta = input ("Desea llevar palitos de ajo Si/No")

palitos = palitos_pregunta.lower == "si"
palitos = palitos_pregunta.lower == "no"


precio_base_pepperoni = 5000
precio_base_margarita = 5000
precio_base_cuatro_quesos = 6000

mediano_pepperoni_margarita = 1500
mediano_cuatro_quesos = 2000
familiar= mediano_pepperoni_margarita * 2

precio_bebidas = {      
"Limón Soda": 2000,
    "Pepsi": 2500,
    "Kem Piña": 2000,
    "Bilz": 2000,
    "Pap": 2000,
    "Canada Dry Ginger Ale": 2000
}

precio_palos_normal = 3000
precio_palos_promocion = 2000

if variedad_pizza == "Pepperoni" or variedad_pizza == "Margarita":
    precio_pizza = precio_base_pepperoni
    if tamaño_pizza == "Mediana":
        precio_pizza += mediano_pepperoni_margarita
    elif tamaño_pizza == "Familiar":
        precio_pizza += familiar
elif variedad_pizza == "Cuatro Quesos":
    precio_pizza = precio_base_cuatro_quesos
    if tamaño_pizza == "Mediana":
        precio_pizza += mediano_cuatro_quesos
    elif tamaño_pizza == "Familiar":
        precio_pizza += familiar

precio_bebida_total = bebida [bebida]


precio_palitos = precio_palos_promocion if variedad_pizza and palitos else precio_palos_normal


total_pedido = precio_pizza + precio_bebida_total + precio_palitos


print("El total de su compra es:", total_pedido)
    

#usar while tru, if, elif, else, int, input y excep  
#no usar lower , def , listas y no usar {}




