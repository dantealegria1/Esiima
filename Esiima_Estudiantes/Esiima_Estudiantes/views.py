
import requests
from typing import Optional

def consultar_calificaciones_api() -> Optional[dict]:
    """
    Consulta una API externa para obtener las calificaciones de los estudiantes.
    """
    url = 'https://api.universidad.com/calificaciones'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
