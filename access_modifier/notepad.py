class SomKlass:
    name = "this is class"

    def get_name(self):  # public
        return self.name

    def _get_name_v2(self):  # protected
        return self.name + " v2"

    def __get_name_v3(self):  # private
        return self.name + " v3"


class OtherKlass(SomKlass):

    def task(self):
        return self.__get_name_v3()


if __name__ == '__main__':
    instance = OtherKlass()

    print(instance.get_name())  # public

    print(instance._get_name_v2())  # protected

    print(instance.task())

    # print(instance.__get_name_v3())  # private
