'''
Class containing common methos (create files, etc)

'''

class common_functions:

    def create_file_n_numbers(self, n=100, file_name='random_number.txt',
            separator=' '):
        print("Generating file {0}. With {1} numbers".format(file_name, n))
        with open(file_name, 'w+') as f:
            for x in range(n):
                f.write(str(random.randint(-30000,30000)) + separator)
        return file_name

    def read_file_n_numbers(self, file_name, separator=' '):
        # Read array from file 
        print("Reading numbers from file {0}.".format(file_name))
        content = None
        with open(file_name, 'r') as f:
            content = f.readlines()
        return content[0].strip().split(separator)
