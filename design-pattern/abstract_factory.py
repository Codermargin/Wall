from abc import ABC, abstractmethod


class Cpu:
    def create_cpu(self):
        pass


class Apple_Cpu(Cpu):
    def create_cpu(self):
        return 'A17 Pro'


class Huawei_Cpu(Cpu):
    def create_cpu(self):
        return 'Qilin 9000S'


class OS:
    def add_os(self):
        pass


class Apple_OS(OS):
    def add_os(self):
        return 'iOS'


class Huawei_OS(OS):
    def add_os(self):
        return 'Harmony OS'


class AbstractPhoneFactory:
    def create_cpu(self):
        pass

    def create_os(self):
        pass


class AppleFactory(AbstractPhoneFactory):
    def create_cpu(self):
        return Apple_Cpu()

    def create_os(self):
        return Apple_OS()


class HuaweiFactory(AbstractPhoneFactory):
    def create_cpu(self):
        return Huawei_Cpu()

    def create_os(self):
        return Huawei_OS()


def Create_Phone(factory):
    cpu = factory.create_cpu()
    os = factory.create_os()
    return cpu, os


if __name__ == '__main__':
    apple_factory = AppleFactory()
    cpu, os = Create_Phone(apple_factory)
    print(f'生产手机成功，CPU -> {cpu.create_cpu()}, OS -> {os.add_os()}')
