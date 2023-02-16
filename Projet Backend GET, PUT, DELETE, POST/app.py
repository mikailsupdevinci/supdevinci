from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
employees = [
    {
        'id': 1,
        'firstName': 'John',
        'lastName': 'Doe',
        'emailId': 'john.doe@example.com'
    },
    {
    
        'id': 2,
        'firstName': 'Jane',
        'lastName': 'Smith',
        'emailId': 'jane.smith@example.com'
    },
    {
        'id': 3,
        'firstName': 'Bob',
        'lastName': 'Johnson',
        'emailId': 'bob.johnson@example.com'
    }
]

@app.route('/api/v1/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'GET':
        return jsonify(employees)

    if request.method == 'POST':
        employee = {
            'id': employees[-1]['id'] + 1,
            'firstName': request.json['firstName'],
            'lastName': request.json['lastName'],
            'emailId': request.json['emailId']
        }
        employees.append(employee)
        return jsonify({'employee': employee}), 201

@app.route('/api/v1/employees/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_employee(employee_id):
    employee = [employee for employee in employees if employee['id'] == employee_id]
    if len(employee) == 0:
        return jsonify({'error': 'Employee not found'})

    if request.method == 'GET':
        return jsonify({'employee': employee[0]})

    if request.method == 'PUT':
        employee[0]['firstName'] = request.json.get('firstName', employee[0]['firstName'])
        employee[0]['lastName'] = request.json.get('lastName', employee[0]['lastName'])
        employee[0]['emailId'] = request.json.get('emailId', employee[0]['emailId'])
        return jsonify({'employee': employee[0]})

    if request.method == 'DELETE':
        employees.remove(employee[0])
        return jsonify({'result': 'Employee deleted'})

if __name__ == '__main__':
    app.run(port=8080, debug=True)