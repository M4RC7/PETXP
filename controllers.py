from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .factory import ModelBulder
from .util import *
from .services import *
import traceback
import json

# Create your views here.
""" Modelo Controller - Trata as requisicoes """
class  AbsController:
    def __init__(self, service):
        self.service = service

    def list_model(self, request):
        try:
    
            return JsonResponse({
                'error': False,
                'msg': 'Lista de Animais recuperadas com suceso',
                'list' : self.service.get_all()

            }, status=200)

        except Exception as e:
            traceback.print_exc()
            return JsonResponse({
                'error': True,
                'msg': 'Houve um erro inesperado ao tentar recuperar ao recuperar a listagem \nErro: ' + str(e)
            }, status=500)
    
    @csrf_exempt
    def register_model(self, request):
        body_decode = request.body.decode('utf-8')
        body_data = json.loads(body_decode))

        self.service.save_or_update()

class AdodanteController(AbsController):
    def __init__(self, service, ong_service):
        super().__init__()

    def list_model(self, request):
        super().list_model() 
    
    @csrf_exempt
    def register_model(self, request):
        super().register_model()



class OngController(AbsController):
    def __init__(self, service, animal_serivce):
        super().__init__()
            
    def list_model(self, request):
       super().list_model(request)


class AnimalController(AbsController):
    def __init__(self, service, ong_service):
        super().__init__()
        self.ong_service = ong_service

    def list_model(self, request):
       super().list_model(request)
    
    @csrf_exempt
    def register_model(self, request):
        cod = 3
        data = []
        try:
            ong = self.ong_service.get_by_id(codOng)
            
            new_animal_info = self.service.save_or_update(data, ong)

            return JsonResponse({
                    "error": False,
                    "msg": "Animal registrado com sucesso",
                    "animal" : new_animal_info
                }, status=200)
        except Exception as e:
               return JsonResponse({
                'error': True,
                'msg': 'Houve um erro inesperado ao registrar o animal \nErro: ' + str(e)
                }, status=500)

 class PedidoController(AbsController):
    def __init__(self, service, ong_service):
        super().__init__()
        self.animal_service = ong_service
        self.adotante_service = adodante_service

    def register_model(self, request):
        codA = 3
        codB = 5 
        data = []
        try:
            animal = self.animal_service()
            adodante = self.adodante_service()

            pedido_info =  self.service.save_or_update(animal, adodante)
            
            return JsonResponse({
                    "error": False,
                    "msg": "Pedido registrado com sucesso",
                    "pedido" : pedido_info
                }, status=200)

         except Exception as e:
               return JsonResponse({
                'error': True,
                'msg': 'Houve um erro inesperado ao registrar o pedido de adocao \nErro: ' + str(e)
                }, status=500)









