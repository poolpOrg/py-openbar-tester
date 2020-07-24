import openbar.routes
import openbar.params


@openbar.routes.register("0.1", "backend")
def setup(app):
    app.post("/")(post_root)


def post_root():
    with openbar.params.json() as j:
        test = j.string('test', default=None)
    return {'test': test}
