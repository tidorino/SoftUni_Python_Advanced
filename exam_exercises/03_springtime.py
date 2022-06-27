def start_spring(**kwargs):
    spring_objects = {}

    for key, value in kwargs.items():
        if value not in spring_objects:
            spring_objects[value] = []
        spring_objects[value].append(key)

    result = sorted(spring_objects.items(), key=lambda x: (- len(x[1]), x[0]))
    type_result = ''
    for type_fl, object_fl in result:
        type_result += f"{type_fl}:\n"
        sorted_fl = sorted(object_fl)
        for fl in sorted_fl:
            type_result += f"-{fl}\n"

    return type_result.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))



# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",
#                    }
#
#
# print(start_spring(**example_objects))
