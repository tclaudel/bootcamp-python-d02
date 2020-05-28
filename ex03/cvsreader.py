class CsvReader:
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.fd = None
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        try:
            self.fd = open(self.filename, "r")
            self.read_data()
            return self
        except FileNotFoundError:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd:
            self.fd.close()

    def read_data(self):
        content = self.fd.readlines()[self.skip_top:]
        del content[:self.skip_bottom]
        if self.header is True:
            self.header = content[0][:-1].split(self.sep)
            for i in range(1, len(content)):
                new_dict = {}
                splitted_content = content[i][:-1].split(self.sep)
                for j in range(0, len(self.header)):
                    new_dict[self.header[j]] = splitted_content[j]
                self.data.append(new_dict)
        else:
            for line in content:
                self.data.append(line[:len(line) - 1].split(self.sep))
            # print(self.data)

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


if __name__ == "__main__":
    with CsvReader('faker.csv', ",", False, 0, 0) as file:
        if file is None:
            print("File is corrupted")
            exit(1)
        data = file.getdata()
        header = file.getheader()
        for item in data:
            print("{}".format(item))
        print(header)
