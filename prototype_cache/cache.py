from prototype_cache.prototype import Prototype


class Cache:
    def __init__(self):
        print(":::::::::::::::::::::¯\(ツ)/¯:::::::::::::::::::::\n"
              "::::::Init cache repository::::::\n::::::::::::::::::::::::::::::::::::::::::::::")
        self.memory = []

    def add_item(self, id_prototype, prototype: Prototype):
        item = {"id": id_prototype, "prototype": prototype}
        self.memory.append(item)
        print(":::::::::::::::::::::¯\(ツ)/¯:::::::::::::::::::::\n"
              "::::::added in memory cache::::::\n:::::::::::::::::::::::::::::::::::::::::::::::\n".upper())

    def get_item_by_name(self, key):
        for item in self.memory:
            if key == item["id"]:
                print(":::::::::::::::::::::¯\(ツ)/¯:::::::::::::::::::::\n"
                      "::::::Found in memory cache::::::\n:::::::::::::::::::::::::::::::::::::"
                      "::::::::::::::::::::::::::::::::\n".upper())
                return item["prototype"].clone()
