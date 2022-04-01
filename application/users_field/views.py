from flask import Blueprint, render_template, request
import utils

users_field_blueprint = Blueprint("users_field_blueprint", __name__, template_folder="templates")


@users_field_blueprint.route("/users/<username>")
def users_field_page(username):
    posts = utils.get_posts_by_user(username)

    return render_template("user-feed.html", posts=posts, username=username)
