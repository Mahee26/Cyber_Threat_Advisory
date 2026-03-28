

## Objectives
- Analyze user login activity  
- Detect suspicious patterns  
- Classify risk levels (Low, Medium, High)  
- Provide actionable security recommendations  
- Demonstrate basic cybersecurity concepts  


## Technologies Used
- Python 
- Pandas  



##  Input Format
The system uses a CSV file with the following structure:


username, failed_login, time, ip, location


### Example:

user1,1,morning,known,india
user1,8,midnight,unknown,russia
user2,2,afternoon,known,india



##  How It Works
1. User enters the CSV file name  
2. User selects a username to analyze  
3. The system filters logs for that user  
4. Each record is evaluated using predefined rules  
5. Only suspicious activities are displayed  
6. A final risk assessment and recommendations are generated  



##  Detection Rules
The system flags activity based on:

- Failed login attempts ≥ 5  
- Login at **midnight**  
- IP marked as **unknown**  
- Location outside **India**  

##  Risk Levels
- **LOW** → Normal activity  
- **MEDIUM** → Suspicious activity  
- **HIGH** → High-risk activity (requires immediate action)  


##  Security Recommendations
- Reset password immediately  
- Enable Two-Factor Authentication (2FA)  
- Monitor account activity  
- Block suspicious IP addresses  



##  How to Run
1. Install required library:

pip install pandas


2. Run the program:

python your_file_name.py


3. Enter:
- CSV file name  
- Username to analyze  


##  Features
- Rule-based threat detection  
- Clean and readable output  
- Reports only abnormal activity  
- Beginner-friendly design  
- Real-world cybersecurity concept  


##  Limitations
- Works only on predefined rules  
- Cannot detect unknown patterns automatically  
- Requires structured CSV input  



##  Future Scope
- Machine Learning-based anomaly detection  
- Real-time monitoring system  
- GUI interface  
- Data visualization  


##  Conclusion
This project demonstrates how login data can be analyzed to detect suspicious activities using a simple and effective rule-based approach. It helps in understanding basic cybersecurity practices and threat detection techniques.


## Outputs
<img width="368" height="132" alt="eror-output" src="https://github.com/user-attachments/assets/9c7b249a-c85b-40a7-a867-9d0cdbfe7fa3" />
<img width="562" height="654" alt="Screenshot 2026-03-29 021156" src="https://github.com/user-attachments/assets/2fdd0ead-12e4-4cf6-8511-0ecf05556a92" />
<img width="1318" height="806" alt="Screenshot 2026-03-29 021116" src="https://github.com/user-attachments/assets/593b31b4-a120-4720-9d08-f1e08e2110dc" />




