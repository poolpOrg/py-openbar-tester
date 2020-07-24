import openbar.routes
import openbar.params

from . import db_tester_0_1


@openbar.routes.register("0.1", "backend")
def setup(app):
    app.get("/")(post_root)


def post_root():
    with openbar.params.json() as j:
        test = j.string('test', default=None)

    with db_tester_0_1.connector("tester-database") as conn:
        conn.test()

    return {'test': test}
