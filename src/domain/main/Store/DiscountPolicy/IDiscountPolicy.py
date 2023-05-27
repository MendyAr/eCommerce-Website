from abc import ABC, abstractmethod

from domain.main.User.Basket import Basket


class IDiscountPolicy(ABC):
    @abstractmethod
    def calculate_proce(self, basket: Basket):
        ...