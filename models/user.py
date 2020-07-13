from flask_sqlalchemy import SQLAlchemy

# Create DB instance
Db = SQLAlchemy()


class User(Db.Model):
    # Fields
    __tablename__ = 'users'
    user_id = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    first_name = Db.Column(Db.String(64), nullable=False)
    age = Db.Column(Db.Integer, nullable=False)

    def setAge(self, age):
        age = age

    def setName(self, name):
        first_name = name

    # toString
    def toString(self):
        print(f"{self.user_id}: {self.first_name} ({self.age})")