from flask import Blueprint, render_template, url_for, redirect
from crowd.main.form import HomeForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()

    if form.validate_on_submit():
        if form.registration.data:
            return redirect(url_for('users.register'))
        elif form.authentication.data:
            return redirect(url_for('users.login'))

    return render_template('home.html', form=form)


@main.route('/blog')
def blog():
    return render_template('blog.html', title='Блог')


