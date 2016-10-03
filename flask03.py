# flask03.py
from flask import Flask, render_template, request
app = Flask(__name__)

# HTTPメソッドのGETを取得し入力されたテキストボックスの値をtext1に代入してください

@app.route('/')
def form_index():
    if request.method == "":
        if 'text1' in request.args:
            return render_template(
                'flask03.html',
                text1=request.args['']
            )
    return render_template('flask03.html')

if __name__ == '__main__':
    app.run(debug=True)
