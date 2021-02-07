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


class Candidate():
    main_skill = ''
    main_skill_grade = ''

    def __init__(self, full_name, email, technologies)
        self.full_name = full_name
        self.email = email
        self.technologies = technologies


class Vacancy():
    main_skill = ''
    main_skill_level = ''

    def __init__(self, title='Python')
        self.title = title