# mymodule/views.py

from flask import Blueprint, current_app, render_template
from myexts.sqlalchemy import db
from mymodule.models import User

blueprint = Blueprint(
    'mymodule',
    __name__,
    template_folder='templates',
)

@blueprint.route("/")
def index():
    db.session.add((User(username="Flask", email="example@example.com")))
    db.session.commit()
    user = User.query.first()
    return render_template(
        'mymodule.html',
        greeting="%s %s" % (current_app.config['MYMODULE_GREETING'], user.username)
    )
