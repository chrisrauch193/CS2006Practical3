def data_translation(field, value):

    def person_id(value):

        return value

    def region(value):

        lookup = {
            'E12000001': 'North East',
            'E12000002': 'North West',
            'E12000003': 'Yorkshire and the Humber',
            'E12000004': 'East Midlands',
            'E12000005': 'West Midlands',
            'E12000006': 'East of England',
            'E12000007': 'London',
            'E12000008': 'South East',
            'E12000009': 'South West',
            'W92000004': 'Wales',
        }

        return lookup.get(value, None)

    def residence_type(value):

        lookup = {
            'C': 'Resident',
            'H': 'Not Resident',
        }

        return lookup.get(value, None)

    def family_composition(value):

        lookup = {
            1: 'Not in Family',
            2: 'Married/Civil Partnership',
            3: 'Cohabiting Couple Family',
            4: 'Lone Parent Family (Male)',
            5: 'Lone Parent Family (Female)',
            6: 'Other Related Family',
            -9: 'No Code Required',
        }

        return lookup.get(value, None)

    def population_base(value):

        lookup = {
            1: 'Usual Resident',
            2: 'Student Living Away From Home',
            3: 'Short-term Resident',
        }

        return lookup.get(value, None)

    def sex(value):

        lookup = {
            1: 'Male',
            2: 'Female',
        }

        return lookup.get(value, None)

    def age(value):

        lookup = {
            1: '0 to 15',
            2: '16 to 24',
            3: '25 to 34',
            4: '35 to 44',
            5: '45 to 54',
            6: '55 to 64',
            7: '65 to 74',
            8: '75 and Over',
        }

        return lookup.get(value, None)

    def marital_status(value):

        lookup = {
            1: 'Single (Never Married/Civil Partnership)',
            2: 'Married/Civil Partnership',
            3: 'Separated but Still Legally Married/Civil Partnership',
            4: 'Divorced or Formerly in a Civil Partnership',
            5: 'Widowed',
        }

        return lookup.get(value, None)

    def student(value):

        lookup = {
            1: True,
            2: False,
        }

        return lookup.get(value, None)

    def country_of_birth(value):

        lookup = {
            1: 'UK',
            2: 'Non-UK',
            -9: 'No Code Required',
        }

        return lookup.get(value, None)

    def health(value):

        lookup = {
            1: 'Very Good Health',
            2: 'Good Health',
            3: 'Fair Health',
            4: 'Bad Health',
            5: 'Very Bad Health',
            -9: 'No Code Requried',
        }

        return lookup.get(value, None)

    def ethnic_group(value):

        lookup = {
            1: 'White',
            2: 'Mixed',
            3: 'Asian or Asian British',
            4: 'Black or Black British',
            5: 'Chinese or Other',
            -9: 'No Code Requried',
        }

        return lookup.get(value, None)

    def religion(value):

        lookup = {
            1: 'No Religion',
            2: 'Christian',
            3: 'Buddhist',
            4: 'Hindu',
            5: 'Jewish',
            6: 'Muslim',
            7: 'Sikh',
            8: 'Other Religion',
            9: 'Not Stated',
            -9: 'No Code Required',
        }

        return lookup.get(value, None)

    def economic_activity(value):

        lookup = {
            1: 'Employee',
            2: 'Self-employed',
            3: 'Unemployed',
            4: 'Full-time Student',
            5: 'Retired',
            6: 'Student',
            7: 'Looking After Home or Family',
            8: 'Long-term Sick or Disabled',
            9: 'Other',
            -9: 'No Code Required',
        }

        return lookup.get(value, None)

    def occupation(value):

        lookup = {
            1: 'Managers, Directors and Senior Officials',
            2: 'Professional',
            3: 'Associate Professional and Technical',
            4: 'Administrative and Secretarial',
            5: 'Skilled Trades',
            6: 'Caring, Leisure and Other Service',
            7: 'Sales and Customer Service',
            8: 'Process, Plant and Machine Operatives',
            9: 'Elementary',
            -9: 'No Code Required',
        }

        return lookup.get(value, None)

    def industry(value):

        lookup = {
            1: 'Agriculture, FOrestry adn Fishing',
            2: 'Mining and Quarrying',
            3: 'Construction',
            4: 'Wholesale and Retail Trade',
            5: 'Accommodation and Food Service',
            6: 'Transport and Storage',
            7: 'Financial and Insurance',
            8: 'Real Estate',
            9: 'Public Adminstration and Defence',
            10: 'Education',
            11: 'Human Health and Social Work',
            12: 'Other Community, Social and Personal Service',
            -9: 'No Code Required',
        }

        return lookup.get(value, None)

    def hours_worked_per_week(value):

        lookup = {
            1: '15 or Less Hours',
            2: '16 to 30 Hours',
            3: '31 to 48 Hours',
            4: '49 or More Hours',
            -9: 'No Code Required'
        }

        return lookup.get(value, None)

    def approximated_social_grade(value):

        lookup = {
            1: 'AB',
            2: 'C1',
            3: 'C2',
            4: 'DE',
            -9: 'No Code Required'
        }

        return lookup.get(value, None)

    translations = {
        'Person ID': person_id,
        'Region': region,
        'Residence Type': residence_type,
        'Family Composition': family_composition,
        'Population Base': population_base,
        'Sex': sex,
        'Age': age,
        'Marital Status': marital_status,
        'Student': student,
        'Country of Birth': country_of_birth,
        'Health': health,
        'Ethnic Group': ethnic_group,
        'Religion': religion,
        'Economic Activity': economic_activity,
        'Occupation': occupation,
        'Industry': industry,
        'Hours worked per week': hours_worked_per_week,
        'Approximated Social Grade': approximated_social_grade,
    }

    return translations[field](value)
