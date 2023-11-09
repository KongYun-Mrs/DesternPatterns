
class Phone():
    def operation():
        pass

class XiaoMiPhone(Phone):
    def operation(self):
        return "XiaoMiPhone"

class Iphone(Phone):
    def operation(self):
        return "Iphone"


class CreatePhoneFactory:
    @staticmethod
    def create_phone(phone_type:str) ->str:
        if phone_type=="xiaomi":
            return XiaoMiPhone()
        elif phone_type=="Iphone":
            return Iphone()
        else:
            raise ValueError("Invaild product")

if __name__ == "__main__":
    # 客户端代码
    product_a = CreatePhoneFactory.create_phone("xiaomi")
    product_b = CreatePhoneFactory.create_phone("Iphone")

    print(product_a.operation())  
    print(product_b.operation())  
    

