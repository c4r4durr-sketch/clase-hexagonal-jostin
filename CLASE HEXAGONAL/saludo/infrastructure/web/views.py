import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from saludo.application.services.saludar_service import SaludarService

@csrf_exempt
def saludar_view(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        nombre = datos.get('nombre', '')
        
        servicio = SaludarService()
        mensaje = servicio.saludar(nombre)
        
        return JsonResponse({'mensaje': mensaje}, status=200)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)