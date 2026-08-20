class UserService:
    def login(self, username:str,password:str) -> dict:
        print(f"[UserService] is logging in {username}")
        return {"user_id": "kanhh56", "username": {username}}
    def get_user(self,userid: str) -> dict:
        print(f"[UserService] getting user for {userid}")
        return {"user_id":{userid}, "name": "Amaan", "Address":"Tempe"}


class OrderService:
    def get_orders(self, user_id: str) -> list:
        print(f"[OrderService] getting orders for {user_id}")
        return [{"order_id":"ORD-1", "total":"1500"},
                {"order_id":"ORD-1", "total":"1500"}]

class APIGateway:
    def __init__(self):
        self.__user_service = UserService()
        self.__order_service = OrderService()

    def login_user(self, username:str, password:str):
        self.__user_service.login(username,password)

    def get_usernames(self, userid:str):
        self.__user_service.get_user(userid)    

    def get_order(self, user_id:str):
        self.__order_service,self.get_order(user_id)

api_gateway = APIGateway()

api_gateway.login_user("Amaan", "Sak")



    

