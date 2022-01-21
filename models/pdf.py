from db import db


ALLOWED_EXTENSIONS = {'html'}


class Profile(db.Model):

    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.FileField, nullable=False)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


    def __init__(self, file):
        self.file = file
        
    def __repr__(self):
        record = {
            "file" : self.file
        } 
        return record    
        
    def serialize(self):
        return {"file": self.file}
        
        
    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
