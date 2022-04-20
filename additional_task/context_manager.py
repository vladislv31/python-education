

class MyFileUnsupportedOperationError(Exception):
    pass


class MyFile:

    def __init__(self, file_path, init_type):
        self.file_path = file_path
        self.init_type = init_type

        self.file_obj = open(file_path, init_type)

    def write(self, text):
        if self.init_type == 'w':
            self.file_obj.write(text)
        else:
            raise MyFileUnsupportedOperationError('not writable')

    def append(self, text):
        if self.init_type == 'a':
            self.file_obj.write(text)
        else:
            raise MyFileUnsupportedOperationError('not appendable')

    def read(self):
        if self.init_type == 'r':
            return self.file_obj.read()
        else:
            raise MyFileUnsupportedOperationError('not readable')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, MyFileUnsupportedOperationError):
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_val}")
            return True
        if self.file_obj:
            self.file_obj.close()


def main():
    
    with MyFile('test.txt', 'a') as file_:
        file_.append('asd')


if __name__ == '__main__':
    main()
