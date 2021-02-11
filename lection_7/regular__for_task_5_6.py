import re

hours_re = re.compile('^.(\d+).*$')


def extract_hours2(activity):
    if match := hours_re.match(activity):
        return int(match.group(1))
    else:
        return 0


courses = {}
with open("regular_file.txt", "r", encoding="utf8") as fp:
    for line in fp:
        course_name, activities = line.split(':', maxsplit=1)
        course_hours = 0
        for activity in activities.split():
            course_hours += extract_hours2(activity)
        courses[course_name] = course_hours

for course_name, course_hours in courses.items():
    print(f'{course_name}: {course_hours}')
