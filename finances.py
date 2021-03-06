from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pandas as pd
import json

from calculate import calculate_balance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
db = SQLAlchemy(app)

#global current_month
current_month = 11
current_year = 2020

global categories


class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4), nullable=False)
    month = db.Column(db.String(2), nullable=False)
    date = db.Column(db.String(2), nullable=False)

    content = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Float, default=0)
    isFixed = db.Column(db.Boolean, default=False)


@app.route("/", methods=['POST', 'GET'])
def index():
    global current_month, current_year

    if request.method == 'POST':
        if request.form['current-month'] == 'next':
            if current_month == 12:
                current_month = 1
                current_year = current_year + 1
            else:
                current_month = current_month + 1
        else:
            if current_month == 1:
                current_month = 12
                current_year = current_year - 1
            else:
                current_month = current_month - 1
    print(current_month)

    expenses = Expenses.query.filter_by(month=str(current_month).zfill(
        2), year=current_year).order_by(Expenses.date).all()
    return render_template('index.html', expenses=expenses)


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
    with open('categories.json', 'r') as f:
        categories = json.loads(f.read())

    if request.method == 'POST':
        expense.year, expense.month, expense.date = request.form['date'].split(
            '-')
        #expense.date = request.form['date']
        expense.content = request.form['content']
        expense.value = request.form['value']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return render_template('error.html', error='There was an issue updating your tasks')

    else:
        return render_template('update.html', expense=expense, categories=categories)


@app.route("/reports", methods=['POST', 'GET'])
def reports():
    report_year = current_year
    report_month = current_month

    if request.method == 'POST':
        report_year, report_month = request.form['report-from'].split('-')
        print(report_year)
        print(report_month)

    expenses = Expenses.query.filter_by(month=str(report_month).zfill(
        2), year=report_year).order_by(Expenses.date).all()
    balance = calculate_balance(expenses)
    return render_template('reports.html', month=report_month, year=report_year, balance=balance)


@app.route("/admin", methods=['POST', 'GET'])
def admin():
    #global categories
    with open('categories.json', 'r') as f:
        categories = json.loads(f.read())

    if request.method == 'POST':
        print("REQUEST FROM ADMIN")
        print(request.form)
        print('CATEGORIES' + str(categories.keys()))
        print('PARENT:' + request.form['parent-tag'])
        if request.form['parent-tag'] in categories.keys():
            if request.form['child-tag'] not in categories[request.form['parent-tag']]:
                categories[request.form['parent-tag']
                           ].append(request.form['child-tag'])
        else:
            categories[request.form['parent-tag']] = []
            categories[request.form['parent-tag']
                       ].append(request.form['child-tag'])

        with open('categories.json', 'w') as f:
            json.dump(categories, f, indent=4)
    return render_template('admin.html', categories=categories)


# @app.route("/expense", methods=['POST', 'GET'])
@app.route("/new-entry", methods=['POST', 'GET'])
def add_expense():
    print(request.form)
    with open('categories.json', 'r') as f:
        categories = json.loads(f.read())

    if request.method == 'POST':
        year, month, date = request.form['date'].split('-')
        expense_content = request.form['content']
        expense_value = request.form['value']
        expense_isFixed = True if 'isFixed' in request.form else False
        new_expense = Expenses(year=year, month=month, date=date,
                               content=expense_content, value=expense_value, isFixed=expense_isFixed)

        try:
            db.session.add(new_expense)
            db.session.commit()
            return redirect('/')

        except:
            return render_template('error.html', error="There was an issue adding your task")
    else:
        return render_template('add_expense.html', categories=categories)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
