import json

def main():
    with open(".prog_data.json") as f:
        data = json.load(f)
        theta0 = data["theta0"]
        theta1 = data["theta1"]
    if(theta0 == 0 and theta1 == 0):
        return(0) 
    while True:
        u_input = input("Mileage> ")
        try:
            mileage = int(u_input)
            if(mileage >= 0):
                break
            else:
                print("Error, a car with a negative mileage? Really?")
        except ValueError:
            print("Error, please give a correct mileage")

    predict_data = theta0 + (theta1 * int(mileage))
    if(predict_data < 0):
        predict_data = 0
    print(f"{predict_data:.2f}€")

if(__name__ == "__main__"):
    main()