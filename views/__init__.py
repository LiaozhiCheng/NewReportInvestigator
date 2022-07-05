from .news_api import news_api



normal_prefix = '/cdal/5000/api'
blueprint_prefix = [(news_api, "/news_api/v1")]


def register_blueprint(app):
    for blueprint, prefix in blueprint_prefix:
        app.register_blueprint(blueprint, url_prefix=normal_prefix+prefix)
    return app