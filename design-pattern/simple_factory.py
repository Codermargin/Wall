import abstract
from abc import ABCMeta, abstractmethod

class Payment:
    def pay(self, num):
        print('支付 ', num, ' 元')

    pass


class AliPay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, num):
        if self.use_huabei:
            print('花呗支付%d元' % num)
        else:
            print('支付宝', '支付', num, '元')


class WeChatPay(Payment):
    def pay(self, num):
        print('微信', '支付', num, '元')

class BankPay(Payment):
    def pay(self, num):
        print('银行卡', '支付', num, '元')


# 反复创建非常麻烦，产品一多就不行
class PayFactory:
    # @abstract
    # def getPayment(self):
    #     pass

    def create_payment(self, function):
        if (function == '支付宝'):
            return AliPay()
        elif (function == '微信'):
            return WeChatPay()
        elif (function == '花呗'):
            return AliPay(use_huabei=True)
        else:
            raise TypeError("No such payment named %s" % function)


# 抽象工厂方式
# 缺点 ： 每加一个具体产品类，就必须增加一个相应的具体工厂类
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AliPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WeChatFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(use_huabei=True)

class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


if __name__ == "__main__":
    factory = HuabeiFactory()
    pm = factory.create_payment()
    pm.pay(200)
