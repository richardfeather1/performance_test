# import flask dependencies
from flask import Flask, render_template, request
from forms.intro import IntroForm

app = Flask(__name__, template_folder='templates')
app.secret_key = '7tioyugfhvj'  # necessary to encrypt data submitted


@app.route('/', methods=['GET', 'POST'])
def intro():  # create introduction page
    form = IntroForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        return render_template('hello.html', name=name)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # runs in port 5000 by default, debug enabled to help with development.
