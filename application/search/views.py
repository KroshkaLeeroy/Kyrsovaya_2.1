from flask import Blueprint, render_template, request
import utils

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/search")
def search_page():
    s = request.args.get('s', "")
    posts = utils.search_for_posts(s)
    post_count = 0

    for post in posts:
        post_count += 1

    return render_template("search.html", posts=posts, post_count=post_count)


