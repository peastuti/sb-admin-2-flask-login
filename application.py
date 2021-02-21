from flask import render_template
from flask_login import login_required, current_user, login_required
import jinja2.exceptions
from project import create_app

application = create_app()

@application.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)
    
@application.route('/<pagename>')
@login_required
def admin(pagename):
    return render_template(pagename+'.html', user=current_user)

@application.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@application.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    application.run( debug=True )
