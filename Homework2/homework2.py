class Employee(object):
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary_for_day = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, working_days):
        return "Salary for {} working_days: {}".format(working_days, working_days * self.salary_for_day)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Programmer(Employee):
    def work(self):
        run_work = super().work()[:-1] + " and start to coding."
        return run_work


class Recruiter(Employee):
    def work(self):
        run_work = super().work()[:-1] + " and start to hiring."
        return run_work


prog = Programmer('Dima', 'dima@gmail.com', 300)
print(prog.work())
print(prog.check_salary(21))
print(prog, end='\n\n')

recrut = Recruiter('Kate', 'kate@gmail.com', 180)
print(recrut.work())
print(recrut.check_salary(15))
print(recrut)
