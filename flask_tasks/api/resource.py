from flask_tasks import q

from flask import Blueprint
from flask_tasks.tasks.tasks import async_save_email

api_bp = Blueprint("api", __name__)

@api_bp.route("/send_email")
def send_email_route():
    result = q.enqueue(async_save_email)
    return "Email will be saved.", 200