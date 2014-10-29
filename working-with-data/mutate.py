"""	Write a function mutate to compute all words generated by a single mutation on a given word. 
	A mutation is defined as inserting a character, deleting a character, replacing a character, or 
	swapping 2 consecutive characters in a string. For simplicity consider only letters from a to z		"""


def mutate(word):
	return insert_set(word) | delete_set(word) | replace_set(word) | swap_set(word)


def a_z():
	return ''.join([chr(i) for i in range(ord('a'),ord('z')+1)])


def insert_set(word):
	ins_set=set()
	for i in range(len(word)+1):
		for c in a_z():
			ins_set.add(word[:i]+c+word[i:])

	return ins_set


def delete_set(word):
	del_set=set()
	for i in range(len(word)):
		del_set.add(word[:i]+word[i+1:])

	return del_set


def replace_set(word):
	rep_set=set()
	for i in range(len(word)):
		for c in a_z():
			rep_set.add(word[:i]+c+word[i+1:])

	return rep_set


def swap_set(word):
	s_set=set()
	l=len(word)
	for i in range(l):
		if i<l-1:
			s_set.add(word[:i] + word[i+1:i+2] + word[i:i+1] + word[i+2:])
		else:
			s_set.add(word[-1] + word[1:-1] + word[:1])
	return s_set
