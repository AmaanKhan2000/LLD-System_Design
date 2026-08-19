class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.log_count = 0

    def log(self,text : str):
        print(f"Logger is logging {text} in {self.file_name}")
        self.log_count +=1


log1 = Logger("app.log")
log1.log("Pattern created")
print(log1.log_count)

log2 = Logger("app.log")
log2.log("Pattern received")
print(log2.log_count)


