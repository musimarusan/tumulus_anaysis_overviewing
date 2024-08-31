import sys
import os
import pandas as pd


def main(path: str):

    Train_True  = f'{path}/Train/TRUE'
    Train_False = f'{path}/Train/FALSE'
    Test_True   = f'{path}/Test/TRUE'
    Test_False  = f'{path}/Test/FALSE'

        
    
    # Train
    train_true  = os.listdir(Train_True)
    df_tr_true = pd.DataFrame(train_true, columns=['file_name'])
    df_tr_true['flag'] = 1

    train_false = os.listdir(Train_False)
    df_tr_false = pd.DataFrame(train_false, columns=['file_name'])
    df_tr_false ['flag'] = 0

    df = pd.concat([df_tr_true, df_tr_false])

    csv = f'{path}/train_data.csv'
    df.to_csv(csv)

    # Test
    test_true  = os.listdir(Test_True)
    df_te_true = pd.DataFrame(test_true, columns=['file_name'])
    df_te_true['flag'] = 1

    test_false = os.listdir(Test_False)
    df_te_false = pd.DataFrame(test_false, columns=['file_name'])
    df_te_false ['flag'] = 0

    df = pd.concat([df_te_true, df_te_false])

    csv = f'{path}/test_data.csv'
    df.to_csv(csv)
    

if __name__ == "__main__":
    path = sys.argv[1]


    print(f'processing path = {path}')

    main(path)
