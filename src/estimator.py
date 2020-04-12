import json
import math

def estimator(data):
  data = impactEstimator(data)
  return data

def periodInDays(type,value):
  value = int(value)
  if type == 'days':
    return value
  elif type == "weeks":
    return value * 7
  elif type == "months":
    return value * 30


def  impactEstimator(data):
  if type(data) == str:
    dictData=json.load(data)
  else:
    dictData = data

  impact={}
  severeImpact={}
  #calculation for impact case
  # currently infected calculations
  currentlyInfected = int(dictData['reportedCases']) * 10
  currentlyInfected = math.trunc(currentlyInfected)

  # calculation for severeCasesByRequestedTime
  severeCasesByRequestedTime = (15/100) * currentlyInfected
  severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)

  # calculation for hospitalBedsByRequestedTime
  total = int(dictData['totalHospitalBeds'])
  hospitalBedInPercnetage = (35/100) * total
  hospitalBedsByRequestedTime = (hospitalBedInPercnetage - severeCasesByRequestedTime)
  hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)

  # calculation for converting the periodtype into days.
  days = periodInDays(dictData['periodType'],dictData['timeToElapse'])
  factor = (days/3)

  # calculation for infectionByRequestedTime
  infectionsByRequestedTime = currentlyInfected * (2 ** factor)
  infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)


  # calculation for casesForICUByRequestedTime
  casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime
  casesForICUByRequestedTime = math.trunc(casesForICUByRequestedTime)

  # calculation for casesForVentilatorsByRequestedTime
  casesForVentilatorsByRequestedTime = (2/100) * infectionsByRequestedTime
  casesForVentilatorsByRequestedTime = math.trunc(casesForVentilatorsByRequestedTime)

  # calculation for dollarsInFlight
  avgDailyIncomePopulation = int(dictData['region']['avgDailyIncomePopulation'])
  avgDailyIncomeInUSD = int(dictData['region']['avgDailyIncomeInUSD'])
  dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / days
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
  currentlyInfected = int(dictData['reportedCases']) * 50
  currentlyInfected = math.trunc(currentlyInfected)

  # calculation for infectionByRequestedTime
  infectionsByRequestedTime = currentlyInfected * (2 ** factor)
  infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)

  # calculation for severeCasesByRequestedTime
  severeCasesByRequestedTime = (15/100) * currentlyInfected
  severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)

  # calculation for hospitalBedsByRequestedTime
  total = dictData['totalHospitalBeds']
  hospitalBedInPercnetage = (35/100) * total
  hospitalBedsByRequestedTime = (hospitalBedInPercnetage - severeCasesByRequestedTime)
  hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)

  # calculation for casesForICUByRequestedTime
  casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime
  casesForICUByRequestedTime = math.trunc(casesForICUByRequestedTime)

  # calculation for casesForVentilatorsByRequestedTime
  casesForVentilatorsByRequestedTime = (2/100) * infectionsByRequestedTime
  casesForVentilatorsByRequestedTime = math.trunc(casesForVentilatorsByRequestedTime)

  # calculation for dollarsInFlight
  avgDailyIncomePopulation = int(dictData['region']['avgDailyIncomePopulation'])
  avgDailyIncomeInUSD = int(dictData['region']['avgDailyIncomeInUSD'])
  dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / days
  dollarsInFlight = math.trunc(dollarsInFlight)

  # adding all data to the dicionary
  severeImpact['currentlyInfected']=currentlyInfected
  severeImpact['infectionsByRequestedTime'] = infectionsByRequestedTime
  severeImpact['severeCasesByRequestedTime'] = severeCasesByRequestedTime
  severeImpact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
  severeImpact['casesForICUByRequestedTime'] = casesForICUByRequestedTime
  severeImpact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
  severeImpact['dollarsInFlight'] = dollarsInFlight

  data = {
    'data': data,
    'impact' : impact,
    'severeImpact': severeImpact
  }

  return data
