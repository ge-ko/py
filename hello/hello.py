students = (
    {"name": "John", "age": 23, "courses": None},
    dict(name="James", age=50, courses=["Maths", "Java", "Databases"])
)

for s in students:
    p = f"Student {s['name']} is {s['age']} years old and "
    if s['courses'] is not None:
        p += "studies "
        p += ", ".join(s['courses'][:-1])
        p += f" and {s['courses'][-1]}"
    else:
        p += "does not study yet"
    print(p)
