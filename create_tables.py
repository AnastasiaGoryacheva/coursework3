from project.config import DevelopmentConfig
from project.server import create_app
from project.setup_db import db

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # db.drop_all()
