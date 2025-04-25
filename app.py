from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, AnonymousIdentity
from users import users, get_user_by_username, User

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Login manager setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Principal setup
principals = Principal(app)
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def home():
    return '<h1>Bienvenido a la app Flask con roles</h1><a href="/login">Iniciar sesión</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            identity_changed.send(app, identity=Identity(user.id))
            return redirect(url_for('dashboard'))
        flash('Credenciales inválidas.')
    return '''
        <form method="post">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    '''

@app.route('/dashboard')
@login_required
def dashboard():
    return f'<h2>Hola, {current_user.username}</h2><p>Bienvenido al panel de usuario.</p>'

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return '<h2>Sección de administrador</h2><p>Acceso autorizado.</p>'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
