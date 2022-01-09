"""
* Assignment: Conditional BooleanAlgebra BloodPressure
* Required: yes
* Complexity: medium
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Table contains Blood Pressure classification according to American Heart Association [1]
    2. User inputs blood pressure in `XXX/YY` or `XXX/YYY` format
    3. User will not try to input invalid data
    4. Data format:
        a. `XXX: int` systolic pressure
        b. `YY: int` or `YYY: int` diastolic pressure
    5. Print status of given blood pressure
    6. If systolic and diastolic values are in different categories, assume worst case
    7. Run doctests - all must succeed

Polish:
    1. Tabela zawiera klasyfikację ciśnienia krwi wg American Heart Association [1]
    2. Użytkownik wprowadza ciśnienie krwi w formacie `XXX/YY` lub `XXX/YYY`
    3. Użytkownik nie będzie próbował wprowadzać danych niepoprawnych
    4. Format danych:
        a. `XXX: int` to wartość ciśnienia skurczowego (ang. *systolic*)
        b. `YY: int` lub `YYY: int` to wartość ciśnienia rozkurczowego (ang. *diastolic*)
    5. Wypisz status wprowadzonego ciśnienia krwi
    6. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek
    7. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `and`
    * `or`

References:
    [1] Whelton, Paul K. and et al.
        2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline for the
        Prevention, Detection, Evaluation, and Management of High Blood Pressure
        in Adults: Executive Summary: A Report of the American College of
        Cardiology/American Heart Association Task Force on Clinical Practice Guidelines.
        Journal of Hypertension. vol 71. pages 1269–1324. 2018. doi: 10.1161/HYP.0000000000000066

Tests:
    TODO: Better Tests

    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assign result to variable: `result`'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> result in (STATUS_NORMAL, STATUS_ELEVATED, STATUS_HYPERTENSION_STAGE_1,
    ...            STATUS_HYPERTENSION_STAGE_2, STATUS_HYPERTENSIVE_CRISIS)
    True

    >>> assert blood_pressure == '119/79' and result == 'Normal' or True
    >>> assert blood_pressure == '120/80' and result == 'Hypertension stage 1' or True
    >>> assert blood_pressure == '121/79' and result == 'Elevated' or True
    >>> assert blood_pressure == '120/81' and result == 'Hypertension stage 1' or True
    >>> assert blood_pressure == '125/85' and result == 'Hypertension stage 1' or True
    >>> assert blood_pressure == '130/80' and result == 'Hypertension stage 1' or True
    >>> assert blood_pressure == '130/89' and result == 'Hypertension stage 1' or True
    >>> assert blood_pressure == '130/100' and result == 'Hypertension stage 2' or True
    >>> assert blood_pressure == '140/85' and result == 'Hypertension stage 2' or True
    >>> assert blood_pressure == '140/89' and result == 'Hypertension stage 2' or True
    >>> assert blood_pressure == '141/90' and result == 'Hypertension stage 2' or True
    >>> assert blood_pressure == '141/91' and result == 'Hypertension stage 2' or True
    >>> assert blood_pressure == '180/120' and result == 'Hypertensive Crisis' or True
    >>> assert blood_pressure == '181/121' and result == 'Hypertensive Crisis' or True
    >>> assert blood_pressure == '181/50' and result == 'Hypertensive Crisis' or True
    >>> assert blood_pressure == '100/121' and result == 'Hypertensive Crisis' or True
    >>> assert blood_pressure == '181/121' and result == 'Hypertensive Crisis' or True
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['119/79', '120/80', '121/79',
                               '120/81', '130/80', '130/89',
                               '140/85', '140/89', '141/90',
                               '141/91', '180/120', '181/121',
                               '181/50', '100/121', '181/121'])

STATUS_NORMAL = 'Normal'
STATUS_ELEVATED = 'Elevated'
STATUS_HYPERTENSION_STAGE_1 = 'Hypertension stage 1'
STATUS_HYPERTENSION_STAGE_2 = 'Hypertension stage 2'
STATUS_HYPERTENSIVE_CRISIS = 'Hypertensive Crisis'

blood_pressure = input('What is your Blood Pressure?: ')
systolic, diastolic = blood_pressure.strip().split('/')
systolic = int(systolic)
diastolic = int(diastolic)


# | Blood Pressure Category | Systolic [mm Hg] | Operator | Diastolic [mm Hg] |
# |-------------------------|------------------|----------|-------------------|
# | Normal                  | Less than 120    | and      | Less than 80      |
# | Elevated                | 120-129          | and      | Less than 80      |
# | Hypertension stage 1    | 130-139          | or       | 80-89             |
# | Hypertension stage 2    | 140 or higher    | or       | 90 or higher      |
# | Hypertensive Crisis     | Higher than 180  | and/or   | Higher than 120   |

# str: one of the STATUS_*
#result = ...

if systolic < 120 and diastolic < 80:
    result = STATUS_NORMAL
elif 120 <= systolic < 130 and diastolic < 80:
    result = STATUS_ELEVATED
elif 130 <= systolic < 140 or 80 <= diastolic < 90:
    result = STATUS_HYPERTENSION_STAGE_1
elif systolic >= 140 or diastolic >= 90:
    result = STATUS_HYPERTENSION_STAGE_2
elif systolic >= 180 or diastolic >= 120:
    result = STATUS_HYPERTENSIVE_CRISIS
