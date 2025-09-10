from flask import Flask, request, escape


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
name = request.args.get('name', '')
safe_name = escape(name)
return f'<h1>Hello {safe_name}</h1>'


if __name__ == '__main__':
app.run(debug=True)
