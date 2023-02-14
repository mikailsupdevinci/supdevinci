from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
    {
        'id': 1,
        'name': 'John Doe',
        'position': 'Manager',
        'salary': 50000
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'position': 'Engineer',
        'salary': 60000
    },
    {
        'id': 3,
        'name': 'Bob Johnson',
        'position': 'Technician',
        'salary': 40000
    }
]

@app.route('/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'GET':
        return jsonify({'employees': employees})

    if request.method == 'POST':
        employee = {
            'id': employees[-1]['id'] + 1,
            'name': request.json['name'],
            'position': request.json['position'],
            'salary': request.json['salary']
        }
        employees.append(employee)
        return jsonify({'employee': employee}), 201

@app.route('/employees/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_employee(employee_id):
    employee = [employee for employee in employees if employee['id'] == employee_id]
    if len(employee) == 0:
        return jsonify({'error': 'Employee not found'})

    if request.method == 'GET':
        return jsonify({'employee': employee[0]})

    if request.method == 'PUT':
        employee[0]['name'] = request.json.get('name', employee[0]['name'])
        employee[0]['position'] = request.json.get('position', employee[0]['position'])
        employee[0]['salary'] = request.json.get('salary', employee[0]['salary'])
        return jsonify({'employee': employee[0]})

    if request.method == 'DELETE':
        employees.remove(employee[0])
        return jsonify({'result': 'Employee deleted'})

if __name__ == '__main__':
    app.run(debug=True)
