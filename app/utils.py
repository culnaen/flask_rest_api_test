def make_id():
    with open("count") as f:
        count = int(f.readline().strip()) + 1
    count = str(count)
    with open("count", "w") as f:
        f.write(count)
    return count
