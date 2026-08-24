# CS 340 Portfolio

## Project Two Artifacts

This repository contains the main files for the CS 340 Project Two dashboard:

- `ProjectTwoDashboard.ipynb`
- `CRUD_Python_Module.py`
- `Grazioso Salvare Logo.png`
- `CS340_Project_Two_README_Aidan_Cauley.docx`

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

I write maintainable programs by separating the project into smaller parts and using clear names for files, classes, methods, and variables. For this course, the CRUD Python module helped keep the MongoDB connection and database operations separate from the dashboard code. This made Project Two easier to build because the dashboard could focus on the layout, filters, data table, chart, and map, while the AnimalShelter class handled the database work.

The advantage of working this way is that the same CRUD module can be reused instead of rewriting database code in multiple places. It also makes the project easier to test and update. In the future, this CRUD module could be used for another dashboard, a reporting tool, or another application that needs to read, create, update, or delete animal records from the database.

### How do you approach a problem as a computer scientist?

I approach a problem by first understanding what the client needs and then breaking the work into smaller steps. For the Grazioso Salvare project, I started by reviewing the dashboard requirements and the rescue dog criteria. Then I translated those requirements into MongoDB queries and connected the query results to dashboard widgets.

This project was different from earlier assignments because it was more client-focused. It was not only about writing a query or a Python method. It was also about making the data useful through an interactive dashboard. In the future, I would use the same strategy by studying the client request, reviewing the available data, building queries that match the requirements, testing the results, and then creating an interface that makes the information easier to understand.

### What do computer scientists do, and why does it matter?

Computer scientists solve problems by designing systems that organize, process, and present information in useful ways. This matters because many companies have a lot of data, but they need tools that help them make decisions from that data.

For a company like Grazioso Salvare, this type of project can help make their work faster and more accurate. Instead of manually searching through animal records, the dashboard lets the user choose a rescue category and immediately see matching dogs, breed information, and location data. This helps the company identify strong candidates for rescue training and use the animal shelter data more effectively.
# CS-340
