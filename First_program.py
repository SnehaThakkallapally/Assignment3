old_list=["i love to code in python"]
new_list = []
for sentence in old_list:
    word = ''
    for ch in sentence:
        if ch == ' ' and word != '':
            new_list.append(word)
            word = ''
        else:
            word += ch
    if word != '':
        new_list.append(word)
		
print("Outpu A):", new_list)

list_val=new_list
for passnum in range(len(list_val)-1, 0, -1):
  for i in range(passnum):
    if list_val[i] > list_val[i+1]:
      list_val[i], list_val[i+1] = list_val[i+1], list_val[i]
print("Outpu B):",list_val)

words = list_val
new_list = []
for sample in words:
	#sample = words[i]
	#print(sample)
	name = list(sample)
	#print(name)
	n = len(name);
	#print(n)
	for i in range(n):
		for j in range(1, n-i):
			if name[j-1] > name[j]:
				(name[j-1], name[j]) = (name[j], name[j-1])
		#print(name)
	s = ''
	s = s.join(name)
	#print(s)
	new_list.append(s)
print("Outpu C):",new_list)
