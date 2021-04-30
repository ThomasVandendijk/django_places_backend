from django.test import TestCase
from google_places.utils import search_places_by_text, retrieve_results, filter_json_with_parameters_list
from google_places.constants import mappings


class TestUtils(TestCase):

    def test_search_places(self):
        test_text = "Leuven"
        response = search_places_by_text(test_text)
        results = retrieve_results(response)
        print(results[0][mappings.ADDRESS])
        self.assertTrue(test_text in results[0][mappings.ADDRESS])

    def test_filter_json_one_param(self):
        test_text = "Leuven"
        response = search_places_by_text(test_text)
        results = retrieve_results(response)
        filtered_data = filter_json_with_parameters_list(results, parameters=[mappings.ADDRESS])
        print(filtered_data)
        self.assertTrue(test_text in filtered_data[0][mappings.ADDRESS])
        self.assertFalse(mappings.NAME in filtered_data[0])

    def test_filter_json_two_param(self):
        test_text = "Leuven"
        response = search_places_by_text(test_text)
        results = retrieve_results(response)
        filtered_data = filter_json_with_parameters_list(results, parameters=[mappings.ADDRESS, mappings.NAME])
        print(filtered_data)
        self.assertTrue(test_text in filtered_data[0][mappings.ADDRESS])
        self.assertTrue(mappings.NAME in filtered_data[0])
        self.assertFalse(mappings.RATING in filtered_data[0])
