def time_adding_machine():
    print("Enter current hour:")
    current_hour = int(input())
    print("Enter current minute:")
    current_minute = int(input())
    print("Enter current second:")
    current_second = int(input())
    print("Enter hour to go forward:")
    forward_hour = int(input())
    print("Enter minute to go forward:")
    forward_minute = int(input())
    print("Enter second to go forward:")
    forward_second = int(input())

    answer_hour = 0
    answer_minute = 0
    answer_second = 0
    carry_second = 0
    carry_minute = 0
    day = 1
    time_half = 'AM'

    answer_second = current_second + forward_second
    if answer_second >= 60:
        answer_second -= 60
        carry_second = 1

    answer_minute = current_minute + forward_minute + carry_second
    if answer_minute >= 60:
        answer_minute -= 60
        carry_minute = 1

    answer_hour = current_hour + forward_hour + carry_minute
    if answer_hour >= 24:
        answer_hour -= 24
        day += 1

    elif answer_hour == 12:
        time_half = "PM"
        
    elif answer_hour > 12:
        answer_hour -= 12
        time_half = 'PM'

    if day == 1:
        day_name = 'Monday'
    elif day == 2:
        day_name = 'Tuesday'
    elif day == 3:
        day_name = 'Wednesday'
    elif day == 4:
        day_name = 'Thursday'
    elif day == 5:
        day_name = 'Friday'
    elif day == 6:
        day_name = 'Saturday'
    elif day == 7:
        day_name = 'Sunday'
    else:
        day_name = day
    

    if day > 1:
        print(f"The answer is {answer_hour:02d}:{answer_minute:02d}:{answer_second:02d}:{time_half} on {day_name} day {day}")
    else:
        print(f"The answer is {answer_hour:02d}:{answer_minute:02d}:{answer_second:02d}:{time_half}on {day_name}")

# Call the function to run the time adding machine
time_adding_machine()