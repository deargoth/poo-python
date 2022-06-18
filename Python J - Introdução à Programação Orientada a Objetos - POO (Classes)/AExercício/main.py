import classes

database = classes.DataBase()

client1 = classes.Client('lUcAs', 17)
client1.set_address('Rio de Janeiro', 'RJ')
client1.set_cpf('379.443.700-41')

client2 = classes.Client('roNALdo', 42)
client2.set_address('Tocantins', 'TO')
client2.set_cpf('957.037.900-69')

client3 = classes.Client('viNÍCIUS gonzaga Rezendes', 18)
client3.set_address('Uberlândia', 'MG')
client3.set_cpf('824.792.360-21')

database.insert_client(client1, 1)
database.insert_client(client2, 2)
database.insert_client(client3, 3)

del client1

database.delete_client()
database.list_clients()