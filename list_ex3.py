# get the first letter of a list of names
lista_de_nombres=['Andrés Anderson Jiménez', 'José Edward Gallego', 'Dario González', 'María Ana Benítez Delgado', 'Luisa Montoya', 'Valeria Yolanda González Salazar', 'Lucía Patricia Aguirre Carvajal', 'María Méndez', 'Santiago Medina', 'María Jenny Rivera Medina', 'Elizabeth Barrios Acosta', 'Carmen Maritza Reyes', 'Ignacio Andrés Agudelo Castellanos', 'Alcides Antonio Arboleda Sanabria', 'David Villamizar', 'Yulieth Ocampo', 'Francisco Corredor', 'Elena Luz Cifuentes', 'Álvaro Cristian Zapata', 'Stiven Jefferson García Granados', 'Leonor Vera', 'Rocío Yaneth Bermúdez Ramos', 'José Héctor Serna', 'Yerson Luis Salamanca', 'José Enrique Galindo', 'Socorro Mercedes Pérez', 'Carlos Camargo Gómez', 'Marisol Carolina Jiménez', 'Luis Ayala', 'Julián Quintero Erazo', 'Aura Molina', 'Olga Liliana Ariza', 'Sofía Vargas Oviedo', 'Esther Sandra Chávez Díaz', 'Daniel Cortés', 'Janeth Andrea Figueroa Pérez', 'Javier Milton Puentes Medina', 'Jesús Santiago Bedoya', 'José Jorge Castro', 'Inés Sánchez']

primeras_letras=[]
for nombre in lista_de_nombres:
    primera_letra=nombre[0]
    primeras_letras.append(primera_letra)
print(primeras_letras)

