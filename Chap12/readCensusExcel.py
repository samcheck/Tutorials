#! /usr/bin/python3/
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    #Make sure the key exists and has a default for states and counties
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, also add in population
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it
print('Writing results...')
with open('census2010.py', 'w') as resultFile:
    resultFile.write('allData = ' + pprint.pformat(countyData))
print('Done.')
