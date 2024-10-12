import pandas as pd
from student_groups.models import Student

# Load the Excel file (use the correct path to your file)
df = pd.read_excel('C:/Users/user/Downloads/.vscode/liste_ING2_24_25.xlsx',header=3)

# Iterate over the rows and save them to the database
for index, row in df.iterrows():
    Student.objects.create(
        n=row['N'],
        numero_inscription=row['Numero Inscription'],
        bac_year=row['Annee Bac'],
        matricule=row['Matricule'],
        nom=row['Nom'],
        prenom=row['Prenom'],
        section=row['Section'],
        group_actual=row['Groupe']
    )













