import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').size()

    # What is the average age of men?
    average_age_men = df.loc[df.loc[:, 'sex'] == 'Male', 'age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors', 'education'].count() / df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] ==  'Doctorate'), ['education', 'salary']]
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] !=  'Doctorate'), ['education', 'salary']]

    # percentage with salary >50K
    higher_education_rich = round(higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] * 100, 1)
    lower_education_rich = round(lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()].shape[0]

    rich_percentage = round(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')].shape[0] / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_groups = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    highest_earning_country_groups['>50K Percentage'] = highest_earning_country_groups['>50K'] * 100

    highest_earning_country = highest_earning_country_groups['>50K Percentage'].idxmax()
    highest_earning_country_percentage = highest_earning_country_groups['>50K Percentage'].max().round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    IN_occupations_group = df[df['native-country'] == 'India'].groupby('occupation').size().reset_index(name='count')
    top_IN_occupation = IN_occupations_group.loc[IN_occupations_group['count'].idxmax()]['occupation']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
