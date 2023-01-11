import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?
1  percentage_bachelors = round(
    ((df['education'] == 'Bachelors').sum() / df.index.size) * 100, 2)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?
  higherEd = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters')
              | (df['education'] == 'Doctorate'))
  total_higher_ed = higherEd.sum()
  total_no_higher_ed = (~higherEd).sum()
  higher_ed_50k_plus = ((higherEd) & (df['salary'] == ">50K")).sum()
  no_higher_ed_50k_plus = ((~higherEd) & (df['salary'] == ">50K")).sum()

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  # percentages...
  higher_education = total_higher_ed / df.index.size
  lower_education = total_no_higher_ed / df.index.size

  # percentage with salary >50K
  higher_education_rich = round(higher_ed_50k_plus / total_higher_ed * 100, 1)
1  lower_education_rich = round(
    no_higher_ed_50k_plus / total_no_higher_ed * 100, 2)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = (df['hours-per-week'] == min_work_hours).sum()
  num_min_workers_50k_plus = ((df['hours-per-week'] == min_work_hours) &
                              (df['salary'] == ">50K")).sum()

  rich_percentage = round(num_min_workers_50k_plus / num_min_workers * 100, 1)

  # What country has the highest percentage of people that earn >50K?
  country_counts = df['native-country'].value_counts()
  country_50k_counts = df[df['salary'] ==
                          '>50K']['native-country'].value_counts()
  country_rich_percentage = (country_50k_counts / country_counts) * 100
  highest_earning_country = country_rich_percentage.idxmax()
1  highest_earning_country_percentage = round(country_rich_percentage.max(), 2)

  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = df[(df['native-country'] == 'India') & (
    df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
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
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }


calculate_demographic_data()
