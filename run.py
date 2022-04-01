from flask import Flask
from application.main.views import main_blueprint
from application.post.views import post_blueprint
from application.search.views import search_blueprint
from application.users_field.views import users_field_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_field_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
