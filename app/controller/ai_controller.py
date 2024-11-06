from flask import Blueprint, request, jsonify
from app.utils.dependency_injector import injector

ai_blueprint = Blueprint('ai', __name__)


@ai_blueprint.route('/answer', methods=['POST'])
def answer():
    message = request.json['message']

    ai_service = injector.get('ai_repository')
    response = ai_service.answer_message(message)

    return response
