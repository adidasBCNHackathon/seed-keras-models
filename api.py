import os

from flask import Flask
from modelname.api import DemoLoader


app = Flask(__name__)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.add_url_rule(
        '/predict/demo',
        view_func=DemoLoader.as_view('demo')
    )

    # If you are using debug=True it might broadcast a "failed to create cublas
    # handle: CUBLAS_STATUS_NOT_INITIALIZED" error
    app.run(host='0.0.0.0', port=port)
