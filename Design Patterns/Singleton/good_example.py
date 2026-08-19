class Logger:
    __instance = None
    def __new__(cls,filename):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.filename = filename
            cls.log_count = 0
            return cls.__instance
        else:
            return cls.__instance

    def log_msg(self, msg):
        print(f"Logging `{msg}` in {self.filename}")
        self.log_count+=1
    def get_log_count(self) -> int:
        return self.log_count        

log1 = Logger("app.log")
log1.log_msg("Created")
log2 = Logger("app.log")
log2.log_msg("Shipped")
log3 = Logger("app.log")
log3.log_msg("Delivered")

print(log1.log_count)
print(log2.log_count)
print(log3.log_count)
