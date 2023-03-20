from django.http import JsonResponse, HttpResponse
from .factory import ModelBuilder
from .util import *
import json

# Create your views here.
""" Modelo Controller - Trata as requisicoes """

def list_animals(request):
    try:
        animals = ModelBuilder.get_all('animal')

        data = []
        for animal in animals:
            data.append(animal.to_dict())

        print(data)
        return JsonResponse({
            'error': False,
            'msg': 'Lista de Animais recuperadas com suceso',
            'data' : data
        })

    except Exception as e:
        return JsonResponse({
            'error': True,
            'msg': 'Houve um erro inesperado ao tentar recuperar a lista de animais \nErro: ' + str(e)
        })

def create_adoption_request(request):
    body_decode =    body_decode = request.body.decode('utf-8')
    body = json.loads(body_decode)

    try:
        user = UserService.auth_user(body["usuario"], body["senha"], "adodante")
        animal = AnimalService.get_animal(body["codAni"])
        if animal is not None: 
            adopt_request_details = AdoptionService.create_order(user, animal) 
        
            return JsonResponse({
                "error" : False,
                "msg" : "Pedido de acocao criado com sucesso",
                "info" : adopt_request_details 
            }, status=204)
        else:
            raise  Exception("Nao foi encontrado Animal referente ao pedido de adocao")
    
    except Exception as e:
        return JsonResponse({'error': True,
                             'msg': "Erro: " + str(e)}},
                             status=400)


def register_animal(request):
   body_decode = request.body.decode('utf-8')
   body = json.loads(body_decode)

   try:
        user = UserService.auth_user(body["usuario"], body["senha"], "ong")
        animal = AnimalSerivce.register_animal(user_info, body)

        return JsonResponse({
            'error': False,
            'msg': 'Animal com codigo adcionado com suceso',
            'info': animal_info
        })

   except Exception as e:
       return JsonResponse({
           'error': True,
           'msg': 'Houve um erro inesperado ao tentar adcionar o animal\nErro: ' + str(e)
       })




