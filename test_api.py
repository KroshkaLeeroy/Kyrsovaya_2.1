from run import app


def test_home_page():
    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200


def test_api():
    flask_app = app

    with flask_app.test_client() as test_client:
        response = test_client.get("/api/posts")
        assert response.status_code == 200
        assert isinstance(response.json, list)
        assert len(response.json) > 0


def test_api_post():
    flask_app = app

    with flask_app.test_client() as test_client:
        resource = test_client.get("/api/posts/1")
        assert resource.status_code == 200
        assert isinstance(resource.json, dict)
        assert len(resource.json) > 0
