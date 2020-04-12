import json
import math


def estimator(data):

    data = impactEstimator(data)
    return data


def periodInDays(periodtype,value):
    if periodtype == 'days':
        return value
    elif periodtype == "weeks":
        return value * 7
    elif periodtype == "months":
        return value * 30


def impactEstimator(data):
    if type(data) == str:
        dictData = json.load(data)
    else:
        dictData = data

    impact = {}
    severeImpact = {}
    # calculation for impact case
    # currently infected calculations
    currentlyInfected = dictData['reportedCases'] * 10

    # calculation for severeCasesByRequestedTime
    severeCasesByRequestedTime = (15 / 100) * currentlyInfected

    # calculation for hospitalBedsByRequestedTime
    total = dictData['totalHospitalBeds']
    hospitalBedInPercnetage = (35 / 100) * total
    hospitalBedsByRequestedTime = (severeCasesByRequestedTime - hospitalBedInPercnetage)

    # calculation for converting the periodtype into days.
    days = periodInDays(dictData['periodType'], dictData['timeToElapse'])
    factor = (days / 3)

    # calculation for infectionByRequestedTime
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)

    # calculation for casesForICUByRequestedTime
    casesForICUByRequestedTime = (infectionsByRequestedTime * 5) /100

    # calculation for casesForVentilatorsByRequestedTime
    casesForVentilatorsByRequestedTime = (infectionsByRequestedTime * 2) / 100

    # calculation for dollarsInFlight
    avgDailyIncomePopulation = dictData['region']['avgDailyIncomePopulation']
    avgDailyIncomeInUSD = dictData['region']['avgDailyIncomeInUSD']
    dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / days

    # removing decimal places
    currentlyInfected = math.trunc(currentlyInfected)
    severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)
    infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)
    hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)
    casesForICUByRequestedTime = math.trunc(casesForICUByRequestedTime)
    casesForVentilatorsByRequestedTime = math.trunc(casesForVentilatorsByRequestedTime)
    dollarsInFlight = math.trunc(dollarsInFlight)

    # adding all data gotten into the dictionary
    impact['currentlyInfected'] = currentlyInfected
    impact['infectionsByRequestedTime'] = infectionsByRequestedTime
    impact['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    impact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
    impact['casesForICUByRequestedTime'] = casesForICUByRequestedTime
    impact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
    impact['dollarsInFlight'] = dollarsInFlight

    # calculation for severeImpact Cases
    # currently infected calculations
    currentlyInfected = dictData['reportedCases'] * 50

    # calculation for infectionByRequestedTime
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)

    # calculation for severeCasesByRequestedTime
    severeCasesByRequestedTime = (currentlyInfected * 15) / 100

    # calculation for hospitalBedsByRequestedTime
    total = dictData['totalHospitalBeds']
    hospitalBedInPercnetage = (total * 35) / 100
    hospitalBedsByRequestedTime = (severeCasesByRequestedTime - hospitalBedInPercnetage)

    # calculation for casesForICUByRequestedTime
    casesForICUByRequestedTime = (infectionsByRequestedTime * 5) / 100

    # calculation for casesForVentilatorsByRequestedTime
    casesForVentilatorsByRequestedTime = (infectionsByRequestedTime * 2) / 100

    # calculation for dollarsInFlight
    avgDailyIncomePopulation = dictData['region']['avgDailyIncomePopulation']
    avgDailyIncomeInUSD = dictData['region']['avgDailyIncomeInUSD']
    dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / days

    # removing decimal places
    currentlyInfected = math.trunc(currentlyInfected)
    infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)
    severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)
    casesForICUByRequestedTime = math.trunc(casesForICUByRequestedTime)
    casesForVentilatorsByRequestedTime = math.trunc(casesForVentilatorsByRequestedTime)
    dollarsInFlight = math.trunc(dollarsInFlight)

    # adding all data to the dicionary
    severeImpact['currentlyInfected'] = currentlyInfected
    severeImpact['infectionsByRequestedTime'] = infectionsByRequestedTime
    severeImpact['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    severeImpact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
    severeImpact['casesForICUByRequestedTime'] = casesForICUByRequestedTime
    severeImpact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
    severeImpact['dollarsInFlight'] = dollarsInFlight

    data = {
        'data': data,
        'impact': impact,
        'severeImpact': severeImpact
    }

    return data
