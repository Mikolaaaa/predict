import numpy as np
from sklearn.metrics import precision_score

def get_precision(targets, predictions, multioutput: bool=True, average: str=None):
    """
    возвращает precision
    
    :code_assign: service
    :code_type: Машинное обучение/Метрики
    
    :packages:
    from sklearn.metrics import precision_score
        
    параметры: целевые значения, прогнозные значения,
               флаг вывода метрики для каждого признака в виде массива или одним значением:
               True - массивом, False - одним значением,
               способ расчета метрики
    """
    
    # если бинарная классификация и нужно вывести массивом
    if average == 'binary' and multioutput:
        # возвращаем значением массивом
        return [np.round(precision_score(targets, predictions, average=average), 3)]
    
    # если average == None и нужно вывести одним значением
    if not average and not multioutput:
        average = 'macro'
    
    return np.round(precision_score(targets, predictions, average=average), 3)
