import numpy as np

class Transaction():
    time, amount = 0 , 0
    v1, v2, v3, v4, v5 = 0, 0 , 0, 0, 0
    v6, v7, v8, v9, v10 = 0, 0 , 0, 0, 0
    v11, v12, v13, v14, v15 = 0, 0 , 0, 0, 0
    v16, v17, v18, v19, v20 = 0, 0 , 0, 0, 0
    v21, v22, v23, v24, v25 = 0, 0 , 0, 0, 0
    v26, v27, v28 = 0, 0 , 0

    def __init__(self, time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, 
        v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount):  
        self.time, self.amount = time , amount
        self.v1, self.v2, self.v3, self.v4, self.v5 = v1, v2, v3, v4, v5
        self.v6, self.v7, self.v8, self.v9, self.v10 = v6, v7, v8, v9, v10
        self.v11, self.v12, self.v13, self.v14, self.v15 = v11, v12, v13, v14, v15
        self.v16, self.v17, self.v18, self.v19, self.v20 = v16, v17, v18, v19, v20
        self.v21, self.v22, self.v23, self.v24, self.v25 = v21, v22, v23, v24, v25
        self.v26, self.v27, self.v28 = v26, v27, v28

    def get_transaction_array(self):
        data = [self.time, self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.v8, 
            self.v9, self.v10, self.v11, self.v12, self.v13, self.v14, self.v15, 
            self.v16, self.v17, self.v18, self.v19, self.v20, self.v21, self.v22, self.v23, 
            self.v24, self.v25, self.v26, self.v27, self.v28, self.amount]
        
        return np.array(data).reshape(1,-1)