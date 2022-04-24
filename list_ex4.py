# sort a list of names from a email list
lista_de_emails=['constanza81@example.net', 'rgarcia@example.net', 'arturo78@example.com', 'andreaherrera@example.net', 'manuel11@example.com', 'diazsalvador@example.net', 'gpena@example.org', 'atorres@example.net', 'orlando84@example.net', 'cristian90@example.net', 'maria38@example.net', 'mario47@example.com', 'hbohorquez@example.org', 'dayanaalarcon@example.net', 'vbarrios@example.org', 'benitezjuan@example.com', 'hugo66@example.com', 'icardozo@example.org', 'lopezemerson@example.com', 'lucilarincon@example.net', 'constanzarodriguez@example.org', 'felipe25@example.net', 'idiaz@example.net', 'richardpalacios@example.org', 'carlosrodriguez@example.com', 'rrincon@example.net', 'imarquez@example.net', 'juliangil@example.com', 'ximenarincon@example.com', 'viviana07@example.org'] 


lista_de_nombres=[]
for email in lista_de_emails:
    name=email.split('@')[0]
    lista_de_nombres.append(name)
print(lista_de_nombres)    
