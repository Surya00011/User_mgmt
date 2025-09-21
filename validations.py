def validate_user_form(name, age, contact, city):
    errors = {}

    name = name.strip()
    age = age.strip()
    contact = contact.strip()
    city = city.strip()

    # Name
    if not name:
        errors['name'] = "Name is required!"
    elif name.isdigit():
        errors['name'] = "Name cannot be a number!"

    # Age
    if not age:
        errors['age'] = "Age is required!"
    elif not age.isdigit():
        errors['age'] = "Age must be a number!"

    # Contact
    if not contact:
        errors['contact'] = "Contact is required!"
    elif not contact.isdigit():
        errors['contact'] = "Contact must be numeric!"

    # City
    if not city:
        errors['city'] = "City is required!"
    elif city.isdigit():
        errors['city'] = "City cannot be a number!"

    return (len(errors) == 0), errors
