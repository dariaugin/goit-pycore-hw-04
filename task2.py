def get_cats_info(path):
    """Returns a list of dicts with the keys (id,name,age) for each cat.

    Each line of the file has the format (id,name,age). Empty lines are skipped.
    Returns an empty list if the file is missing, has invalid data or is empty.
    """
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                # in case of an empty line
                if not line:
                    continue
                # to make sure only 3 fields are present
                cat_id, name, age = line.split(",")
                # to make sure fields are not empty 
                if not (cat_id and name and age.isdigit()):
                    raise ValueError("invalid line")
        
                cats.append({"id": cat_id, "name": name, "age": age})

    except FileNotFoundError:
            print(f"File not found: {path}")
            return []
    except ValueError:
        print(f"File {path} has invalid data")
        return []
    
    if len(cats) == 0:
            print(f"File {path} has no data")
    return cats
if __name__ == "__main__":
    file_path = "cats.txt"
    cats = get_cats_info(file_path)
    if cats:
        print(cats)