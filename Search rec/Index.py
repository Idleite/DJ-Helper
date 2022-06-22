
import requests

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

search = "Riptide"

Search_URL = '	https://api.spotify.com/v1/search'
par = { 'q': search, 'type': 'track', 'limit': '1' }
# POST
Search_response = requests.get(Search_URL, params={ 'q': search, 'type': 'track', 'limit': '1' }, headers={
    'Accept': 'application/json',
    'content_type': 'application/json',
    'Authorization' : 'Bearer ' + access_token
})
print(Search_response.text)