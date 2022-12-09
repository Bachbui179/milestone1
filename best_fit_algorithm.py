def bestFit(weight, maxSize, n):
	storeItems = [[] for i in range(n)]

	res = 0

	bin_rem = [0]*n

	for i in range(n):
		j = 0
		min = maxSize + 1
		bi = 0
		for j in range(res):
			if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):				
				bi = j
				min = bin_rem[j] - weight[i]
				storeItems[j].append(weight[i])
			else:
				continue
		if (min == maxSize + 1):
			bin_rem[res] = maxSize - weight[i]
			storeItems[res].append(weight[i])
			res += 1
		else: 
			bin_rem[bi] -= weight[i]

	return storeItems