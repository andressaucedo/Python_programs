In [59]: for i in tattoo_machines:
    ...:     print(f"{i}:")
    ...:     for field in tattoo_machines[i]:
    ...:         print(f"\t{field}")
    ...:         print(f"\t\t{tattoo_machines[i][field]}")
    ...: 
    ...: 
    ...: 
    ...: 
2:
	name
		Black widow
	maker
		Tim Hendricks
	year
		2017
3:
	name
		Flite X1
	maker
		Inkjecta
	year
		2019
