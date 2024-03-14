import time


class Palindromo:
    # Esta clase permite comprobar si una palabra es un palíndromo o no.
    # Un palíndromo es una palabra que si la lees al derecho o al revés se lee igual
    
    def __init__(self, cadena):
        self.cadena = cadena.lower()  # Convertir la cadena a minúsculas para ignorar diferencias de mayúsculas
        
    @classmethod #Es un método de clase ya que accede directamente al constructor
    def esPalindromo(cls, cadena):
        cadena_limpia = cadena.lower()
        return cadena_limpia == cadena_limpia[::-1]  # Verificar si la cadena es igual a su inversa
    
    def test(self): 
        resultado = self.esPalindromo(self.cadena)  # Utilizar el método de clase para verificar el palíndromo
        print(self.cadena.upper(), end=": ")  # Imprimir la cadena en mayúsculas
        return resultado
    
    def __del__(self): # Este método permite que al eliminar de la memoria un objeto de clase, previo a que suceda se ejecutará dicho método
        print(f"La palabra: {self.cadena.upper()} se ha eliminado de la memoria")
        
        
def preguntar(num): # Los posibles números son 1 y 2; siendo el número 1 el que pregunta por la palabra que queremos comprobar y el número 2 el número de palabras que queremos comprobar
    while True:
        
        # Comprobar si la respuesta es una palabra (str) si num es 1
        if num == 1:
            respuesta = input("Dime la palabra que quieres comprobar si es un palíndromo o no: ")
            if isinstance(respuesta, str):
                return respuesta
        # Comprobar si la respuesta es un número (int) si num es diferente de 1
        elif num == 2:
            respuesta = input("Dime cuantas palabras quieres comprobar: ")
            if respuesta.isdigit():  # Utilizamos respuesta.isdigit() para verificar si la entrada es un número entero positivo
                return int(respuesta)  # Convertir la respuesta a un entero
        else:
            print("Introduce otra cosa")

def main():
    num_palabras = preguntar(2)  # Solicitar al usuario el número de palabras a verificar
    for _ in range(num_palabras):
        palabra = Palindromo(str(preguntar(1)))  # Solicitar al usuario una palabra
        print(palabra.test())

    time.sleep(1)
    print("Además, a modo de ejemplo, mostraremos las siguientes palabras para entender mejor el comportamiento\n")
    
    palabra2 = Palindromo("radar")
    print(palabra2.test())
    print()
    time.sleep(0.5)
    
    palabra2 = Palindromo("sonar")
    print(palabra2.test())
    print()
    time.sleep(0.5)
    
    palabra2 = Palindromo("Arde ya la yedra")
    print(palabra2.test())
    print()
    time.sleep(0.5)
    
    palabra2 = Palindromo("Ardeyalayedra")
    print(palabra2.test())
    print()
    time.sleep(0.5)



if __name__ == "__main__":
    main()
