import json

def main():
    with open(".prog_data.json") as f:
        data = json.load(f)
        theta0 = data["theta0"]
        theta1 = data["theta1"]
    if(theta0 == 0 and theta1 == 0):
        return(0) 
    mileage = input("Mileage> ")
    # Gestion d'erreur manquante # 
    predict_data = theta0 + (theta1 * int(mileage))
    print(f"{predict_data:.2f}€")

if(__name__ == "__main__"):
    main()