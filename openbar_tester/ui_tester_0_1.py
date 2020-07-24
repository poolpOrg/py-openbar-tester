import openbar.routes
import openbar.sessions
import openbar.templates


@openbar.routes.register("0.1", "frontend")
def setup(app):
    app.get("/")(get_root)
    app.get("/session-reset")(get_session_reset)


@openbar.templates.render("test.html")
def get_root():
    session = openbar.sessions.current()
    session['counter'] = session.get('counter', 0) + 1
    session.save()

    return {'counter' : session['counter']}

def get_session_reset():
    session = openbar.sessions.current()
    session.delete()

    return {}
