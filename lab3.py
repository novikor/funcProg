import numpy as np
import pandas as pd


def question_1(df: pd.DataFrame):
    print('Скільки чоловіків і жінок представлено в цьому наборі даних?\n')
    avg_height = df.height.mean()

    df['sex'] = (df['height'] > avg_height).map({True: 'male', False: 'female'})

    cnt = df.groupby(['sex', 'gender'])['id'].count()

    # print(cnt)

    df['gender'] = df['gender'].map({cnt['female'].idxmax(): 'female', cnt['male'].idxmax(): 'male'})
    del df['sex']

    print(df.groupby(['gender'])['id'].count())


def question_2(df: pd.DataFrame):
    print('\nХто в середньому рідше вказує, що вживає алкоголь - чоловіки чи жінки?\n')
    result = df.loc[df['alco'] == 1].groupby(['gender'])['id'].count()
    print(result)
    print('Відповідь: ' + result.idxmin())


def question_3(df: pd.DataFrame):
    print('\nУ скільки разів відсоток курців серед чоловіків більше, ніж відсоток курців серед жінок?\n')
    all_smokers = df.groupby(['gender', 'smoke'])['id'].count()

    male_smokers_percent = round((all_smokers['male'][1] * 100) / sum(all_smokers['male']))
    female_smokers_percent = round((all_smokers['female'][1] * 100) / sum(all_smokers['female']))
    # print(male_smokers_percent, female_smokers_percent)
    print('В {0} разів'.format(male_smokers_percent / female_smokers_percent))


def question_4(df: pd.DataFrame):
    print('\nНа скільки місяців (приблизно) відрізняються медіанне значення віку курців і тих хто не курить?\n')
    not_smoking_male = df[(df['gender'] == 'male') & (df['smoke'] == 0)]
    not_smoking_female = df[(df['gender'] == 'female') & (df['smoke'] == 0)]
    male_smokers = df[(df['gender'] == 'male') & (df['smoke'] == 1)]
    female_smokers = df[(df['gender'] == 'female') & (df['smoke'] == 1)]

    median_age_of_smoking = (female_smokers['age'].median() / 365) * 12 + (male_smokers['age'].median() / 365) * 12
    median_age_of_not_smoked = (not_smoking_male['age'].median() / 365) * 12 + (
            not_smoking_female['age'].median() / 365) * 12

    print(str(int(round(median_age_of_not_smoked - median_age_of_smoking))) + ' місяців')


def question_5(df: pd.DataFrame):
    print('\nУ скільки разів відрізняються частки хворих людей в цих двох підвибірках?\n')
    df['age_years'] = round(df['age'] / 365)
    old_guys = df[df['age_years'].between(60.0, 64.0)]
    first_group = old_guys.query('ap_hi < 120 & cholesterol == 1')
    percents_of_sick_first_group = (100 * len(first_group.query('cardio == 1').index)) / len(first_group.index)
    second_group = old_guys.query('ap_hi >=160 & ap_hi < 180 & cholesterol == 3')
    percents_of_sick_second_group = (100 * len(second_group.query('cardio == 1').index)) / len(
        second_group.index)
    res = percents_of_sick_second_group / percents_of_sick_first_group

    print('Частка хворих в другій підгрупі в {0} рази більша, ніж в першій'.format((round(res))))


def question_6(df: pd.DataFrame):
    print('\nТвердження:\n')
    df['BMI'] = round(df['weight'] / (np.square(df['height'] / 100)))
    print('Медіанний BMI по вибірці перевищує норму: ' + ('Ні' if df['BMI'].median() < 25 else 'Так'))
    print('У жінок в середньому BMI нижче, ніж у чоловіків: ' + (
        'Так'
        if df[df['gender'] == 'male']['BMI'].mean() > df[df['gender'] == 'female']['BMI'].mean()
        else 'Ні'
    ))
    print('У здорових в середньому BMI вище, ніж у хворих: ' + (
        'Так' if df[df['cardio'] == 0]['BMI'].mean() > df[df['cardio'] == 1]['BMI'].mean() else 'Ні')
          )

    healthy_males = df.query('gender == "male" & cardio == 0 & alco == 0')
    healthy_females = df.query('gender == "female" & cardio == 0 & alco == 0')
    norm_bmi_males = healthy_males[healthy_males['BMI'].between(18.5, 25)]
    percent_of_norm_bmi_males = (len(norm_bmi_males) * 100) / len(healthy_males)
    # print(percent_of_norm_bmi_males)

    norm_bmi_females = healthy_females[healthy_females['BMI'].between(18.5, 25)]
    percent_of_norm_bmi_females = (len(norm_bmi_females) * 100) / len(healthy_females)
    # print(percent_of_norm_bmi_females)

    print('У сегменті здорових і тих що не вживають алкоголь чоловіків в середньому BMI ближче до норми, '
          'ніж в сегменті здорових і тих що не вживають алкоголь жінок: {0}'
          .format('Так' if (percent_of_norm_bmi_males > percent_of_norm_bmi_females) else 'Ні')
          )


def question_7(df: pd.DataFrame):
    # print(df.head())
    filtered = df.query(
        '(ap_lo < ap_hi) & (weight > {0}) & (height > {1})'.format(
            df['weight'].quantile(.975), df['height'].quantile(.975)
        )
    )
    # print(len(filtered))
    print(
        '\nСкільки відсотків даних ми викинули? А вот стільки: {0}%\n'.format(
            str(np.round(((len(df) - len(filtered)) * 100) / len(df), 2))
        ))
