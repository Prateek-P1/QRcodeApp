import validators
import webbrowser

def url_validator(url):
    validation=validators.url(url)
    if validation:
        return 'T'
    else:
        return 'F'

def url_opener(url):
    webbrowser.open(url,0,True)