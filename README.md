# tarea2unidad_2.11
Arzaba Diaz April 1173 3W
print(" ")
print("Arzaba Diaz April 3W 1173")
def distancia_dirigida(punto1, punto2):
    """
    esta funcion calcula la distancia dirigida entre dos puntos en un plano.
    
    args:
    punto1 (tuple): Coordenadas del primer punto (x1, y1)
    punto2 (tuple): Coordenadas del segundo punto (x2, y2)

    returns:
    tuple: la distancia dirigida en x y en y (dx, dy)
    """
    #esta linea desempaquetamos las coordenadas de los puntos
    x1, y1 = punto1
    x2, y2 = punto2
    # Calculamos la distancia dirigida en x y en y
    dx = x2 - x1
    dy = y2 - y1
    return (dx, dy)

#estab linea dara un ejemplo de uso
resultado = distancia_dirigida((1, 2), (4, 6))
print(resultado)  #salida: (3, 4)
![image](https://github.com/user-attachments/assets/ee6579ac-0f11-4e12-9274-44571b846023)
