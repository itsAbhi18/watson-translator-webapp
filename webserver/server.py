from distutils.log import debug
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    #print(textToTranslate)
    fr_text = translator.en_to_fr(textToTranslate)
    #print(fr_text)
    return fr_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    #print(textToTranslate)
    # Write your code here
    en_text = translator.fr_to_en(textToTranslate)
    #print(en_text)
    return en_text

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
