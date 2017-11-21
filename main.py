from flask import Flask, render_template_string, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """


<!DOCTYPE html >
<html>
    <head>
        <style>
            form {{
                background - color:  # eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans - serif;
                border-radius: 10px; }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px; }}
        </style>
    </head>
    <body >
      <form method= 'POST'>
       <form>
       <label>Rotate by:
            <input name="rot" type="text" />
        </label>
        <textarea name='message'>{0}</textarea>
        <br>
        <input type="submit"/>
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    message = request.form['message']

    encrypted_message = rotate_string(message, rot)
    return form.format(encrypted_message)


app.run()
