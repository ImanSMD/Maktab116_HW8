from core.model import Model

class User(Model):
    store = []
    
    
    def validate_username(self, username : str) -> None:
        assert isinstance(username ,str) and len(username) >= 4 , "Username must be a string and at least 4 characters long!"
        for user in self.__class__.store :
            if hasattr(user , "username"):
                assert user.username != username , "Username already exists!"
    
    @staticmethod
    def validate_password(password : str) -> None:
        assert isinstance(password , str) and len(password) >= 4 , "Password must be a string and at least 4 characters long!"
                
    def __init__(self , username :str , password : str) -> None:
        self.username = username
        self.password = password
        
        
    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self , value : str) -> None:
        self.validate_username(value)
        self.__username = value
        
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self , value : str) -> None:
        self.validate_password(value)
        self.__password = value
        

class BankAccount(Model):
    store = []
        
    def unique_validation(self , attr_name : str ,attr_value ) -> None:
         for account in self.__class__.store :
            if hasattr(account , attr_name):
                assert getattr(account ,attr_name )!= attr_value , f"Account {attr_name} already exists!"
    
    def validate_name(self, name : str) -> None:
        assert isinstance(name ,str) and len(name) >= 4 , "Name must be a string and at least 4 characters long!"
        
    def validate_account_number(self, account_number : int) -> None:
        assert isinstance(account_number , int)  and account_number > 0 , "Account number must be a string and at least 4 characters long!"
        self.unique_validation("account_number" , account_number)
        
    def validate_cart_number(self, cart_number : int) -> None:
        assert isinstance(cart_number , int) and cart_number > 0 , "Cart number must be a string and at least 4 characters long!"
        self.unique_validation("cart_number" , cart_number)
        
    def validate_balance(self, balance : int) -> None:
        assert isinstance(balance , int) and balance >= 0 , "Balance must be a string and positive!"
        
        
    def __init__(self,name:str , account_number : int, cart_number:int , balance:int ) -> None:
        self.name = name
        self.account_number = account_number
        self.cart_number = cart_number
        self.balance = balance
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self , value : str) -> None:
        self.validate_name(value)
        self.__name = value
    
    @property
    def account_number(self) -> int:
        return self.__account_number
    
    @account_number.setter
    def account_number(self , value : int) -> None:
        self.validate_account_number(value)
        self.__account_number = value
    
    @property
    def cart_number(self) -> int:
        return self.__cart_number
    
    @cart_number.setter
    def cart_number(self , value : int) -> None:
        self.validate_cart_number(value)
        self.__cart_number = value
    
        
    @property
    def balance(self) -> int:
        return self.__balance
    
    @balance.setter
    def balance(self , value : int) -> None:
        self.validate_balance(value)
        self.__balance = value

    
        


 