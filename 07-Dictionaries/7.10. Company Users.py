command = input()
companies = {}
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)
    command = input()
for company_name, employee_id in companies.items():
    print(company_name)
    for i in range(0, len(employee_id)):
        print(f'-- {employee_id[i]}')
