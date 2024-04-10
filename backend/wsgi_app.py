from client.main_view import View

client_view = View()

def open_html(view):
    template = view.template
    with open(f"client/{template}", "rb") as html:
        encoded_data = html.read()

    return encoded_data

def wsgi_application(environ, start_response):
    headers = [('Content-type', 'text/html')]
    try:
        body = open_html(client_view)
        status = "200 OK"
        client_view.flag = False
    except Exception as e:
        print(e)
        body = b"Error"
        status = "404 Not Found"

    start_response(status, headers)
    return [body]