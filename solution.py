import pandas as pd
import numpy as np


chat_id = 5127116142 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
     return ks_2samp(x, y).pvalue < 0.1 # Ваш ответ, True или False
