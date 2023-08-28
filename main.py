from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
import pyjokes


def date_today():
    today = date.today()
    print(today)


def get_joke():
    joke = pyjokes.get_joke(language='en', category='all')
    return print(joke)


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    get_joke()
    date_today()
