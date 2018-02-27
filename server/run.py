import sys
import os
sys.path.append(os.path.abspath(os.pardir))

from server import app


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    #app.run(host="192.168.0.20")
    app.run()
