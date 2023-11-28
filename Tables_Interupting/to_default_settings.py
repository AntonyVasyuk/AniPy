import csv


rows = [
    ["NumOfVisibleFrames", 11]
]


with open('Tables_Interupting/Default_Settings.csv', 'w', newline='') as settings:
    writer = csv.writer(settings, delimiter=';', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerows(rows)