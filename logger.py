# logger.py
import pandas as pd
import os
import datetime

def save_to_csv(data):
    file_name = "emotion_logs.csv"
    df = pd.DataFrame([data])
    if not os.path.exists(file_name):
        df.to_csv(file_name, index=False)
    else:
        df.to_csv(file_name, mode='a', header=False, index=False)