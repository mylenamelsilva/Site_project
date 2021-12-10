from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/sobre')
def sobre():
    return render_template("sobre.html")

@views.route('/acervo')
def acervo():
    return render_template("acervo.html")

@views.route('/o-que-é-inovação')
def pg2():
    return render_template("pg2.html")

@views.route('/como-se-classificam-as-inovações')
def pg3():
    return render_template("pg3.html")

@views.route('/como-inovar')
def pg4():
    return render_template("pg4.html")

@views.route('/o-que-caracteriza-um-sujeito-inovador')
def pg5():
    return render_template("pg5.html")

@views.route('/o-ambiente-afeta-a-inovação')
def pg6():
    return render_template("pg6.html")

@views.route('/por-que-as-empresas-inovam')
def pg7():
    return render_template("pg7.html")

@views.route('/como-captar-recursos-para-inovações')
def pg8():
    return render_template("pg8.html")