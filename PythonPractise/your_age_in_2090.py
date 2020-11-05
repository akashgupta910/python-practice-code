print("\n<------ Your Age in 2090 ------->\n")

while True:
    age = int(input("Enter your Age: "))
    
    if age <= 0:
        print("You are not born yet!\n")

    elif age > 200:
        print("I have no words to say :-)\n")

    elif age > 100:
        print("You seem to be oldest person alive\n")

    else:
        _100 = (2019 - age) + 100
        print(f"You will turn 100 years old in {_100}\n")
        
        yes_no_inp = input("----> Do you want to know your age in any particular year. Y/N: ")

        if yes_no_inp == "y" or yes_no_inp == "Y":
            year = int(input("Enter Year: ")) 

            if year < 2019 or year > 2090:
                print("Year must be between 2019 to 2090")
                _year = int(input("Enter Year: "))
                if _year < 2019 or _year > 2090:
                    print("Value Error!")
                    break
                else:
                    __age = (_year - 2019) + age
                    print(f"You become {__age} years old in year {_year}.")
                    break
            else:
                _age = (year - 2019) + age
                print(f"You become {_age} years old in year {year}.")
                break
        
        else:
            break
        