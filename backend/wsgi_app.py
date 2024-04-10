from client.main_view import View

client_view = View()

def wsgi_application(environ, start_resonse):
    headers = [('Content-type', 'text/html')]
    try:
        body = client_view.get_body().encode("utf-8")
        status = "200 OK"
        client_view.flag = False
    except Exception:
        body = b"Error"
        status = "404 Not Found"

    start_resonse(status, headers)
    return [body]