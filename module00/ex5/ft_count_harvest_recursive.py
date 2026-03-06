def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(day, total):
        if day > total:
            print("Harvest time!")
            return
        print("Day", day)
        count(day + 1, total)

    count(1, days)
