day = 5
match day:
    case 1 :
        print("Monday")
    case 2 :
        print("Tuesday")
    case 3 :
        print("Wednesday")
    case 4 :
        print("Thursday")
    case 5 :
        print("Friday")
    case 6 :
        print("Saturday")
    case 7 :
        print("Sunday")
    case _ :
        print("Invalid day")
# Output: Friday    
day = 3
match day:
    case 1 | 3 | 5 | 7 :
        print("Odd day")
    case 2 | 4 | 6 :
        print("Even day")
    case _ :
        print("Invalid day")
# Output: Odd day                
                

    