class User:
    def __init__(self, name) -> None:
        self.name: str = name
        self.password = None
        self.total_assets: list = []
        
    def Add_To_Assets(self, order) -> None:
        self.total_assets.append(order)

    def Verify_Password(self, input):
        if input != self.password:
            return False
        return True

admin_user = User("John", "password123")

def Login():
    print(admin_user.Verify_Password("asdflkajksdfl"))