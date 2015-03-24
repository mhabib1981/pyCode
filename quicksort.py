a=[1201,854,8,52,27,924,9,9,5,65,3,59,850,73,831,4,676,110,988,10,70,1627,57]
b=[1007,7,96,404,30,853,11,928,623,3,7,166,2,486,806,14,123,100,8,92,99,1569,220]
c=[15,1212,1,50,65,930,229,5,70,94,8,89,95,412,816,219,13,590,18,95,109,949,201]

def quicksort(list, start, end):
	if start < end:
		pivot=partition(list, start, end)
		quicksort (list, start, pivot-1)
		quicksort (list, pivot+1, end)
	return list


def partition(list, start, end):
	pivot=list[start]
	left=pivot+1
	right=end
	done=False
	while not done:
		while left <= right and list[left] <= pivot:
			left=left+1
		while list[right] >= pivot and right >=left:
			right=right-1
		if right < left:
			done=True
		else:
			temp=list[left] 
			list[left]=list[right]
			list[right]=temp
		temp=list[start]
		list[start]=list[right]
		list[right]=temp
	return right

def main():
	list_sorted=quicksort(a, 0, len(a)-1)
	print list_sorted
	
main()
