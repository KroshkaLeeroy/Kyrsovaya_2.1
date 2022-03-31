from flask import Blueprint, render_template
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
