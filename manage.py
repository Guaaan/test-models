from flask import Flask
from flask.templating import render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, User, Profile

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['ENV'] = 'production'
app.config['SQLALCHEMY_TRACK_MODIFICACIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://lrodriguez:derek.15@localhost:3306/testmodels'

db.init_app(app)
Migrate(app, db)
CORS(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.route('/')
def root():
    return render_template('index.html')


#############################################3
'''

user = User()
user.name = name


profile = Profile()
#profile.bio = request.json.get("bio", "")

user.profile = profile

phone = Phone()
phone.phone = "+56393939329"

user.phones.append(phone)

user.save()





'''

if __name__ == "__main__":
    manager.run()