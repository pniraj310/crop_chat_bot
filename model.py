# model.py

def predict_yield(crop, temperature, rainfall):
    # Simple dummy logic for now
    if crop.lower() == "paddy":
        return round((rainfall * 0.1 + temperature * 0.2) / 2, 2)
    elif crop.lower() == "wheat":
        return round((rainfall * 0.08 + temperature * 0.15) / 2, 2)
    else:
        return round((rainfall * 0.05 + temperature * 0.1) / 2, 2)
