import pandas as pd
import numpy as np
from apyori import apriori
class Recommender:
    resultsinDataFrame = []
    def __init__(self) -> None:
        data = pd.read_csv('C:/Users/91773/OneDrive/Documents/bhaa/shop/newdataset.csv')
        transactions = []
        for i in range(0, 82):
            transactions.append([str(data.values[i,j]) for j in range(0, 5)])
        rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)
        results = list(rules)
        def inspect(results):
            lhs         = [tuple(result[2][0][0])[0] for result in results]
            rhs         = [tuple(result[2][0][1])[0] for result in results]
            supports    = [result[1] for result in results]
            return list(zip(lhs, rhs, supports))
        self.resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])
        
    def recommend(self,dish):
        recommended = []
        for row in self.resultsinDataFrame.iterrows():
            if row[1]['Product 1'] == dish:
                recommended.append(row[1]['Product 2'])
            if row[1]['Product 2'] == dish:
                recommended.append(row[1]['Product 1'])
        return(recommended)


