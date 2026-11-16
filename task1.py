def total_salary(path):
    """Returns a tuple (total, average) of the salaries listed in the file.

    Each line has the format (Surname Name,salary). Empty lines are skipped.
    Returns (None, None) if the file is missing, has invalid data or is empty.
    """
    salaries = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                # in case of an empty line
                if not line:
                    continue
                # to make sure only 2 fields are present
                name, salary = line.split(",")
                # name must not be empty, salary must be a number 
                if not (name and salary.isdigit()):
                    raise ValueError
                salaries.append(int(salary))
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None, None
    except ValueError:
        print(f"File {path} has invalid data")
        return None, None

    if len(salaries) == 0:
        print(f"File {path} has no data")
        return None, None

    total = sum(salaries)
    return total, total / len(salaries)

if __name__ == "__main__":
    file_path = "salaries.txt"
    total, average = total_salary(file_path)
    if total is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    
    
