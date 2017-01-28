# wtts

Watson Text-to-Speech in Python.

## API

### `watsontts.synthesize(text: str) -> requests.Response`
Perform text-to-speech on the given text.

## Usage

### python-telegram-bot

Here's a function you can build upon to bring `wtts` to your bot.<br>
(Imports and handlers omitted for brevity)

```python
def tts(bot, update):
    text = update.message.text
    
    tmp_f = open('tmp.ogg', 'wb+')
    tmp_f.write(watsontts.synthesize(text).content)

    bot.sendAudio(update.message.chat_id, audio=open('tmp.ogg', 'rb'))

    tmp_f.close()
    os.remove('tmp.ogg')
```

### Try it

[Try it online](https://www.ibm.com/watson/developercloud/text-to-speech.html#try-it-out-block) or run `python3 watsontts.py`

## License

MIT. See [LICENSE](LICENSE).
