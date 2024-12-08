from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Cliente, Contato, Pet, Raca, Atendimento
from django.contrib.auth.models import User


class ClienteAPITestCase(APITestCase):

    def setUp(self):
        # Crie um usuário para o teste
        self.usuario = User.objects.create_user(
            username='usuario_teste',
            password='senha123'
        )
        # Gere um token JWT para o usuário
        refresh = RefreshToken.for_user(self.usuario)
        self.token = str(refresh.access_token)

    def test_criar_cliente(self):
        url = reverse('cliente-list')  # Ajuste conforme o nome da URL
        data = {
            'nome': 'João Silva',
            'cpf': '12345678901',
        }

        # Agora, passe o token na requisição
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Imprima a resposta para debug, caso necessário
        print(response.data)

        # Verifique se o status da resposta é 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)