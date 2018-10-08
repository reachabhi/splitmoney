from flask import Flask, jsonify, make_response, abort, request
import json

app = Flask(__name__)
expenses = [{"spentBy":"Abhishek","spentFor":"Toll","moneySpent":100,"contributors":["Abhishek","Tushar","Pranav"]},{"spentBy":"Tushar","spentFor":"Booze","moneySpent":2000,"contributors":["Abhishek","Pranav"]},{"spentBy":"Pranav","spentFor":"Food","moneySpent":1000,"contributors":["Abhishek","Pranav"]}]


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/expenses/all',methods=['GET','POST'])
def expense_details():
    if(request.method=='POST'):
        print(request.get_json())
        expenses.append(request.get_json())
        return jsonify(expenses)
    else:
        return jsonify(expenses)


@app.route('/expenses/<name>',methods=['GET'])
def per_expense(name):
    per_expense = []
    match = [i for i in expenses if(i['spentBy']==name)]
    per_expense.append(match)
    if len(per_expense)==0:
        abort(404)
    else:
        return jsonify(per_expense)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    app.run(debug=True)