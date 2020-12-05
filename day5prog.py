#FBFBBFFRLR
from math import ceil, floor

inp = "FBFBBFFRLR"

def find_seat(inp):
	rows = inp[:7]
	cols = inp[7:]

	start = 0
	stop = 127
	t = stop / 2

	row = 0
	col = 0

	#to find row
	start, stop = (0, floor(t)) if inp[0] == 'F' else (ceil(t), stop) #F = (0, 63), B = (64, 127)
	start, stop = (start, floor(start+(stop-start)/2)) if inp[1] == 'F' else (ceil(start+(stop-start)/2), stop) 
	start, stop = (start, floor(start+(stop-start)/2)) if inp[2] == 'F' else (ceil(start+(stop-start)/2), stop)
	start, stop = (start, floor(start+(stop-start)/2)) if inp[3] == 'F' else (ceil(start+(stop-start)/2), stop)
	start, stop = (start, floor(start+(stop-start)/2)) if inp[4] == 'F' else (ceil(start+(stop-start)/2), stop)
	start, stop = (start, floor(start+(stop-start)/2)) if inp[5] == 'F' else (ceil(start+(stop-start)/2), stop)
	start, stop = (start, floor(start+(stop-start)/2)) if inp[6] == 'F' else (ceil(start+(stop-start)/2), stop)

	row = start

	#to find column
	start = 0
	stop = 7
	t = stop / 2
	start, stop = (0, floor(t)) if cols[0] == 'L' else (ceil(t), stop)
	start, stop = (start, floor(start+(stop-start)/2)) if cols[1] == 'L' else (ceil(start+(stop-start)/2), stop) 
	start, stop = (start, floor(start+(stop-start)/2)) if cols[2] == 'L' else (ceil(start+(stop-start)/2), stop) 

	col = start

	return row*8+col

seat_list = []
with open('day5inp.txt', 'r') as f:
	for line in f.readlines():
		seat_list.append(find_seat(line.strip()))

print(seat_list)
print(max(seat_list))





















