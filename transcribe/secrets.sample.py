bing_speech_api_key = "bing speech api key"
# The actual credential string is massive, so you'll want to use triple quotes here so you can span multiple lines
# Must double escape any \n characters; this is an awful way to store this anyway
google_credentials_json = '''
    {"project_id": "..."}
    '''
google_preferred_phrases = [
    'list of phrases', ]  # https://cloud.google.com/speech/docs/basics#phrase-hints
