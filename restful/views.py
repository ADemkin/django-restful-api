from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from .forms import DictionaryForm
from .dictionary import *
import requests


def index(request):
    # clear cache for geo example
    request.session.flush()
    return render(request, 'restful/index.html')


def geo(request):
    is_chached = ('geo' in request.session)
    
    if not is_chached:
        try:
            api_data = requests.get('http://freegeoip.net/json/')
        except Exception as message:
            return error(request, message)
        
        request.session['geo'] = api_data.json()
    
    json_data = request.session['geo']
    
    context = {
        'ip'        :json_data['ip'],
        'city'      :json_data['city'],
        'country'   :json_data['country_name'],
        'latitude'  :json_data['latitude'],
        'longitude' :json_data['longitude'],
        'api_key'   :settings.GOOGLE_MAPS_API_KEY,
        'is_chached':is_chached,
    }
    
    return render(request, 'restful/geo.html', context)


def github(request):
    user_data = {}
    rate = {}
    if 'username' in request.GET and request.GET['username'] != '':
        username = request.GET['username']
        try:
            api_data = requests.get(f'https://api.github.com/users/{username}')
        except Exception as message:
            return error(request, message)
        
        user_data = api_data.json()
        
        headers = api_data.headers
        
        rate['limit'] = headers['X-RateLimit-Limit']
        rate['remain'] = headers['X-RateLimit-Remaining']
        
        if rate['remain'] == '0':
            unban_time = datetime.fromtimestamp(int(headers['X-RateLimit-Reset']))
            rate['unban_time'] = unban_time.strftime('%H:%M:%S')
    
    return render(request, 'restful/github.html', context={'user':user_data, 'headers':rate})


def dictionary(request):
    word_info = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            word_info['successful'] = False
            word_to_search = form.search()
            try:
                oxford_response = get_dictionary(word_to_search,
                                                 api_id=settings.OXFORD_API_ID,
                                                 api_key=settings.OXFORD_API_KEY)
            except Exception as message:
                return error(request, message)
            
            if oxford_response.status_code == 200:
                
                search = oxford_response.json()
                
                word_info['successful'] = True
                
                word_info['word'] = get_word(search)
                word_info['definitions'] = get_definitions(search)
                word_info['phonetic_spelling'] = get_phonetic_spelling(search)
                word_info['audio_file'] = get_audio_file(search)
                word_info['dialects'] = get_dialects(search)
            
            else:
                word_info['successful'] = False
                
                if oxford_response.status_code == 404:
                    word_info['error'] = f"{word_to_search} not found in dictionary."
                
                else:
                    word_info['error'] = "Oxford server not available. Try again later."
    else:
        form = DictionaryForm()
    
    context = {
        'form'  :form,
        'search':word_info
    }
    return render(request, 'restful/dictionary.html', context)


def error(request, details=''):
    error = {
        'title'  :'Error',
        'message':'Failed to establish a new connection.',
        'details':details,
    }
    return render(request, 'restful/error.html', error)
