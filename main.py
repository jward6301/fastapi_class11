from fastapi import FastAPI
import panda as pd

df = pd.read_csv('./data/diagnoses.csv')

app = FastAPI()


@app.get('/')
def home():
    return 'this is a API service for MN ICD code details'


@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result


@app.get('/icd/{value}') 
async def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")


@app.get('/icd/{value}/sex/{value2}') 
async def icdcode2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records") 