from flask_tasks.models import EmailExample
from flask_tasks import q


def async_save_email():
    email = EmailExample(
        sender='someone@example.com', 
        subject='Example Email', 
        content='This is an example email to save in database.'
	)
    
    email.save_to_db()