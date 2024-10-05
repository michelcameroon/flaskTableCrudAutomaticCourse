
#from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy

from flask import current_app

def create_course_model(db):  # Pass db instance as an argument


    class CourseModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        description = db.Column(db.Text)
        # Other columns...

    
        def __repr__(self):
            return f'<CourseModel {self.id}>'

        def __init__(self, name, description):
            self.name=name
            self.description=description

    return CourseModel


#CourseModel = create_course_model(db)  # Call the function to create the model


