flag = True

class View():
    flag = True

    def get_body(self):
        # Solely for testing exceptions
        if not self.flag:
            raise Exception

        return "<h1>Hello from the client side</h1>"