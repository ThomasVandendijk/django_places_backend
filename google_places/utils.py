import requests
from google_places.constants import urls, mappings
from backend_thefridge import settings


def get_key_part_url():
    return '&key=' + settings.GOOGLE_PLACES_API_KEY


def quote_string(str):
    return "'" + str + "'"


def filter_json_with_parameters_list(data_json, parameters):
    result_lst = []
    for item in data_json:
        item_dict = {}
        for parameter in parameters:
            if parameter in item:
                item_dict[parameter] = item[parameter]
        if item_dict:
            result_lst.append(item_dict)
    return result_lst


def retrieve_results(json_data):
    return json_data[mappings.RESULTS]


def search_places_by_text(search_text):
    quoted_search_text = quote_string(search_text)
    url = urls.GOOGLE_PLACES_URL + quoted_search_text + get_key_part_url()
    response = requests.get(url)
    return response.json()


def retrieve_places_by_parameters(search_text, parameters):
    response = search_places_by_text(search_text)
    results = retrieve_results(response)
    return filter_json_with_parameters_list(results, parameters)

print(retrieve_places_by_parameters("resto brussel", ['photos']))
