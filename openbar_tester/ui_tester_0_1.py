import openbar.routes
import openbar.templates


@openbar.routes.register("0.1", "frontend")
def setup(app):
    app.get("/")(get_root)


@openbar.templates.render("test.html")
def get_root():
    return {'test' : 42}
