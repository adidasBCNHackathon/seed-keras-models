from flask import jsonify, request, abort
from flask.views import MethodView

import modelname.model as model


class DemoLoader(MethodView):
    """
    Summarize predictor
    """

    def __init__(self):
        """Initialize ModelLoader class."""
        pass

    def post(self):
        if not request.json:
            abort(400)

        seq = request.json["input"].lower()
        #  TODO: create predict function in model
        #  sample = model.predict(seq, chunk_size=5000)

        return jsonify(
            input=seq,
            prediction=sample
        )
