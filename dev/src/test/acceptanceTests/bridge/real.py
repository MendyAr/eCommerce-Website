import string

from dev.src.test.acceptanceTests.bridge.Bridge import Bridge
from dev.src.main.Market.Market import Market
from dev.src.main.Service.IService import IService
from dev.src.main.Utils.Session import Session
from typing import Tuple
from dev.src.main.Utils.Response import Response


class real(Bridge):
    market: Market
    user_sessions: list[int]
    user_counter: int

    def __init__(self):
        self.user_sessions = []
        self.market = Market()
        self.user_counter = 0

    def enter_market(self) -> int:
        s = self.market.enter()
        self.user_sessions.append(s.identifier)
        return s.identifier

    def register(self, session_id: int, username: string, password: string) -> bool:
        r = self.market.register(session_id, username, password)
        return r.result

    def exit_market(self, session_id: int) -> bool:
        return self.market.exit_market(session_id).result

    def login(self, session_id: int, username: string, password: string) -> bool:
        res = self.market.login(session_id, username, password)
        return res.result

    def open_store(self, session_id: int, store_name: string) -> bool:
        return self.market.open_store(session_id, store_name).success

    # guest buying operations
    def get_all_stores(self, session_id) -> list:
        res = self.market.get_all_stores(session_id)
        if res.success:
            return res.result.split(", ")
        else:
            return []

    def get_store_products(self, session_id: int, store_id: int) -> list:
        return []

    def get_products_by_name(self, session_id: int, name: string) -> list:
        return []

    def get_products_by_category(self, session_id: int, name: string) -> list:
        return []

    def get_products_by_keyword(self, session_id: int, name: string) -> list:
        return []

    ##quesion??????????????????????????????????????????????????
    def filter_products_by_price_range(self, session_id: int, low: int, high: int) -> list:
        return []

    def filter_products_by_rating(self, session_id: int, low: int, high: int):
        return []

    def filter_products_by_category(self, session_id: int, category: string):
        return []

    def filter_products_by_store_rating(self, session_id: int, low: int, high: int):
        return []

    ##quesion??????????????????????????????????????????????????

    def add_to_cart(self, session_id: int, store_name: string, product_name: string, quantity: int) -> bool:
        return True

    def buy_cart(self, session_id: int,) -> bool:
        return True

    # registered user operations
    def logout(self, session_id: int,) -> bool:
        return True

    # storeOwner operations
    def add_product(self, session_identifier: int, store_name: str, product_name: str, category: str,
                    price: float, quantity: int, keywords: list[str]) -> bool:
        return True

    def remove_product(self, session_id: int, store_id: int, product_id: int, amount: int) -> bool:
        return True

    def change_product_name(self, session_id: int, store_id: int, product_id: int, new_name: string) -> bool:
        return True

    def change_product_price(self, session_id: int, store_id: int, product_id: int, new_price: int) -> bool:
        return True

    def appoint_owner(self, session_id: int, store_id: int, new_owner: string) -> bool:
        return True

    def appoint_manager(self, session_id: int, store_id: int, new_owner: string) -> bool:
        return True

    # TODO: 4.7: permissions of store manager

    def close_store(self, session_id: int, store_id: int) -> bool:
        return True

    def get_store_personal(self, session_id: int, store_id) -> list:
        return []

    def get_store_purchase_history(self, session_id: int, store_id) -> list:
        return []

    def show_cart(self, session_id: int) -> list:
        return []
