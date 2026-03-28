

import pandas as pd


### FUNCTION: Calculate Risk

def calculate_risk(row):
    score = 0
    reasons = []

    if row['failed_login'] >= 5:
        score += 2
        reasons.append("Multiple failed login attempts")

    if str(row['time']).lower() == "midnight":
        score += 1
        reasons.append("Login at unusual time")

    if str(row['ip']).lower() == "unknown":
        score += 1
        reasons.append("Unknown IP address")

    if str(row['location']).lower() != "india":
        score += 2
        reasons.append("Login from foreign location")

    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk, reasons


### MAIN PROGRAM

def main():
    print("-" * 40)
    print("CYBER THREAT ADVISORY SYSTEM")
    print("-" * 40)

    file_name = input("Enter CSV file name: ")

    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        print(" File not found.")
        return

    username = input("Enter username to analyze: ")

    user_data = df[df['username'] == username]

    if user_data.empty:
        print(" No data found for this user.")
        return

    print(f"\n Analyzing activity for: {username}")
    print("-" * 40)

    high_count = 0
    medium_count = 0
    abnormal_found = False

   
    ### Analyze each record
  
    for _, row in user_data.iterrows():
        risk, reasons = calculate_risk(row)

        if risk != "LOW":
            abnormal_found = True

            print("\n Suspicious Activity Detected:")
            print(f"- Time: {row['time']}")
            print(f"- IP: {row['ip']}")
            print(f"- Location: {row['location']}")
            print(f"- Risk Level: {risk}")

            print("- Reasons:")
            for r in reasons:
                print(f"  • {r}")

            # Count risks
            if risk == "HIGH":
                high_count += 1
            elif risk == "MEDIUM":
                medium_count += 1



     ###Final Summary
  
    print("\n Final Assessment:")
    
    if not abnormal_found:
        print(" No suspicious activity detected. User behavior is normal.")
    elif high_count > 0:
        print(" HIGH RISK: Immediate action required!")
    elif medium_count > 0:
        print(" MEDIUM RISK: Monitor user activity closely.")

    
    ### Burst Activity Check
  
    if user_data['failed_login'].sum() > 10:
        print("\n ALERT: Multiple failed login attempts detected!")


    ### Recommendations
  
    print("\n Security Recommendations:")

    if high_count > 0:
        print("- Reset password immediately")
        print("- Enable Two-Factor Authentication (2FA)")
        print("- Block suspicious IP addresses")

    elif medium_count > 0:
        print("- Monitor account activity")
        print("- Enable 2FA for better security")

    else:
        print("- No immediate action required")


###Run program
if __name__ == "__main__":
    main()