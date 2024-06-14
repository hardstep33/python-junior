def read_generator(file_name):
    f = open(file_name)
    for index, row in enumerate(f.readlines()):
        yield index, row


for index, row in read_generator("log.txt"):
    result = row.lower().find("error")
    if result != -1:
        print(f"[{index}], ROW: {row}".format(index=index, row=row))
