# flask02.py      
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/pow/<int:x>/<int:y>/')
def web_pow(x, y):
	# xのy乗を結果としてresultに返すようにして下さい

    return render_template('flask02.html', x=x, y=y, result=result)

if __name__ == '__main__':
    app.run()
