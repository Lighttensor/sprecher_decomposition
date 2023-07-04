# author Tensor
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

class SPRECHER_ksi:
    def __init__(self):
        pass
    
    @staticmethod
    def d_k_decomposition(d_k, k, gamma):
        dk = d_k * gamma ** k
        d_k_array = []

        for i in range(k):
            d_k_array.append(int(dk % gamma))
            dk //= gamma

        return d_k_array[::-1]
    
    @staticmethod
    def alpha_p(n, gamma):
        if n == 1:
            return 1
        else:
            alpha_p = 0
            for r in range(1, 1000):
                for p in range(2, n + 1):
                    alpha_p += gamma ** (-(p - 1)*(((n ** r) -1) // (n - 1)))
            return alpha_p
    
    @staticmethod
    def i_comma_round(counter, gamma):
        if counter < 2:
            return 0
        else:
            if counter == gamma - 1:
                return 1
            else:
                return 0
    
    @staticmethod
    def i_comma_square(counter, gamma):
        if counter < 2:
            return 0
        else:
            if counter == gamma - 1 or counter == gamma - 2:
                return 1
            else:
                return 0
    
    @staticmethod
    def i_tilda(counter, gamma):
        if counter < 2:
            return 0
        if counter < gamma - 1:
            return counter
        else:
            return 1
    
    @staticmethod
    def m_r_calc(counter_arr, counter, k, gamma):
        result = 1
        for s in counter_arr:
            result *= SPRECHER_ksi.i_comma_square(s, gamma)
        return SPRECHER_ksi.i_comma_round(counter, gamma) * (1 + result)
    
    def ksi_decomposition(self, d_k, gamma, k, n):
        d_k_decompose = SPRECHER_ksi.d_k_decomposition(d_k, k, gamma)
        ksi = 0
        if gamma - 1 in d_k_decompose:
            index = d_k_decompose.index(gamma - 1)
            d_k_decompose[index] -= 1
            for i in range(len(d_k_decompose)):
                if d_k_decompose[i] != gamma - 1:
                    d_k_decompose[i] += 1
        for r in range(k):
            ksi += d_k_decompose[r] / gamma ** ((n**(r + 1) - 1) / (n - 1))
        return ksi
    
    @staticmethod
    def subtract_lists(list1, list2):
        if len(list1) != len(list2):
            return None
        result = []
        for i in range(len(list1)):
            result.append(list1[i] - list2[i])
        return result
