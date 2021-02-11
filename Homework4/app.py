import sys, traceback
from datetime import datetime
from models import Recruiter, Programmer, Candidate, Vacancy, UnableToWorkException


def main_decoration(main_function):
    def try_main():
        try:
            main_function()
        except UnableToWorkException as utwe:
            print(utwe)
            date_time_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            with open('logs.py', 'a') as file:
                file.write("date: {} {}, {}\n".format(date_time_now,
                    exc_type.__name__, repr(traceback.format_tb(exc_traceback))))
    return try_main

@main_decoration
def main():
    recruter_kate = Recruiter('Kate', 'kate@gmail.com', 180, save_email=True)
    programmer_dima = Programmer('Dima', 'dima@gmail.com', 300, save_email=True)
    programmer_sasha = Programmer('Sasha', 'sasha@gmail.com', 300, save_email=True)
    candidate_vasya = Candidate('Vasya', 'vasya@gmail.com', 'Python')
    candidate_tanya = Candidate('Tanya', 'tanya@gmail.com', 'Python')
    candidate_ruslan = Candidate('Ruslan', 'ruslan@gmail.com', 'Front end')
    vacancy_python = Vacancy('Python')
    vacancy_front_end = Vacancy('Front end')

    candidate_tanya.work()


if __name__ == '__main__':
    main()