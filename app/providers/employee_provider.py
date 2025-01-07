from app.dao.employee_dao import EmployeeDAO


class EmployeeProvider:
    @staticmethod
    def get_all_employees_p():
        return [
            emp.to_dict() for emp in EmployeeDAO.get_all_employees()
        ]  # list compression
# get_all_employees()method which is from dao layer calling in provider
# now this provider method calling in API





    @staticmethod
    def create_employee_p(input_data):
        return EmployeeDAO.create_employee(
            input_data["name"],
            input_data["role"],
            input_data["salary"],
            input_data["address"],
        )

    # @staticmethod
    # def get_employee_by_id_p(emp_id):
    #     emp = EmployeeDAO.get_employee_by_id(emp_id)
    #     return emp.to_dict() if emp else None

    # @staticmethod
    # def update_employee_p(emp_id, input_data):
    #     emp = EmployeeDAO.update_employee(
    #         emp_id,
    #         nm=input_data.get("name"),
    #         role=input_data.get("role"),
    #         sal=input_data.get("salary"),
    #         addr=input_data.get("address"),
    #     )
    #     return emp.to_dict() if emp else None