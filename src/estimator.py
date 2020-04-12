import json
import math


def estimator(data):
    data = impactEstimator(data)
    return data


def periodInDays(periodtype,value):
    value = int(value)
    if periodtype == 'days':
        return value
    elif periodtype == "weeks":
        return value * 7
    elif periodtype == "months":
        return value * 30


def impactEstimator(data):

    dictData = data

    impact = {}
    severeImpact = {}

    # calculation for impact case
    # currently infected calculations

    currentlyInfected = dictData['reportedCases'] * 10

    # calculation for converting the periodtype into days.
    days = periodInDays(dictData['periodType'],dictData['timeToElapse'])
    factor = (days // 3)

    # calculation for infectionByRequestedTime
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)

    # calculating severeCasesByRequestedTime
    severeCasesByRequestedTime = (15/100) * infectionsByRequestedTime

    # calculating hospitalBedsByRequestedTime
    totalHospitalBeds = dictData['totalHospitalBeds']
    totalHospitalBeds = (35/100) * totalHospitalBeds
    hospitalBedsByRequestedTime = severeCasesByRequestedTime - totalHospitalBeds


    # removing decimal places
    currentlyInfected = math.trunc(currentlyInfected)
    infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)
    severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)


    # adding all data gotten into the dictionary
    impact['currentlyInfected'] = currentlyInfected
    impact['infectionsByRequestedTime'] = infectionsByRequestedTime
    impact['severeCasesByRequestedTime']=severeCasesByRequestedTime
    impact['hospitalBedsByRequestedTime']= hospitalBedsByRequestedTime

    # calculation for severeImpact Cases
    # currently infected calculations
    currentlyInfected = dictData['reportedCases'] * 50

    # calculation for infectionByRequestedTime
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)

    # calculating severeCasesByRequestedTime
    severeCasesByRequestedTime = (15/100) * infectionsByRequestedTime

    # calculating hospitalBedsByRequestedTime
    totalHospitalBeds = dictData['totalHospitalBeds']
    totalHospitalBeds = (35/100) * totalHospitalBeds
    hospitalBedsByRequestedTime = severeCasesByRequestedTime - totalHospitalBeds

    # removing decimal places
    currentlyInfected = math.trunc(currentlyInfected)
    infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)
    severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)

    # adding all data to the dicionary
    severeImpact['currentlyInfected'] = currentlyInfected
    severeImpact['infectionsByRequestedTime'] = infectionsByRequestedTime
    severeImpact['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    severeImpact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime

    data = {
        'data': data,
        'impact': impact,
        'severeImpact': severeImpact
    }

    return data
