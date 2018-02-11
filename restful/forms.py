from django import forms
import requests

OXFORD_API_ID = 'aafa69b5'
OXFORD_API_KEY = '4c54227a3ed47c2db5d4eae1ee9320c9'


class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                                   attrs={
                                       'class'      :'form-control col-sm-3 ml-3',
                                       'placeholder':'Enter word',
                                   }
                           ))
    
    def search(self):
        'https://od-api.oxforddictionaries.com/api/v1'
        # result = {}
        #
        # word = self.cleaned_data['word']
        # language = 'en'
        # url = f'https://od-api.oxforddictionaries.com:443/api/v1/entries/{language}/{word.lower()}'
        # headers = {
        #     "app_id" :OXFORD_API_ID,
        #     "app_key":OXFORD_API_KEY
        # }
        # try:
        #     response = requests.request('GET', url, headers=headers)
        # except:
        #     result['successful'] = False
        #     result['error'] = f'Oxford server is not available. Try again later.'
        #     return result
        #
        # if response.status_code == 200:
        #     result = response.json()
        #     result['successful'] = True
        # else:
        #     result['successful'] = False
        #     if response.status_code == 404:
        #         result['error'] = f'{word.capitalize()} is not found in dictionary.'
        #     else:
        #         result['error'] = f'Unknown error. Something went wrong. Sorry about that.'

        return self.cleaned_data['word']
