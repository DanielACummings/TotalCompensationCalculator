import json, os

class Employee():
    def __init__(self, name):
        self.name = name
    regular = 0
    overtime = 0
    doubletime = 0
    wage_total = 0
    benefits_total = 0
    workweek_total_hours = 0


# def calc_job_length():

# def display_results():
# TODO: Output to a .jsonc file

def process_punch(job_data, punch, active_employee):
    pass

# Get directory that the script is running from (not always the CWD)
scriptDir = os.path.realpath(os.path.dirname(__file__))

# Load JSON data as objects
# TODO: load data from a .jsonc file
f = open(f'{scriptDir}\PunchLogicData.json')
data = json.load(f)
employee_data = data['employeeData']
job_data = data['jobMeta']

# Process employee data
employees = []
for employee_obj in employee_data:
    # Loop through single employee's data
    for key, value in employee_obj.items():
        if key == 'employee':
            employee_name = value
            active_employee = Employee(employee_name)
        elif key == 'timePunch':
            for punch in employee_obj[key]:
                # test
                print(punch)
                print()
                # 
                process_punch(job_data, punch, active_employee)
# TODO: else handle bad data
# TODO: Handle when employee name already exists in employees
    employees.append(active_employee)


f.close()

# test
for employee in employees:
    print(employee.name)
print()
input('test complete')
# 
