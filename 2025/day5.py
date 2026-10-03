example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def combine_ranges(r1, r2):
    start1, end1 = r1
    start2, end2 = r2

    return (min(start1, start2), max(end1, end2))

def check_overlap(r1, r2):
    start1, end1 = r1
    start2, end2 = r2
    return start1 <= end2 and start2 <= end1

def is_fresh(item, db):
    for start, end in db:
        if start <= item <= end:
            return True

    return False

def simplify_db(db):
    current_db = db
    while True:
        
        new_db = []
        skip_next = False
        for i in range(0, len(current_db)):
            if skip_next:
                skip_next = False
                continue

            current = current_db[i]
            if (i + 1) >= len(current_db):
                new_db.append(current)
                continue

            next = current_db[i + 1]
            if check_overlap(current, next):
                skip_next = True
                new_db.append(combine_ranges(current, next))
            else:
                new_db.append(current)

        if len(current_db) == len(new_db):
            break
        
        current_db = new_db
    return current_db

def main():
    with open('../inputs/2025/day5.txt') as f:
        db = []

        db_flag = True
        count = 0
        for line in f.readlines():
        # for line in example.split():
            if '-' not in line and db_flag:
                db_flag = False
                db.sort(key = lambda x: x[0])
                break
            elif db_flag:
                start, end = line.strip().split('-')
                db.append((int(start), int(end)))
            # else:
            #     item = int(line.strip())

            #     if is_fresh(item, db):
            #         count +=1
        
        db = simplify_db(db)
        for start, end in db:
            count += ((end - start) + 1)

        print(count)
if __name__ == '__main__':
    main()
