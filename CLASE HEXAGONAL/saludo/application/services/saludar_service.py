from saludo.application.ports.saludar_use_case import SaludarUseCase
from saludo.domain.persona import Persona

class SaludarService(SaludarUseCase):
    def saludar(self, nombre: str) -> str:
        persona = Persona(nombre)
        return f"Hola {persona.nombre}"