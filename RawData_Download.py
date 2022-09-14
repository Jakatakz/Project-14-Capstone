
# coding: utf-8

# In[6]:


import requests

def download_file_from_google_drive(id, destination):
    URL = "https://drive.google.com/uc?export=download&confirm=s5vl&id=1yJKqx4mhvbpwKPyJaNUq7J9cGy7wuqi5"
    

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

file_id = 'T1yJKqx4mhvbpwKPyJaNUq7J9cGy7wuqi5'
destination = 'endomondoHR.json.gz'
download_file_from_google_drive(file_id, destination)

print('file is downloaded.')

