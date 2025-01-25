""" MY WSGI ENTRY POINT """
from app import create_buu


app = create_buu()

if __name__ == '__main__':
    app.run(port=5015)
