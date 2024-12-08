from django.db import models

class Usuario(models.Model):
    CPF = models.CharField(max_length=11, unique=True, primary_key=True)  # CPF como chave primária
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)
    perfil = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Cliente', 'Cliente')])

    objects = models.Manager()

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)  # ID automático como chave primária
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11, unique=True)  # CPF único, mas não chave primária
    data_de_cadastro = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)  # ID automático como chave primária
    logradouro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=200, blank=True, null=True)  # Campo opcional
    tag = models.CharField(max_length=50)
    identificador_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="enderecos")  # Ligação com Cliente

    objects = models.Manager()

    def __str__(self):
        return f"{self.logradouro}, {self.cidade}"


class Raca(models.Model):
    id_raca = models.AutoField(primary_key=True)  # ID automático como chave primária
    nome_raca = models.CharField(max_length=75)

    objects = models.Manager()

    def __str__(self):
        return self.nome_raca


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)  # ID automático como chave primária
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pets")  # Ligação com Cliente
    id_raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, related_name="pets")  # Ligação com Raça (opcional)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    objects = models.Manager()

    def __str__(self):
        return self.nome


class Atendimento(models.Model):
    id_atend = models.AutoField(primary_key=True)  # ID automático como chave primária
    id_pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="atendimentos")  # Ligação com Pet
    descricao_do_atendimento = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return f"Atendimento do {self.id_pet.nome} - {self.data}"
