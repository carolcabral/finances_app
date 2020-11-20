from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
db = SQLAlchemy(app)

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4), nullable=False)
    month = db.Column(db.String(2), nullable=False) 
    date = db.Column(db.String(2), nullable=False)

    content = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Float, default=0)
    #isFixed = db.Column(db.Boolean, default = False)



@app.route("/", methods=['POST', 'GET'])
def index():
    expenses = Expenses.query.order_by(Expenses.id).all() # TODO: ORDER BY DATE
    return render_template('index.html', expenses=expenses)


@app.route("/expense", methods=['POST', 'GET'])
def add_expense():
    if request.method == 'POST':
        year, month, date = request.form['date'].split('-')
        expense_content = request.form['content']
        expense_value = request.form['value']
        #expense_isFixed = request.form['isFixed'] 

        new_expense = Expenses(year=year, month=month, date=date, content=expense_content, value=expense_value)# isFixed=expense_isFixed)

        try:
            db.session.add(new_expense)
            db.session.commit()
            return redirect('/')
        
        except:
            return render_template('error.html', error="There was an issue adding your task")
    else: 
        return render_template('add_expense.html')

@app.route("/delete/<int:id>")
def delete(id):
	expense_to_delete = Expenses.query.get_or_404(id)

	try:
		db.session.delete(expense_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return render_template('error.html', error='There was a problem deleting that task')

@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    expense = Expenses.query.get_or_404(id)
    
    if request.method == 'POST':
        expense.year, expense.month, expense.date = request.form['date'].split('-')
        #expense.date = request.form['date']
        expense.content = request.form['content']      
        expense.value = request.form['value']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return render_template('error.html', error='There was an issue updating your tasks')
    
    else:
        return render_template('update.html', expense=expense)

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)