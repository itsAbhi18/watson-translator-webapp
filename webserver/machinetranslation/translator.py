"""
Translation functions that uses watson api to translate
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-10-13',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def en_to_fr(en_text):
    """
    Translates ENGLISH to FRENCH
    """
    fr_translation = language_translator.translate(
    text=en_text,
    model_id='en-fr').get_result()
    fr_translation = fr_translation["translations"]
    fr_translation = fr_translation[0]
    fr_translation = fr_translation["translation"]
    return fr_translation

def fr_to_en(fr_text):
    """
    Translates FRENCH to ENGLISH
    """
    en_translation = language_translator.translate(
    text=fr_text,
    model_id='fr-en').get_result()
    en_translation = en_translation["translations"]
    en_translation = en_translation[0]
    en_translation = en_translation["translation"]
    return en_translation
    
if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")