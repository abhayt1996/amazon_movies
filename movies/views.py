import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from datetime import datetime, timedelta
import requests
from movies.authenticate import get_secret_key, token_required
import configparser
config = configparser.RawConfigParser()
config.read('./config.cfg')
api_config_dict = dict(config.items('api'))
@csrf_exempt
@token_required
def get_movies(request):
    try:
        page_number = request.GET.get('page')
        url = f"https://demo.credy.in/api/v1/maya/movies/?page={page_number}"

        headers = {
            'Username': api_config_dict['api_username'],
            'Password': api_config_dict['api_password']
        }

        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            movie_resposne = response.json()
            return JsonResponse({"message":movie_resposne},status=200)
        return JsonResponse({"message":""},status=404)
    except Exception as ee:
        print(str(ee))
        return JsonResponse({"message":""},status=401)

@csrf_exempt
def login(request):
    try:
        data = request.body
        data = json.loads(data)
        username = data.get("username")
        password = data.get("password")
        if username == "admin" and password == "password":
            token = jwt.encode({
                'username': username,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            },get_secret_key())
            return JsonResponse({"token":token.decode("utf-8")},status=200)
        return JsonResponse({"token":""},status=401)
    except Exception as ee:
        print(str(ee))
        return JsonResponse({"token":""},status=401)
