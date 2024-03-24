

def find_one(list, needle):
    """
    Devuelve True si encuentra uno o má ocurrencias de needle en list
    """
    return find_n(list, needle, 1)

def find_n(list, needle, n):
    """
    Devuelve True si encuentra n o más ocurrencias de needle en list
    False en caso contrario
    """
    # Si n >= 0 
    if n >= 0:
        # Inicializamos el índice y el contador
        count = 0
        i = 0
        # mientras no hayamos encontrado al elemento n vceces o no hayamos terminado la lista...
        while (count < n) and (i < len(list)):
            # si lo encontramos, actualizamos el contador
            if  needle == list[i]:
                # incrementamos el contador
                count += 1
            # avanzamos al siguiente elemento
            i += 1    
        # devolvemos el resultado de comparar contador con n
        return count >= n
    else:
        return False

def find_streak(list, needle, n):
    """
    Devuelve True si en list hay n o más needles seguidos 
    False en caso contrario
    """
    # Inicializo el indice, el contador y el indicador de racha
    if n >= 0:
        index = 0
        count = 0
        in_streak = False
        # Mientras no haya encontrado n seguidos o la lista no se haya acabado...
        while (count < n) and (index < len(list)):
            # Si encontramos el elemento, aumentamos el contador y avanzamos al siguiente
            if needle == list[index]:
                in_streak = True
                count += 1
            # Si no lo encontramos, restablecemos el contador y avanzamos al siguiente
            else:
                in_streak = False
                count = 0
            index += 1            
        # Devolvemos el resultado de comparar el contador con n Siempre y Cuando estemos en racha
        return count >= n and in_streak
    else:
        return False
        
    
   
    