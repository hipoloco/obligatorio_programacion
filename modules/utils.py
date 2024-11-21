import os
from modules.constants import COLORS

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cprint(text, color):
    if not isinstance(text, str):
        raise ValueError("El texto a imprimir debe ser un string.")

    if not isinstance(color, str):
        raise ValueError("El color debe ser un string en mayúsculas.")
    
    # Usar el color por defecto si no se encuentra el color solicitado
    color = COLORS.get(color, COLORS.get("RST"))
    print(f"{color}{text}{COLORS['RST']}")

def secs_to_time(seconds):
    """
    Convierte una duration de tiempo en segundos a una representación en cadena según los siguientes criterios:
    
    - "Instantáneo" cuando el tiempo sea menor de 1 segundo
    - "# segundo(s)" cuando el tiempo sea menor a 1 minuto
    - "# minuto(s)" cuando el tiempo sea menor a 1 hora
    - "# hora(s)" cuando el tiempo sea menor a 1 día
    - "# semana(s)" cuando el tiempo sea menor a 1 mes
    - "# mes(es)" cuando el tiempo sea menor a 1 año
    - "# año(s)" cuando el tiempo supere el año
    
    Args:
        seconds (float o int): duration de tiempo en segundos.
    
    Returns:
        str: Representación en cadena del tiempo.
    """
    # Definición de las conversiones en segundos
    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    WEEK = 7 * DAY
    MONTH = 30 * DAY  # Aproximación de 1 mes = 30 días
    YEAR = 365 * DAY  # Aproximación de 1 año = 365 días

    if seconds < SECOND:
        return "Instantáneo"
    elif seconds < MINUTE:
        duration = int(seconds)
        unit = "segundo" if duration == 1 else "segundos"
        return f"{duration} {unit}"
    elif seconds < HOUR:
        duration = int(seconds // MINUTE)
        unit = "minuto" if duration == 1 else "minutos"
        return f"{duration} {unit}"
    elif seconds < DAY:
        duration = int(seconds // HOUR)
        unit = "hora" if duration == 1 else "horas"
        return f"{duration} {unit}"
    elif seconds < MONTH:
        duration = int(seconds // WEEK)
        unit = "semana" if duration == 1 else "semanas"
        return f"{duration} {unit}"
    elif seconds < YEAR:
        duration = int(seconds // MONTH)
        unit = "mes" if duration == 1 else "meses"
        return f"{duration} {unit}"
    else:
        duration = int(seconds // YEAR)
        unit = "año" if duration == 1 else "años"
        return f"{duration} {unit}"
