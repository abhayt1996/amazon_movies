# decorator for verifying the JWT
from functools import wraps
import jwt
from django.http import HttpResponse, JsonResponse

secret_key = "abhay"

def get_secret_key():
    return secret_key
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'api-key' in args[0].headers:
            token = args[0].headers['api-key']
        # return 401 if token is not passed
        if not token:
            return JsonResponse({'message': 'Token is missing !!'},status=401)

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, get_secret_key())
            if data['username'] == "admin":
                return f(*args, **kwargs)
            return JsonResponse({
                'message': 'Token is invalid !!'
            }, status=401)
        except:
            return JsonResponse({
                'message': 'Token is invalid !!'
            },status=401)
        # returns the current logged in users contex to the routes


    return decorated