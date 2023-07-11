def calculate_allocation(num_students):
    num_classes = (num_students + 29) // 30
    students_per_class = num_students // num_classes
    remaining_students = num_students % num_classes

    allocation = {}

    for i in range(1, num_classes + 1):
        if i <= remaining_students:
            allocation[f"Class {i}"] = students_per_class + 1
        else:
            allocation[f"Class {i}"] = students_per_class

    print(f"Proposed Allocation: {num_classes} class{'es' if num_classes > 1 else ''}" )
    print(allocation)

calculate_allocation(87)
calculate_allocation(31)
calculate_allocation(59)
