from django.test import TestCase

from django.test import Client
from core.models import Calculation

# Create your tests here.

#=== VIEWS ===
class CoreViewsTest(TestCase):
    def test_view_page_calculator_online(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)

#=== MODELS ===
class CalculationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Calculation.objects.create(expression="2 + 2", result="4")
    
    def test_expression_label(self):
        calculation = Calculation.objects.get(id=1)
        field_label = calculation._meta.get_field('expression').verbose_name
        self.assertEquals(field_label, 'expression')
    
    def test_result_label(self):
        calculation = Calculation.objects.get(id=1)
        field_label = calculation._meta.get_field('result').verbose_name
        self.assertEquals(field_label, 'result')
    
    def test_expression_max_length(self):
        calculation = Calculation.objects.get(id=1)
        max_length = calculation._meta.get_field('expression').max_length
        self.assertEquals(max_length, 100)
    
    def test_result_max_length(self):
        calculation = Calculation.objects.get(id=1)
        max_length = calculation._meta.get_field('result').max_length
        self.assertEquals(max_length, 100)
    
    def test_method_str(self):
        calculation = Calculation.objects.get(id=1)
        self.assertEquals(str(calculation), "2 + 2 = 4")