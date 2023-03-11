# Python Project using Flask and SQL 
(S2R Analytics - QA  DevOps Apprenticeship Level 4.)

![Github issues](https://img.shields.io/badge/DevOps%20Portfolio%20Project-Python-red)

![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)
![Edge](https://img.shields.io/badge/Edge-0078D7?style=for-the-badge&logo=Microsoft-edge&logoColor=white)
![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white).
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

![S2RAnalytics](https://img.shields.io/badge/Project_By-QA-blue)
![QA](https://img.shields.io/badge/Project_For-S2RAnalytics-blue)
![Monitor_Queue](https://img.shields.io/badge/Monitor-Queue-red)

# Aim and Objective of the Project:   

- Develop an application using the Flask framework
- Provide a web interface to the processing logs generated by the ByltInsyte platform
- Project will use Bootstrap for formatting
- Project will access an SQL database
- Show a list of logs with the ability to search for different criteria
- Live view where it shows incomplete jobs

#  🔗[Assessment criteria with evidence](https://gitlab.com/s2ranalytics/prototyping/monitor-queues/-/blob/dev/Asssessment%20Criteria/Assessment%20Criteria%20-%202.2%20-%20Coding%20Fundamentals%20-%20Project.pdf)

## Program

Files created to run the project successfully. 

**variable.py**

- This files connects the application to the database stored in Microsoft SQL server which has been requested by the user.
          
      Database name: Monitor 
      Table name: dbo.logs 2

**app.py**

- It file will run to diaplay the web application using Flask. 
                    
-     Home page using function - def home():
        - renders home page (designed using bootstrap and HTML)
-     About page using function - def about():
        - renders about page (designed using bootstrap and HTML)
-     Top 20 page using function - def top20():
        - renders Top 20 queues (designed using bootstrap and HTML intergates to databases to fetch live data)
-     Top 50 page using function - def top50():
        - renders Top 50 queues (designed using bootstrap and HTML intergates to databases to fetch live data)
-     Top 100 page using function - def top100():
        - renders Top 100 queues (designed using bootstrap and HTML intergates to databases to fetch live data)
-     Job Id page using function - def jobid(): Using GET method
        - User is prompted to share his preference for job id (designed using bootstrap and HTML intergates to databases to fetch live data)
-     Job Id page using function - def getjob(): Using Post method
        - displays queues as per user choice of job id (designed using bootstrap and HTML intergates to databases to fetch live data)
-     Hours 24 page using function - def hours24():
        - renders latest 24 hours queues (designed using bootstrap and HTML intergates to databases to fetch live data)
-     Last week page using function - def lastweek():
        - renders all last week's queues (designed using bootstrap and HTML intergates to databases to fetch live data)

**templates folder**

- home.html
- about.html
- top20.html
- top50.html
- top100.html
- jobid.html
- hours24.html
- lastweek.html
- contactus.html


**test folder**
- test_app.py
- conftest.py
- __init__.py

**static folder**
- css 
- pictures

**linting folder**
- pylint_score_app.png

**assessment criteria**
- assessment-criteria-2.2-Coding Fundamentals-Project.pdf

**website screenshots folder**
- 24hours.png
- about_page.png
- contact_page.png
- home_page.png
- jobid_page.png
- lastweek_page.png
- top20_page.png
- top50_page.png
- top100_page.png

## **Tech Stack**

**Front-end :**
- [HTML](https://html.com/html5/) — to style the web page
- [CSS](https://www.w3schools.com/Css/) — to style the web page
- [Bootstrap](https://getbootstrap.com/) — for frontend design, responsive and mobile-first website. 


**Back-end :**
- Python - version 3.10
    - [PyCharm](https://www.jetbrains.com/pycharm/) — to run the application
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) — base for everything.


**DataBase :**
- [MicrosoftSQLServer](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) — Workbench to design, model, generate and manage database. 

**Testing :**
- [PyTest](https://docs.pytest.org/en/7.2.x/) — pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.


**Workplace Communication Tool:**
- [Microsoft Teams](https://www.microsoft.com/microsoft-teams) — to communicate with your team

**Code Hosting Platform:**
- [GitHub](https://github.com) — for project submission. 
- [GitLab](https://gitlab.com/) — collaboration with team members and version control.


***This Python Project is designed as a part of the DevOps Apprenticeship Level 4 in Feb 2023***   


## 🔗**Profile**

- Employer Name: [S2R Analytics Ltd.](https://www.s2ranalytics.com/)
- Training Provider: [QA Ltd.](https://www.qa.com/)
- Authored by : [Purvi Thakkar](https://www.linkedin.com/in/thakkarpurvilondon)

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/ThakkarPurvi)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thakkarpurvilondon/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/purvi41)
