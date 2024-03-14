class Logger:
    def __init__(self):
        self.log_count = 0
        self.log_file = open("log.txt", "w")
        self.log_file.write("--Start log--\n")

    def log(self, mensaje):
        self.log_count += 1
        self.log_file.write("{}\n".format(mensaje))

    def __del__(self):
        self.log_file.write("--End log: {} log(s)--".format(self.log_count))
        self.log_file.close()


class Test:
    def __init__(self):
        self.logger = Logger()

    def llamada(self, mensaje):
        self.logger.log(mensaje)


def main():
    test = Test()
    for i in range(1, 6):
        if i == 1:
            test.llamada("Primera llamada")
        else:
            test.llamada("{}ª llamada".format(i))

    test.llamada("Ha funcionado todo")
    # Asegurarse de que se haya cerrado el archivo
    del test
    
if __name__ == "__main__":
    main()
