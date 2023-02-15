import sqlite3
import xlsxwriter


workbook = xlsxwriter.Workbook('vehicles.xlsx')

worksheet = workbook.add_worksheet()

conn = sqlite3.connect("main.db", check_same_thread=False)
cur = conn.cursor()

cur.execute(f"SELECT * FROM vehicles")
vehicles_info = cur.fetchall()

nn = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'North' and vehicle_info[9] == 'North']
ne = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'North' and vehicle_info[9] == 'East']
nw = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'North' and vehicle_info[9] == 'West']
ns = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'North' and vehicle_info[9] == 'South']

en = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'East' and vehicle_info[9] == 'North']
ee = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'East' and vehicle_info[9] == 'East']
ew = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'East' and vehicle_info[9] == 'West']
es = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'East' and vehicle_info[9] == 'South']

wn = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'West' and vehicle_info[9] == 'North']
we = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'West' and vehicle_info[9] == 'East']
ww = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'West' and vehicle_info[9] == 'West']
ws = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'West' and vehicle_info[9] == 'South']

sn = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'South' and vehicle_info[9] == 'North']
se = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'South' and vehicle_info[9] == 'East']
sw = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'South' and vehicle_info[9] == 'West']
ss = [vehicle_info for vehicle_info in vehicles_info if vehicle_info[8] == 'South' and vehicle_info[9] == 'South']

worksheet.write('A1', 'in\\out')

worksheet.write('B1', 'North')
worksheet.write('C1', 'East')
worksheet.write('D1', 'West')
worksheet.write('E1', 'South')

worksheet.write('A2', 'North')
worksheet.write('A3', 'East')
worksheet.write('A4', 'West')
worksheet.write('A5', 'South')

worksheet.write('B2', str(len(nn)))
worksheet.write('C2', str(len(ne)))
worksheet.write('D2', str(len(nw)))
worksheet.write('E2', str(len(ns)))

worksheet.write('B3', str(len(en)))
worksheet.write('C3', str(len(ee)))
worksheet.write('D3', str(len(ew)))
worksheet.write('E3', str(len(es)))

worksheet.write('B4', str(len(wn)))
worksheet.write('C4', str(len(we)))
worksheet.write('D4', str(len(ww)))
worksheet.write('E4', str(len(ws)))

worksheet.write('B5', str(len(sn)))
worksheet.write('C5', str(len(se)))
worksheet.write('D5', str(len(sw)))
worksheet.write('E5', str(len(ss)))
 
# Finally, close the Excel file
# via the close() method.
workbook.close()
