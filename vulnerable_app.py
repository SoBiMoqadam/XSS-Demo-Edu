from flask import Flask, request


app = Flask(__name__)


html_form = '''
<form method="GET">
<input type="text" name="name">
<button type="submit">Submit</button>
</form>
<div>{output}</div>
'''


@app.route('/', methods=['GET'])
def index():
name = request.args.get('name', '')
return html_form.format(output=name)


if __name__ == '__main__':
app.run(debug=True)
