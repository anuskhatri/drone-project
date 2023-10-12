from flask import Blueprint, render_template, redirect, url_for

flight = Blueprint('flight', __name__)

@flight.route('/test', methods=['GET', 'POST'])
def test():
    # You can add more logic here to render a template or perform some action.
    return "test"

@flight.route('/location', methods=['GET', 'POST'])
def location():
    # You can add more logic here to render a template or perform some action.
    return "test"

@flight.route('/autonomous')
def autonomous():
    # You can add more logic here to render a template or perform some action.
    return "test"
