import requests
import json

def get_bank_data():
    export_json = requests.get('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230206T201720Z&X-Amz-Expires=86400&X-Amz-Signature=53b7ea53068a51f44d11c58a49f1491bbc370e1496eea905492528682c764499&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject')
    bank_data = export_json.json()
    return bank_data


