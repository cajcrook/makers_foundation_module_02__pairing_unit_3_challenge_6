from datetime import datetime

def age_checker(date_of_birth):
    format = "%Y-%m-%d"
    try:
        datetime.strptime(date_of_birth, format)
    except ValueError:
        raise Exception("Age format is incorrect")
    user_age = datetime.strptime(date_of_birth, format)
    # print (user_age)
    # print (type(user_age))
    today = datetime.today()
    # print (today)
    difference = today - user_age
    # print (difference)
    if int(difference.days) >= 365 * 16:
        return 'Access Granted'
    else:
        return (f'Access Denied, current age: {int(difference.days / 365)}, you need to be 16')   