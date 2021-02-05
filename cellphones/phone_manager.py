# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # TODO raise exception if two employees with same ID are added
        for each_employee in self.employees:
            if each_employee.id == employee.id:
                raise PhoneError("employee with similiar Id is in the list")
        self.employees.append(employee)


    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        #for phone in self.phones:
        for each_phone in self.phones:
            if each_phone.id == phone.id: #and each_phone.make==phone.make and each_phone.model==phone.model:
                raise PhoneError("phone Id already in list")
        self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.
        for each_phone in self.phones:
            if each_phone.employee_id == employee.id:
                if each_phone.id != phone_id:
                    raise PhoneError("employee has phone")
                else:
                    return
            if each_phone.id==phone_id:
                if each_phone.employee_id == employee.id:
                    return
                elif each_phone.employee_id is None:
                    each_phone.employee_id = employee.id
                    return
                else:
                    raise PhoneError("phone already assigned")


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for each_phone in self.phones:
            if each_phone.id == phone_id:
                each_phone.employee_id = None   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO  should return None if the employee does not have a phone
        # TODO  the method should raise an exception if the employee does not exist
        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone
        for emp in self.employees:
            if emp.id == employee.id:
                return None
        raise  PhoneError("Employee not found") 
class PhoneError(Exception):
    pass
