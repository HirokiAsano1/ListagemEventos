from django.test import TestCase, Client
from datetime import date
from agenda.models import Evento , Categoria


# Create your tests here.
class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")


class TestListagemDeEventos(TestCase):
    def test_evento_Com_data_hoje(self):
        categoria = Categoria()
        categoria.name ="Backend"
        categoria.save()
        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local ="Rio de Janeiro"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertEqual(list(response.context["eventos"]), [evento])
    
    def test_eventos_sem_Data_sao_exibidos(self):
        categoria = Categoria()
        categoria.name ="Backend"
        categoria.save()
        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local ="Rio de Janeiro"
        evento.data = None
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertContains(response, "A definir")
        self.assertEqual(list(response.context["eventos"]), [evento])