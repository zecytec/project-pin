from flask import Flask, render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=formLogin)



@app.route('/criarconta', methods=['GET', 'POST'])
def criar_conta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data, email=formcriarconta.email.data, senha=senha)
        #duvida
    
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criar_conta.html', form=formcriarconta)



@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))
    if id_usuario == int(current_user.id):
        #usuario vê o proprio perfil
        return render_template('perfil.html', usuario=current_user)
    else:
        #vê o de outro usuario
        return render_template('perfil.html', usuario=usuario)
    
 


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))