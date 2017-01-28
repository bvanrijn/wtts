import requests

import copy
from urllib.parse import urlencode



syn_parameters = {
    'text': '',
    'voice': 'en-US_AllisonVoice',
    'download': True,
    'accept': 'audio/ogg'
}

def main():
    text = input('Text: ')

    s = synthesize(text)

    with open('f.ogg', 'wb+') as f:
        f.write(s.content)


def synthesize(text):
    parameters = copy.copy(syn_parameters)
    
    parameters['text'] = text

    r = requests.get('https://text-to-speech-demo.mybluemix.net/api/synthesize?' + urlencode(parameters))

    return r


if __name__ == '__main__':
    main()