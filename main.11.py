print(" ")
print("Arzaba Diaz April 3W 1173")
def distancia_dirigida(punto1, punto2):
    """
    Esta funcion calcula la distancia dirigida entre dos puntos en un plano 2D.
    
    Args:
    punto1 (tuple): Coordenadas del primer punto (x1, y1).
    punto2 (tuple): Coordenadas del segundo punto (x2, y2).
    
    Returns:
    float: La distancia dirigida desde el primer punto al segundo.
    """
    x1, y1 = punto1
    x2, y2 = punto2
    return (x2 - x1, y2 - y1)



  