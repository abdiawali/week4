import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        #creating list of phones
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        testPhone3 = Phone(2, 'Apple', 'iPhone 5')
        #adding phones 
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        #testing if there is error when add phone that's already in the list
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone3)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        #create employees
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bill')

        test_employees = [employee1, employee2]
        #add employee 
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_employee(employee2)
        #test if the employee that add are same as employee in the employee list
        self.assertCountEqual(test_employees, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(1, 'Bill')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        # test for error if two employees with same id are added
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(employee2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments

        testAssignmentMgr = PhoneAssignments()
        
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr.add_phone(testPhone1)
        
        employee1 = Employee(1, 'Alice')
        #add employee1 to employees
        testAssignmentMgr.add_employee(employee1)
        #assign phone to the employee1
        testAssignmentMgr.assign(testPhone1.id, employee1)
        #test if true phone if assigned to an employee
        self.assertTrue(testPhone1.employee_id == employee1.id)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.
        testAssignmentMgr = PhoneAssignments()
        #create phone
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        #add phone to the phones
        testAssignmentMgr.add_phone(testPhone1)
        #create employees
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bill')
        #add employee1 and 2 to the employees
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_employee(employee2)
        #assign employee1 with the phone1
        testAssignmentMgr.assign(testPhone1.id, employee1)
        #test for error when employee2 is assigned with taken phone
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, employee2)



    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        testAssignmentMgr = PhoneAssignments()
        #create phones
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        #add the new phones to the phone list
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        #create employee
        employee1 = Employee(1, 'Alice')
        #add the new employee to the employee list
        testAssignmentMgr.add_employee(employee1)
        #assign phone1 to employee1
        testAssignmentMgr.assign(testPhone1.id, employee1)
        #test for error when assigned employee1 with another phone
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, employee1)



    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        testAssignmentMgr = PhoneAssignments()
        #create new phones
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 6')
        #add new phones to the phone list
        testAssignmentMgr.add_phone(testPhone1)
        #create new employee
        employee1 = Employee(1, 'Alice')
        #add new employee to the employee list
        testAssignmentMgr.add_employee(employee1)
        #assign employee1 with phone1
        testAssignmentMgr.assign(testPhone1.id, employee1)
        #test it's none when assigned same phone to the same employee
        self.assertIsNone(testAssignmentMgr.assign(testPhone2.id, employee1))


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        testAssignmentMgr = PhoneAssignments()
        #create new phones
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        #add new phones to the phone list
        testAssignmentMgr.add_phone(testPhone1)
        #create new employee
        employee1 = Employee(1, 'Alice')
        #add new employee to the employee list
        testAssignmentMgr.add_employee(employee1)
        #assign employee1 with phone1
        testAssignmentMgr.assign(testPhone1.id, employee1)
        testAssignmentMgr.un_assign(testPhone1.id)

        #test it's none after unassign employee by checking phone's employee 
        self.assertIsNone(testPhone1.employee_id)


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
        
        testAssignmentMgr = PhoneAssignments()
        #create new phones
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        #add new phones to the phone list
        testAssignmentMgr.add_phone(testPhone1)
        #create new employee
        employee1 = Employee(1, 'Alice')
        #add new employee to the employee list
        testAssignmentMgr.add_employee(employee1)
        #assign employee1 with phone1
        testAssignmentMgr.assign(testPhone1.id, employee1)
        #phone_info returns the list of phone and employee_id
        employee_assigned=testAssignmentMgr.phone_info(employee1)
        #test employee id on the phone info is same as employee assigned
        self.assertEqual(testPhone1.employee_id, employee_assigned.employee_id)
        

if __name__=='__main__':
    unittest.main()
