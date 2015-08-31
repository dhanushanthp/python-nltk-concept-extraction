from flask import Flask, url_for, request
execfile("extractor.py")
import extractor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.data
            toks = nltk.regexp_tokenize(data, sentence_re)
            postoks = nltk.tag.pos_tag(toks)
            tree = chunker.parse(postoks)
            terms = extractor.get_terms(tree)

            list = []
            uniqueSet = []
            for term in terms:
                concept = ''
                for word in term:
                    concept = concept + ' ' + word
                list.append(concept.strip())

            json = '{"concepts": ['
            for concept in set(list):
                json = json + '"' + concept + '",'
            json = json + ']}'

            json = json.replace(',]}', ']}')
            return json
        except Error(e):
            print e
    else:
        return 'get'

if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8080,threaded=True)
    app.run()
