from django.test import TestCase
from django.urls import reverse
from .models import Restaurant


class RestaurantsPageTestCase(TestCase):
    def test_restaurants_page(self):
        response = self.client.get(reverse('RESTAURANTS:restaurants'))
        self.assertEqual(response.status_code, 200)


class DetailsPageTestCase(TestCase):
    def setUp(self):
        impossible = Restaurant.objects.create(name="un restaurant", email="unrestaurant@gmail.com", adresse="1 avenue des restaurants", codePostal=35470, ville="Poitiers", phone="05 24 28 91 37", website="unrestaurant.fr", image="un_restaurant.png")
        self.resto = Restaurant.objects.get(name="un restaurant", email="unrestaurant@gmail.com", adresse="1 avenue des restaurants", codePostal=35470, ville="Poitiers", phone="05 24 28 91 37", website="unrestaurant.fr", image="un_restaurant.png")

    def test_details_page_return_200(self):
        restaurant_id = self.resto.id
        response = self.client.get(reverse('RESTAURANTS:details', args=(restaurant_id,)))
        self.assertEqual(response.status_code, 200)

    def test_details_page_return_404(self):
        restaurant_id = self.resto.id + 1
        response = self.client.get(reverse('RESTAURANTS:details', args=(restaurant_id,)))
        self.assertEqual(response.status_code, 404)
