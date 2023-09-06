import random
from flask import Flask, render_template_string, render_template, request

app = Flask(__name__)




nicknames = ['%s']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        p = request.values.get('nickname')
        id = random.randint(0, len(nicknames) - 1)
            
        return render_template_string(nicknames[id] % p)

       
			
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
