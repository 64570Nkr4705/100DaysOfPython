#FORMA PRIMITIVA
'''
class User:
    def __init__(self):
        print("New user being created...")
        
user_1 = User()
user_1.id = "001"
user_1.username = "Gaston"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Jack"
'''

#FORMA SIMPLIFICADA
class User():
    #a esta funcion init se la denomina constructor
    #Cuando una funcion esta unida a un objeto se denomina metodo
    '''tenemos nuestra funcion init, y dentro un self que es nuestro objeto real
        que se esta creando o inicializando,  
        Luego tenemos los parametros,que se van a pasar cuando se construyan los
        objetos desde la clase User()'''
    def __init__(self, user_id, username):
        ''''''
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    '''A diferencia de una funcion, siempre
        necesita tener un parámetro propio como primer parámetro.
        Self es una forma de referirse al objeto que se va a crear a partir de 
        esta clase dentro del plano de la clase.'''
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
#De esta manera pasamos los parametros a nuestra clase User()
#siempre de manera ordenada uno destras de otro
user_1 = User("001", "Gaston")
#print(user_1.id, user_1.username)
user_2 = User("002", "Jack")
#print(user_2.id, user_2.username)

'''Este es el objeto 1 (user_1), y su metodo follow del objeto 1
    y luego el usuario_2 es la persona a la que vamos a seguir'''
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)