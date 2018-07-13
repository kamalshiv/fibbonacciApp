from flask import Flask, jsonify, abort, make_response, current_app
from fibbohelper import makeFibboSeries

from flask import (
    Blueprint, request
)

bp = Blueprint('fibbo', __name__, url_prefix='/fibbonacci/api/v1.0')

@bp.route('/series/<num>', methods=['GET'])
def getFibboSeries(num):
    current_app.logger.debug('Request received to get fibbonacci series for numbers %s', num)
    try:
        num = int(num)
    except:
        current_app.logger.debug('The requested param %s is not an integer', num)
        abort(400)
    if num > 0 :
        series = list(makeFibboSeries(num))
    else :
        current_app.logger.debug('The requested param %s is negative integer', num)
        abort(400)
    return jsonify(series)

@bp.errorhandler(400)
def invalidValue(error):
    return make_response(jsonify({'error': 'Please enter a positive integer value'}), 400)

@bp.errorhandler(404)
def notFoundError(error):
    return make_response(jsonify({'error': 'Please check the url entered'}), 404)