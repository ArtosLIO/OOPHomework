class Employee(object):
    def __init__(self, name, email, salary, save_email=False):
        self.name = name
        self.email = email
        self.salary_for_day = salary
        if save_email:
            self._save_email()

    def _save_email(self):
        try:
            with open('email.txt') as f:
                email_in_bd = f.read().split('\n')
                for email in email_in_bd:
                    if email == self.email:
                        raise ValueError
        except ValueError:
            print("This email has been registered!")
        else:
            with open('email.txt', 'a') as f:
                f.write(self.email + '\n')

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


class Candidate(object):
    main_skill = ''
    main_skill_grade = ''

    def __init__(self, full_name, email, technologies):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies

    def work(self):
        raise UnableToWorkException("I'm not hired yet, lol.")


class Vacancy(object):
    main_skill = ''
    main_skill_level = ''

    def __init__(self, title='Python'):
        self.title = title


class UnableToWorkException(Exception):
    pass