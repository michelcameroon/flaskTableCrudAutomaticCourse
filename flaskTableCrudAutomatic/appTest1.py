from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import insert,update

from models import create_course_model


database1 = 'schoolAdmin.db'

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schoolAdmin.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database1
db = SQLAlchemy(app)

# Create the CourseModel class
CourseModel = create_course_model(db)

table1 = 'course_model'



import fieldNamesInTable


app.app_context().push()






@app.route('/')
def index():
    print ('table1=')
    print (table1)
    namesNoId = fieldNamesInTable.namesNoId(database1, table1)
        
    records = CourseModel.query.all()
    return render_template('index.html', records=records, namesNoId=namesNoId)


@app.route('/new', methods=['GET', 'POST'])
def new_record():
    namesNoId = fieldNamesInTable.namesNoId(database1, table1)
    if request.method == 'POST':

        data = {nameNoId: request.form[nameNoId] for nameNoId in namesNoId}

        new_record = CourseModel(**data)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_record.html', namesNoId=namesNoId)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_record(id):

    record = CourseModel.query.get(id)
    
    namesNoId = fieldNamesInTable.namesNoId(database1, table1)

    if not record:
        return "Record not found", 404

    if request.method == 'POST':

        
        keyValues = request.form
        update_stmt = update(CourseModel).where (CourseModel.id == id)
        for key, value in keyValues.items():
        
            if hasattr(CourseModel, key):
                update_stmt = update_stmt.values(**{key: value})
        
        result = db.session.execute(update_stmt)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to index page or another suitable location

    return render_template('update_record.html', record=record, namesNoId=namesNoId)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_record(id):
    record = CourseModel.query.get(id)
    namesNoId = fieldNamesInTable.namesNoId('your_database.db', table1)

    if not record:
        return "Record not found", 404

    if request.method == 'POST':

        db.session.delete(record)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to index page or another suitable location

    return render_template('delete_record.html', record=record, namesNoId=namesNoId)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
