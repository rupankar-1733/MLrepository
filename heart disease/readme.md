❤️ Heart Disease Prediction App

This project is an interactive web application that predicts the likelihood of heart disease based on patient health data. It is built using Streamlit and uses a trained Random Forest classifier, selected after testing multiple machine learning models via 5-fold cross-validation.

🔍 Features
Predicts heart disease risk based on key medical parameters.

Easy-to-use UI for patient data input.

Provides probability-based risk feedback.

Built with clean UI using custom CSS styling.

Model performance compared with Logistic Regression, KNN, SVM, XGBoost, and Gradient Boosting.

🧠 Models Compared
The following models were tested and evaluated based on cross-validated accuracy:

Logistic Regression

Random Forest ✅ (Selected model)

Gradient Boosting

XGBoost

K-Nearest Neighbors (KNN)

Linear SVC

(Refer to the bar_plot.jpeg for visual accuracy comparison.)

📸 App Screenshot



📂 Files Included
app.py: Streamlit application code

heart-disease.csv: Dataset used for training/testing

best_rf_model.pkl: Trained Random Forest model (should be added for full functionality)

bar_plot.jpeg: Model accuracy bar plot

Screen_font.png: App screenshot

▶️ How to Run Locally
Clone the repo:

git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Make sure the file best_rf_model.pkl is in the same directory as app.py.

🌐 How to Keep Streamlit App Always Running
To make your app publicly accessible and always online:

Option 1: Deploy on Streamlit Community Cloud
Push your code to GitHub.

Go to Streamlit Cloud and connect your GitHub repo.

Deploy with a single click. It will stay live as long as it receives some traffic periodically.

Option 2: Use a cloud provider (for advanced users)
Deploy on:

Render

Heroku

Google Cloud Run

AWS EC2

These options require setting up persistent servers, so they are more involved but offer more control.

📊 Dataset
The dataset (heart-disease.csv) includes:

Age, Sex, Chest pain type

Cholesterol, Blood pressure

ECG results, ST depression

Max heart rate, Thalassemia, etc.

This data is typically derived from the UCI Heart Disease Dataset or similar sources.

📌 Future Improvements
Allow upload of CSVs for batch predictions

Save patient results for historical tracking

Add SHAP or feature importance plots for model interpretability

🙌 Credits
Developed by Rupankar Mondal
Built with ❤️ using Machine Learning & Streamlit
