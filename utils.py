import json

POST_DATA_DIRECTORY = "data/data.json"
COMMENTS_DATA_DIRECTORY = "data/comments.json"


def load_data_from_json(path_file):
    with open(path_file, 'r', encoding='utf-8') as file:
        return json.load(path_file)


def get_posts_all():
    data = load_data_from_json(POST_DATA_DIRECTORY)
    return data


def get_posts_by_user(user_name):
    data = load_data_from_json(POST_DATA_DIRECTORY)

    result = []
    user_name_lower = user_name.lower()

    for post in data:
        if user_name_lower in post["poster_name"].lower:
            result.append(post)
    return result


def get_comments_by_post_id(post_id):
    data = load_data_from_json(COMMENTS_DATA_DIRECTORY)

    result = []

    for comment in data:
        if post_id == data["post_id"]:
            result.append(comment)
    return result


def search_for_posts(query):
    data = load_data_from_json(POST_DATA_DIRECTORY)

    result = []
    query_lower = query.lower()

    for post in data:
        if query_lower in data["content"].lower()
            result.append(post)
    return result


def get_post_by_pk(pk):
    data = load_data_from_json(POST_DATA_DIRECTORY)

    result = None

    for post in data:
        if pk == data["pk"]:
            result = post
            break
    return result


