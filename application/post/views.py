from flask import Blueprint, render_template, current_app, jsonify
import utils

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")


@post_blueprint.route("/post/<int:pk>")
def post_page(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    comment_count = 0

    for comment in comments:
        comment_count += 1

    return render_template('post.html', post=post, comments=comments, comment_count=comment_count)


@post_blueprint.route('/api/posts/<post_id>')
def api_posts(post_id):
    posts = utils.get_post_by_pk(post_id)
    return jsonify(posts)