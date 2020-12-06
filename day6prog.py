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

	print(f"part 1: {sum([ len(set([ item for sublist in list_item for item in sublist ])) for list_item in ans_lst ])}")
	print(f"part 2: {sum([ len(set.intersection(*i)) for i in [l for l in ans_lst] ])}")



print(count_yes('day6inp.txt'))