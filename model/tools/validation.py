import re




def code_validation(code):
    if not  re.match(r"^[a-zA_Z\s]{3,30}$",code):
        raise ValueError("Invalid code !!!")


def name_validation(name):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name !!!")

def family_validation(family):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",family):
        raise ValueError("Invalid family !!!")

def birth_date_validation(birth_date):
    if not  re.match(r"^\d{4}-\d{2}-\d{2}$",birth_date):
        raise ValueError("Invalid birth date !!!")


def username_validation(username):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",username):
        raise ValueError("Invalid username !!!")


def password_validation(password):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",password):
        raise ValueError("Invalid password !!!")


def role_validation(role):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",role):
        raise ValueError("Invalid role !!!")


def locked_validation(locked):
    if not re.match(r"^[a-zA-Z\s]{3,30}$",locked):
        raise ValueError("Invalid locked !!!")


def origin_validation(origin):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$", origin):
        raise ValueError("Invalid origin !!!")


def destination_validation(destination):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",destination):
        raise ValueError("Invalid destination !!!")


def start_date_time_validation(start_date_time):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",start_date_time):
        raise ValueError("Invalid start_date_time !!!")



def end_date_time_validation(end_date_time):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",end_date_time):
        raise ValueError("Invalid end_date_time !!!")



def ticket_type_validation(ticket_type):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$", ticket_type):
        raise ValueError("Invalid ticket_type !!!")


def seat_number_validation(seat_number):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$",seat_number):
        raise ValueError("Invalid seat_number !!!")



def price_validation(price):
    if not  re.match(r"^[a-zA-Z\s]{3,30}$", price):
        raise ValueError("Invalid price !!!")



def phone_number(phone_number):
    if not re.match(r"^\+?1?\d{9,15}$", phone_number):
        raise ValueError("Invalid phone_number !!!")
