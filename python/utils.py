

def print_subints(subints):
    if len(subints) <= 0:
        print("No subinterfaces.")
    for subint in subints:
        name = subint["name"]
        id = subint["subIntfId"]
        print(f"{name}.{id}")
        