from extensions import db

user_list = []


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    telegram = db.Column(db.String(200), nullable=False, unique=True)
    age = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_telegram(cls, telegram):
        return cls.query.filter_by(telegram=telegram).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
