# my solution
def rental_car_cost(d):
    if d >= 7:
        return d * 40 - 50
    elif 3 <= d < 7:
        return d * 40 - 20
    else:
        return d * 40

# best solution
