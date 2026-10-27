from lab_pgm6 import employee_details

def test_employee_datails():
    result =employee_details("Rahul","EMP101","IT",50000)

    expected = "Name:Rahul\nEmployee ID:EMP101\nDepartment:IT\nSalary:50000"

    asert result ==expected