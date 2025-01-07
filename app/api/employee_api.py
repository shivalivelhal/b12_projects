from app.providers.employee_provider import EmployeeProvider
from flask import jsonify, Blueprint, request

employee_bp = Blueprint("employee_api", __name__)


# in dao and provider that was method now we are making function here
@employee_bp.route("/")  #by default method is get so no need to write # already define in app __init__ for url so here only "/""
def get_all_employees():
    data = EmployeeProvider.get_all_employees_p()
    return jsonify(data), 200


# http://127.0.0.1:5000/api/employees


# so we don't have created table and in that data also not there for that few commands




@employee_bp.route("/", methods=["POST"])
def create_employee():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name is required!"}), 400
    emp_object = EmployeeProvider.create_employee_p(data)
    return jsonify(emp_object.to_dict()), 201

.
# @employee_bp.route("/<int:empid>/", methods=["GET"])
# def get_eployee_by_id(empid):
#     emp = EmployeeProvider.get_employee_by_id_p(empid)
#     if not emp:
#         return jsonify({"error": f"Employee with {empid} not found"}), 404
#     return jsonify(emp), 200


# @employee_bp.route("/<int:empid>/", methods=["PATCH"])
# def update_employee(empid):
#     data = request.json
#     emp = EmployeeProvider.update_employee_p(empid, data)
#     if not emp:
#         return jsonify({"error": f"Employee with {empid} not found"}), 404
#     return jsonify(emp), 200


# # delete == status code, 204
# # jsonify({"message": "de"}), 204

# # chatgpt command:
# # define one more endpoint to fetch the employees data in csv file.. it should return a csv consisting all the employee records from database.. api should be /api/employees/download-csv
# # use provider, dao layer as above answer

# @employee_bp.route("/download-csv", methods=["GET"])
# def update_employee(empid):
#     pass