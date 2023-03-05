import matplotlib.pyplot as plt

def charts():
    

    # Datos
    labels = ['Etiqueta 1', 'Etiqueta 2', 'Etiqueta 3', 'Etiqueta 4']
    sizes = [20, 30, 25, 25]

    # Crear gráfico de pastel
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    # Mostrar gráfico
    plt.savefig("image.png")
    plt.close()

