from flask import Blueprint, render_template, current_app, jsonify
import utils

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route('/')
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/api/posts')
def api_posts():
    posts = utils.get_posts_all()
    return jsonify(posts)
