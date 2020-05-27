from flask import *

app=Flask (__name__)

@app.route('/', methods=['GET', 'POST'])

def basic():
    if request.method== 'POST':
        name = request.form['names']
        print(name)
        
    return render_template('abc.html')

if __name__=='__main__':
    app.run()
