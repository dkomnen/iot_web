import sys
import os
sys.path.append(os.path.abspath(os.pardir))

from server import app


if __name__ == "__main__":
    app.run()
