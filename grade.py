import pandas as pd

csc_class_27 = {"Hod" : "Dr. John Doe",
     "students" : {
        "John Doe": {"MTS101": 85, "CSC101": 67, "CSC102": 92, "PHY101": 78, "CHE101": 81, "BIO101": 74},
        "Israel Daniel": {"MTS101": 73, "CSC101": 88, "CSC102": 69, "PHY101": 91, "CHE101": 85, "BIO101": 76},
        "Moses Bee": {"MTS101": 90, "CSC101": 76, "CSC102": 87, "PHY101": 84, "CHE101": 79, "BIO101": 65},
        "Ade Markinton": {"MTS101": 77, "CSC101": 89, "CSC102": 82, "PHY101": 85, "CHE101": 90, "BIO101": 71},
        "Stela Morio": {"MTS101": 92, "CSC101": 81, "CSC102": 73, "PHY101": 79, "CHE101": 74, "BIO101": 88},
        "Moris Buffalo": {"MTS101": 86, "CSC101": 78, "CSC102": 94, "PHY101": 82, "CHE101": 77, "BIO101": 80},
        "Nathan Bethel": {"MTS101": 69, "CSC101": 92, "CSC102": 75, "PHY101": 88, "CHE101": 83, "BIO101": 79},
        "Okon Tale": {"MTS101": 94, "CSC101": 74, "CSC102": 88, "PHY101": 76, "CHE101": 81, "BIO101": 67},
        "Indio Morinton": {"MTS101": 88, "CSC101": 69, "CSC102": 92, "PHY101": 85, "CHE101": 78, "BIO101": 72},
        "Donald Beckam": {"MTS101": 81, "CSC101": 90, "CSC102": 79, "PHY101": 83, "CHE101": 75, "BIO101": 89},
        "Indifreke Danton": {"MTS101": 74, "CSC101": 82, "CSC102": 91, "PHY101": 78, "CHE101": 86, "BIO101": 68},
        "Rice Midfield": {"MTS101": 79, "CSC101": 95, "CSC102": 81, "PHY101": 77, "CHE101": 80, "BIO101": 84},
        "Isaac Holland": {"MTS101": 93, "CSC101": 76, "CSC102": 74, "PHY101": 86, "CHE101": 89, "BIO101": 71},
        "Mbappe Stone": {"MTS101": 87, "CSC101": 79, "CSC102": 93, "PHY101": 90, "CHE101": 74, "BIO101": 82},
        "Jame Bonday": {"MTS101": 75, "CSC101": 88, "CSC102": 72, "PHY101": 81, "CHE101": 77, "BIO101": 89},
        "Math Mathes": {"MTS101": 91, "CSC101": 84, "CSC102": 77, "PHY101": 79, "CHE101": 92, "BIO101": 68},
        "Birthing Jell": {"MTS101": 80, "CSC101": 65, "CSC102": 85, "PHY101": 92, "CHE101": 79, "BIO101": 75},
        "Brog Doe": {"MTS101": 78, "CSC101": 90, "CSC102": 73, "PHY101": 81, "CHE101": 88, "BIO101": 69},
        "Emmanuel Jackson": {"MTS101": 95, "CSC101": 74, "CSC102": 92, "PHY101": 76, "CHE101": 81, "BIO101": 83},
        "Jan Jane": {"MTS101": 82, "CSC101": 77, "CSC102": 65, "PHY101": 76, "CHE101": 79, "BIO101": 69},
        "Peter Park": {"MTS101": 81, "CSC101": 69, "CSC102": 93, "PHY101": 80, "CHE101": 79, "BIO101": 78},
        "Marry Jane": {"BIO101": 100, "MTS101": 78, "CSC101": 66, "CSC102": 82, "PHY101": 82, "CHE101": 79},
        "John Isrealites": {"MTS101": 77, "CSC101": 79, "CSC102": 80, "PHY101": 81, "CHE101": 79, "BIO101": 64},
        "Amaka Emeka": {"MTS101": 99, "CSC101": 78, "CSC102": 88, "BIO101": 78, "PHY101": 67, "CHE101": 79},
        "Jack Jacky": {"MTS101": 85, "CSC101": 90, "CSC102": 71, "PHY101": 87, "CHE101": 67, "BIO101": 88},
        "Detes Date": {"MTS101": 85, "CSC101": 60, "CSC102": 77, "PHY101": 87, "CHE101": 79, "BIO101": 55},
        "Detes Date": {"MTS101": 85, "CSC101": 60, "CSC102": 77, "PHY101": 87, "CHE101": 79, "BIO101": 55},
        "John Doe": {"MTS101": 82, "CSC101": 65, "CSC102": 79, "PHY101": 85, "CHE101": 80, "BIO101": 57},
        "Alice Carter": {"MTS101": 88, "CSC101": 70, "CSC102": 81, "PHY101": 90, "CHE101": 78, "BIO101": 60},
        "Michael Johnson": {"MTS101": 75, "CSC101": 68, "CSC102": 74, "PHY101": 82, "CHE101": 76, "BIO101": 58},
        "Sophia Williams": {"MTS101": 90, "CSC101": 80, "CSC102": 85, "PHY101": 92, "CHE101": 88, "BIO101": 70},
        "Daniel Brown": {"MTS101": 95, "CSC101": 85, "CSC102": 89, "PHY101": 94, "CHE101": 90, "BIO101": 75},
        "Emma Davis": {"MTS101": 78, "CSC101": 72, "CSC102": 76, "PHY101": 80, "CHE101": 74, "BIO101": 59},
        "Olivia Wilson": {"MTS101": 84, "CSC101": 78, "CSC102": 83, "PHY101": 86, "CHE101": 82, "BIO101": 65},
        "James Martinez": {"MTS101": 91, "CSC101": 87, "CSC102": 88, "PHY101": 93, "CHE101": 89, "BIO101": 72},
        "Liam Thompson": {"MTS101": 70, "CSC101": 60, "CSC102": 65, "PHY101": 72, "CHE101": 68, "BIO101": 50},
        "Emily Anderson": {"MTS101": 77, "CSC101": 69, "CSC102": 72, "PHY101": 79, "CHE101": 75, "BIO101": 58},
        "Benjamin Rodriguez": {"MTS101": 86, "CSC101": 76, "CSC102": 80, "PHY101": 84, "CHE101": 79, "BIO101": 64},
        "Charlotte Moore": {"MTS101": 89, "CSC101": 82, "CSC102": 86, "PHY101": 91, "CHE101": 85, "BIO101": 68},
        "Ethan Lee": {"MTS101": 93, "CSC101": 90, "CSC102": 92, "PHY101": 95, "CHE101": 94, "BIO101": 78},
        "Amelia Taylor": {"MTS101": 79, "CSC101": 71, "CSC102": 75, "PHY101": 81, "CHE101": 73, "BIO101": 57},
        "Harper White": {"MTS101": 85, "CSC101": 79, "CSC102": 82, "PHY101": 88, "CHE101": 80, "BIO101": 66},
        "Henry Clark": {"MTS101": 92, "CSC101": 88, "CSC102": 90, "PHY101": 94, "CHE101": 91, "BIO101": 76},
        "Elizabeth Hall": {"MTS101": 76, "CSC101": 70, "CSC102": 73, "PHY101": 78, "CHE101": 71, "BIO101": 55},
        "Lucas Allen": {"MTS101": 83, "CSC101": 75, "CSC102": 78, "PHY101": 85, "CHE101": 77, "BIO101": 60},
        "Mia Young": {"MTS101": 94, "CSC101": 89, "CSC102": 91, "PHY101": 96, "CHE101": 92, "BIO101": 80},
        "David Scott": {"MTS101": 81, "CSC101": 74, "CSC102": 77, "PHY101": 83, "CHE101": 76, "BIO101": 58},
        "Ella King": {"MTS101": 88, "CSC101": 80, "CSC102": 85, "PHY101": 90, "CHE101": 82, "BIO101": 67},
        "Mason Baker": {"MTS101": 97, "CSC101": 92, "CSC102": 95, "PHY101": 98, "CHE101": 94, "BIO101": 85},
        "Aria Nelson": {"MTS101": 82, "CSC101": 76, "CSC102": 79, "PHY101": 84, "CHE101": 78, "BIO101": 59},
        "Jack Carter": {"MTS101": 87, "CSC101": 81, "CSC102": 83, "PHY101": 88, "CHE101": 84, "BIO101": 66},
        "Hannah Adams": {"MTS101": 90, "CSC101": 85, "CSC102": 88, "PHY101": 91, "CHE101": 89, "BIO101": 71},
        "Lucas Phillips": {"MTS101": 78, "CSC101": 72, "CSC102": 76, "PHY101": 80, "CHE101": 74, "BIO101": 60},
        "Madison Turner": {"MTS101": 85, "CSC101": 79, "CSC102": 82, "PHY101": 88, "CHE101": 80, "BIO101": 67},
        "Leo Evans": {"MTS101": 92, "CSC101": 88, "CSC102": 90, "PHY101": 94, "CHE101": 91, "BIO101": 75},
    
    }
}

print(csc_class_27)
# display data using rows and column
data = pd.DataFrame.from_dict(csc_class_27["students"], orient="index")
# print(data)
# print(data.describe())
#  create an new column to calculate the percentage of all the students
data["Percentage"] = data.mean(axis = 1)


def get_remark(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 80:
        return "Very Good"
    elif avg >= 70:
        return "Good"
    elif avg >= 60:
        return "Fair"
    else:
        return "Needs Improvement"

# Calculate the average score and add the remark column

data["Remark"] = data["Percentage"].apply(get_remark)
print(data)
# Save the data to a CSV file
data.to_csv("csc_class_27.csv", index=True)



