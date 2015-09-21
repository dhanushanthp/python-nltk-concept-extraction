from flask import Flask, url_for, request
from logging.config import thread
# exec(open("readPython.py").read())
execfile("readPython.py")
import readPython

application = Flask(__name__)
    
@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
           return readPython.getRelatedConcepts(request.data);
        except Error(e):
            print (e);
    else:
        return readPython.getRelatedConcepts(request.args['concept'],request.args['topcount']);

if __name__ == '__main__':
#     application.run(host='0.0.0.0',port=8080,threaded=True);
    application.run(threaded=True)
