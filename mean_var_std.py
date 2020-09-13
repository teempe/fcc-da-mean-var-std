import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3, 3)

    calculations = {"mean": [], "variance": [], "standard deviation": [], "max": [], "min": [], "sum": []}

    for ax in (0, 1, None):
        calculations["mean"].append(np.mean(arr, ax).tolist())
        calculations["variance"].append(np.var(arr, ax).tolist())
        calculations["standard deviation"].append(np.std(arr, ax).tolist())
        calculations["max"].append(np.max(arr, ax).tolist())
        calculations["min"].append(np.min(arr, ax).tolist())
        calculations["sum"].append(np.sum(arr, ax).tolist())

    return calculations