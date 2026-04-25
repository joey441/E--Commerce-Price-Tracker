import os
import pandas as pd
def save_to_tracker(product_data,filename='price_tracker.csv'):
    # If file doesn't exist, write with header. If it does, append without
    df = pd.DataFrame([product_data])
    file_exists=os.path.isfile(filename)
    df.to_csv(filename, mode='a', header=not file_exists, index=False)
    print(f'Successfully saved data to {filename}')