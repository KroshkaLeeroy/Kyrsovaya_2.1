from flask import Blueprint, render_template
# Можно ли импортировать фласк целиком?, зачем импоритровать по отдельности
import utils

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
# Для чего используется __name__
# Откуда начинается путь для templates


@main_blueprint.route('/')
def main_page():
    posts = utils.get_posts_all()
    # как сократить количество контнетна показываемого, как сделать выезжающую подробнее
    return render_template('index.html', posts=posts)


