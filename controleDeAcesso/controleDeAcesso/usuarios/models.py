from django.db import models


class UsuariosSearch(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains=query) | \
			models.Q(created_at__icontains=query))


class UsuariosModel(models.Model):

	name = models.CharField('Nome', max_length=100)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	is_active = models.BooleanField('Está ativo?', blank=True, default=True)
	objects = UsuariosSearch()

	def __str__(self):
		return self.name


class HistoricoSearch(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains=query) | \
			models.Q(created_at__icontains=query))


class HistoricoModel(models.Model):
	usuario = models.ForeignKey(UsuariosModel, on_delete=models.CASCADE, null=True)
	time = models.DateTimeField('Autorizado em', auto_now_add=True)

	objects = HistoricoSearch()

	def __str__(self):
		return self.id