def main():
    mealtime = input("What time is it? ")
    converted = convert(mealtime)
    if converted >= 7 and converted <= 8:
        print("breakfast time")
    elif converted >= 12 and converted <= 13:
        print("lunch time")
    elif converted >= 18 and converted <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    time = float(hours) + minutes
    return time



if __name__ == "__main__":
    main()
