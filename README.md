# Solar-Challange-Week0
Solar Data Explorer - Quick Setup
Requirements

Python 3.10 or higher

pip

Install dependencies
pip install streamlit pandas matplotlib seaborn


Alternatively, if you have a requirements.txt:

pip install -r requirements.txt

Run the app
streamlit run app/main.py


Open your browser at: http://localhost:8501

Upload your CSV files when prompted or use default data (if included).

Example Usage
Load Dataset:
import pandas as pd

benin_df = pd.read_csv('data/benin.csv')
print(benin_df.head())

Plot GHI Time Series:
import matplotlib.pyplot as plt

plt.plot(benin_df['timestamp'], benin_df['GHI'])
plt.title('GHI Over Time - Benin')
plt.xlabel('Date')
plt.ylabel('GHI (W/m^2)')
plt.show()

Launch Dashboard:
streamlit run dashboard/solar_dashboard.py

Optional

For virtual environment (recommended):

python -m venv venv

 
 Windows
venv\Scripts\activate


You can find the live app here: https://solar-challange-week0-5etmgmqfz5zfqscypodu6r.streamlit.app/

Then install dependencies inside the virtual environment.
