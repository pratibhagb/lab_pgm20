def calculate_gross_salary(basic_salary):
  hra = 0.20 * basic_salary  # 20% HRA
  da = 0.10 * basic_salary  # 10% DA
  gross_salary = basic_salary + hra + da
  return hra, da, gross_salary


if _name_ == "_main_":
  basic = 50000
  hra, da, gross = calculate_gross_salary(basic)

  print(f"Basic Salary : {basic}")
  print(f"HRA (20%)    : {hra}")
  print(f"DA (10%)     : {da}")
  print(f"Gross Salary : {gross}")