# tester file for the project

class OpenCSV:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    

    # select all files in the directory
    # for each file, open it
    # for each file, read it
    # for each file, close it

    def open_file(self):
        with open(self.filename, 'r') as f:
            print(f.read()) 
            

            