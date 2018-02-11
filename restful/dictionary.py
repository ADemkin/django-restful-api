import requests


def get_dictionary(search, api_id, api_key):
    language = 'en'
    url = f'https://od-api.oxforddictionaries.com:443/api/v1/entries/{language}/{search.lower()}'
    headers = {
        "app_id" :api_id,
        "app_key":api_key,
    }
    return requests.get(url=url, headers=headers)


def get_word(search):
    return search["results"][0]["word"]


def get_dialects(search):
    dialects = set()
    try:
        for results in search["results"]:
            for lexicalEntries in results["lexicalEntries"]:
                # sometimes there are no "pronunciations"
                for pronunciation in lexicalEntries["pronunciations"]:
                    # sometimes there are no "dialects"
                    for dialect in pronunciation["dialects"]:
                        dialects.add(dialect)
    except:
        pass
    return list(dialects)


def get_audio_file(search):
    pronunciation = []
    try:
        for results in search["results"]:
            for lexicalEntries in results["lexicalEntries"]:
                # sometimes there are no "pronunciations"
                for pronunciations in lexicalEntries["pronunciations"]:
                    # sometimes there are no "audioFile"
                    pronunciation.append(pronunciations["audioFile"])
    except:
        pass
    if pronunciation:
        return pronunciation[0]


def get_phonetic_spelling(search):
    phonetic_spelling = set()
    try:
        for results in search["results"]:
            for lexicalEntries in results["lexicalEntries"]:
                # sometimes there are no "pronunciations"
                for pronunciations in lexicalEntries["pronunciations"]:
                    # sometimes there are no "phoneticSpelling"
                    phonetic_spelling.add(pronunciations["phoneticSpelling"])
    except:
        pass
    return list(phonetic_spelling)


def get_definitions(search):
    definitions = set()
    try:
        for results in search["results"]:
            for lexicalEntries in results["lexicalEntries"]:
                for entries in lexicalEntries["entries"]:
                    for senses in entries["senses"]:
                        # sometimes there are no "definitions"
                        definitions.add(senses["definitions"][0])
    except:
        pass
    return list(definitions)
