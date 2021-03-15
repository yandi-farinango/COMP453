from flask import Flask, render_template, url_for, flash, redirect
from flaskDemo.forms import RegistrationForm, LoginForm, SnackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Channah Naiman',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Peter Dordal',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

favSnacks = list()
favSnack = dict()
favSnack['snack']="Nestle's Crunch"
favSnack['calories'] = 101
favSnacks.append(favSnack)
favSnack=dict()
favSnack['snack']="KitKat"
favSnack['calories'] = 202
favSnacks.append(favSnack)

@app.route("/")
@app.route("/home")
def home():
    return render_template("snacks.html", title = "Tom", favSnacks = favSnacks)
    return render_template('home.html', favSnacks=favSnacks)
    


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/addSnack", methods=['GET', 'POST'])
def addSnack():
    form = SnackForm()
    if form.validate_on_submit():
        favSnack=dict()
        favSnack['snack'] = form.snackName.data
        favSnack['calories'] = form.calories.data
        favSnacks.append(favSnack)
        flash(f'Snack added for {form.snackName.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('addSnack.html', title='addSnack', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
