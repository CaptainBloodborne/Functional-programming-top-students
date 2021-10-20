from typing import List


def get_top(data: List[dict]) -> dict:
    """Returns top student name by course

    Parameters
    ----------
    data: List[dict]
        List of dictionaries with students names, attended courses and
        their marks.

    Returns
        ---------
        dict
            Dictionary with keys as course name and value as
            name of top student.

    Examples
    --------
    students = [
        {'name': 'Alexey',  'rate': 5, 'course': 'Python'},
        {'name': 'Andrey',  'rate': 3, 'course': 'Java'},
        {'name': 'Oleg',  'rate': 4, 'course': 'Python'},
        {'name': 'Julia',  'rate': 3, 'course': 'Java'},
        {'name': 'Elena',  'rate': 4, 'course': 'Python'},
        {'name': 'Igor',  'rate': 4, 'course': 'Java'}
    ]
    print(get_top(students))
    {'Java': 'Igor', 'Python': 'Alexey'}
    """
    course = set(map(lambda x: x['course'], data))
    course_list = map(lambda x: filter(lambda y: y['course'] == x, data), course)

    from operator import itemgetter

    itemgetter_func = itemgetter('course', 'name')
    filter_value = map(
        lambda course_name: itemgetter_func(max(course_name, key=lambda x: x['rate'])),
        course_list
    )
    return dict(list(filter_value))
