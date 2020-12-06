def count_yes(fname):
	ans_lst = []
	with open(fname) as f:
		tmp = [] 
		for line in f.readlines():
			if line == '\n':
				ans_lst.append(tmp)
				tmp = []
			else:
				tmp.append(set(line.strip()))
		ans_lst.append(tmp)

	return sum([ len(set([ item for sublist in list_item for item in sublist ])) for list_item in ans_lst ])


print(count_yes('day6inp.txt'))