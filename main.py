# import pandas as pa
# import pyarrow as py
# import boto3
# import numpy as np
# import fastparquet as fp

def my_handler(event, context):
    # my_list = [1, 2, 3, 4, 5, 6]
    # df = pa.DataFrame(np.array(my_list).reshape(2, 3), columns = list('abc'))
    # # fp.write('test.parquet', df)
    # # df.to_csv('test.csv')
    message = "Hello World!"
    # data = df
    return {
        'message': message
        # 'data': data,
        # 'event-payload': event
    }