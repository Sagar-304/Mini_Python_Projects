# calander of october month of 2025 to find which day is on which date
date = (input("Enter the date :"))

match date:
    case "1":
        print("It is Wednesday")
    case "2" | "9" | "16" | "23" | "30":
        print("It is Thrusday")
    case "3" | "10" | "17" | "24" | "31":
        print("It is Friday")
    case "4" | "11" | "18" | "25":
        print("It is Saturday")
    case "5" | "12" | "19" | "26":
        print("It is Weekend ", sep="\n")
    case "6" | "13" | "20" | "27":
        print("It is Monday")
    case "7" | "14" | "21" | "28":
        print("It is Tuesday")
    case _:
        print("Please enter valid date")