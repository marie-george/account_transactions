import requests
import json


def get_bank_data():
    export_json = requests.get('https://api.npoint.io/786486118ec5de8bdd64')
    bank_data = export_json.json()
    return bank_data


