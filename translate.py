import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
    "q": "Hello, world!",
    "target": "ur",
    "source": "en"
}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "3129d9460bmsh5e467d04a6888cap13f4fcjsn7c3ce3b8431a",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

data = response.json()['data']
translatedText = data['translations'][0]['translatedText']
print(translatedText.sort(ascending=False))
