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
    # Get the text
    text = input('Text: ')

    # Synthesize it
    s = synthesize(text)

    # Write it to a `f.ogg` file, overwriting it if it exists
    with open('f.ogg', 'wb+') as f:
        f.write(s.content)


def synthesize(text):
    # Don't modify the original object
    parameters = copy.copy(syn_parameters)
    
    # Set the text
    parameters['text'] = text

    # Request foo!
    r = requests.get('https://text-to-speech-demo.mybluemix.net/api/synthesize?' + urlencode(parameters))

    return r

if __name__ == '__main__':
    # watsontts was called directly
    main()