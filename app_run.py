from app import create_app
from config import HOST, PORT


if __name__ == '__main__':
    app = create_app()
    # app = create_app(host=HOST, port=PORT)
    app.run(host=HOST, port=PORT)
