#22
grades = [1,3,7,99]
def calculate_average (grades):
    average_grades = sum(grades)/len(grades)
    return average_grades

print(calculate_average(grades))

def add_bonus (grades):
    return [x+5 for x in grades]

print(add_bonus(grades))

def get_result (a):
    for x in grades:
        if a == 100:
            return ('excellent')
        if 80 <= a <= 99:
            return ('very good')
        if 70 <= a <= 79:
            return (' good')
        if 60 <= a <= 69:
            return ('pass')
        else: return ('fall')

print(get_result(56))
