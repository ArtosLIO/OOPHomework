from models import Recruiter, Programmer, Candidate, Vacancy


def main():
	recruter_kate = Recruiter('Kate', 'kate@gmail.com', 180)
	programmer_dima = Programmer('Dima', 'dima@gmail.com', 300)
	programmer_sasha = Programmer('Sasha', 'sasha@gmail.com', 300)
	candidate_vasya = Candidate('Vasya', 'vasya@gmail.com', 'Python')
	candidate_tanya = Candidate('Tanya', 'tanya@gmail.com', 'Python')
	candidate_ruslan = Candidate('Ruslan', 'ruslan@gmail.com', 'Front end')
	vacancy_python = Vacancy('Python')
	vacancy_front_end = Vacancy('Front end')