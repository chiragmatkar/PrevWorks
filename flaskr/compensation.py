from flaskr.pg_db_connect import get_db
import pandas as pd


# Workers' Comp Premium = Employee Classification Rate  X  Employer Payroll (Per $100) X Experience Mod Rate (Mod)
def calc_total_comp(employee_classification, industry, payroll, total_hours_worked, num_injuries):
    # read in employee classification rates and industry incidence data
    class_df = pd.read_csv('data/raw/Employee_Classification_Rates.csv')
    industry_df = pd.read_excel('data/raw/labor_statistics/by_industry/rate/cd_r5_2019.xlsx')

    classifications = class_df['phrase'].tolist()
    industries = industry_df['Industry(1)'].tolist()

    # get employee classification rate
    phrase_to_rate = dict(zip(classifications, class_df['employee classification rate'].tolist()))
    print(phrase_to_rate)
    class_rate = phrase_to_rate[employee_classification]
    if '$' in class_rate:
        class_rate = class_rate.replace('$', '')
    # calculate company and industry incidence rates
    incidence_rate = float(num_injuries) / float(total_hours_worked) * 20000000
    industry_to_average_incidence = dict(zip(industries, industry_df['Total rate'].tolist()))
    industry_incidence = float(industry_to_average_incidence[industry])

    # make industry incidence in same units as company's
    industry_incidence = industry_incidence
    premium = "{:,}".format(round(float(class_rate) * float(payroll) / 100 * float(incidence_rate) / float(industry_incidence), 2))
    return premium


def calc_specific_comp(age, occupation, employee_salary, employee_classification):
    db = get_db()
    dbcursor = db.cursor()
    # get occupation ID
    dbcursor.execute(
        "SELECT occupationId"
        "FROM occupations"
        "WHERE occupationName = %s", occupation
    )
    occupation_id = dbcursor.fetchone()
    if occupation_id is None:
        return -1

    # get probability of injury for specific worker
    dbcursor.execute(
        "SELECT probability"
        "FROM occupationAgeProbabilities "
        "WHERE ageUpper >= %d AND ageLower <= %d AND occupationId = %s", (int(age), int(age), occupation_id)
    )
    injury_probability = dbcursor.fetchone()
    if injury_probability is None:
        return -1

    # get employee classification rate
    class_df = pd.read_csv('data/raw/Employee_Classification_Rates.csv')
    classifications = class_df['phrase'].tolist()
    phrase_to_rate = dict(zip(classifications, class_df['employee classification rate'].tolist()))
    class_rate = phrase_to_rate[employee_classification].strip()
    if '$' in class_rate:
        class_rate = class_rate.replace('$', '')

    premium = "{:,}".format(round((float(employee_salary)/100 * injury_probability * float(class_rate)), 2))

    return premium


def calc_industry_premium(employee_classification, industry, payroll):
    # read in employee classification rates and industry incidence data
    class_df = pd.read_csv('data/raw/Employee_Classification_Rates.csv')
    industry_df = pd.read_excel('data/raw/labor_statistics/by_industry/rate/cd_r5_2019.xlsx')

    classifications = class_df['phrase'].tolist()
    industries = industry_df['Industry(1)'].tolist()

    # get employee classification rate
    phrase_to_rate = dict(zip(classifications, class_df['employee classification rate'].tolist()))
    class_rate = phrase_to_rate[employee_classification]
    if '$' in class_rate:
        class_rate = class_rate.replace('$', '')
    # calculate company and industry incidence rates
    industry_to_average_incidence = dict(zip(industries, industry_df['Total rate'].tolist()))
    industry_incidence = float(industry_to_average_incidence[industry])

    # make industry incidence in same units as company's
    industry_incidence = industry_incidence / 20000000
    premium = "{:,}".format(round(float(class_rate) * float(payroll) / 100, 2))

    return premium


