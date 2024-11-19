from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed

# Usuário simulado
USUARIO_LOCAL = {
    'username': 'usuario_teste',
    'password': 'senha123',
}


def create_jwt_token(username):
    
    class FakeUser:
        def __init__(self, username, user_id):
            self.username = username
            self.id = user_id  

    user = FakeUser(username, user_id=1)
    
    
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token), str(refresh)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username == USUARIO_LOCAL['username'] and password == USUARIO_LOCAL['password']:
        access_token, refresh_token = create_jwt_token(username)
        return Response({
            'access': access_token,
            'refresh': refresh_token
        })
    else:
        raise AuthenticationFailed('Credenciais inválidas')
