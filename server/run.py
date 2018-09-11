import sys
import logging

sys.path.append('./')

from livereload import Server

from myapp import app

def main(init_logger=True):
    if init_logger:
        app.debug = True
        # Logger config
        logging.getLogger("werkzeug").setLevel(logging.WARNING) # tunrning off spammer
    else:
        app.debug = False
    # if developing the webpage, run with livereload watcher
    if app.debug:
        server = Server(app.wsgi_app)
        server.serve(port=5000)
    else:
        app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
