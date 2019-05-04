from app import application as sd_app
from app import db
db.create_all()
sd_app.run(host="0.0.0.0")
