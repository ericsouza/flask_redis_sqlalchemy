from flask_tasks.database import db

class EmailExample(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(50))
    subject = db.Column(db.String(50))
    content = db.Column(db.Text)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

