class Inventory_m:
    def __init__(self, id="", name="", category="", qty="", mrp="", cost="", ph=""):
        self.__id = id
        self.__name = name
        self.__category = category
        self.__qty = qty
        self.__mrp = mrp
        self.__cost = cost
        self.__ph = ph

    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_category(self, category):
        self.__category = category
    def set_qty(self, qty):
        self.__qty = qty
    def set_mrp(self, mrp):
        self.__mrp = mrp
    def set_cost(self, cost):
        self.__cost = cost
    def set_ph(self, ph):
        self.__ph = ph

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_category(self):
        return self.__category
    def get_qty(self):
        return self.__qty
    def get_mrp(self):
        return self.__mrp
    def get_cost(self):
        return self.__cost
    def get_ph(self):
        return self.__ph

