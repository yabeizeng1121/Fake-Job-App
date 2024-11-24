# Fake Job Posting Detection App

Author: Yabei Zeng

This project is a Streamlit-based web application designed to predict whether a given job posting is real or fake. It leverages a machine learning model trained using scikit-learn on a dataset of job postings, and deployed through Streamlit for ease of access and interactivity.

---
## **Features**
- Accepts job descriptions as input from users.
- Predicts whether the job posting is real or fake using a pre-trained machine learning model.
- Simple, user-friendly interface built with Streamlit.
- Provides real-time results for entered job descriptions.

---

## **Project Structure**

```markdown
alternativedata/ 
├── app.py # Streamlit app script 
├── model.pkl # Pre-trained machine learning model ├── requirements.txt # Python dependencies 
├── README.md 
├── New_alternative_data.ipynb # model training
├── function.zip # packaged model and dependencies
├── README.md 
```


---

## **How It Works**
1. **Text Preprocessing**:
   - The app preprocesses the input job description (converts to lowercase, removes digits and punctuation).
2. **TF-IDF Vectorization**:
   - Converts the text data into numerical form using TF-IDF (Term Frequency-Inverse Document Frequency).
3. **Classification**:
   - The app uses a pre-trained Support Vector Machine (SVM) model to classify the job as `Real` or `Fake`.

---

## **Dataset**
- **Dataset Name**: [Fake and Real Job Postings Dataset](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction)
- **Dataset Description**: The dataset consists of job postings labeled as either real or fake, along with various features such as:
  - `job_id`
  - `title`
  - `location`
  - `department`
  - `salary_range`
  - `company_profile`
  - `description`
  - `requirements`
  - `benefits`
  - `telecommuting`
  - `has_company_logo`
  - `has_questions`
  - `employment_type`
  - `required_experience`
  - `required_education`
  - `industry`
  - `function`
  - `fradulent`
- **Dataset Size**: 17,880 job postings.
- **Target Variable**: `fraudulent` (1 = Fake, 0 = Real).

---

## **Model Details**
- **Model Used**: Support Vector Machine (SVM) with a linear kernel.
- **Feature Engineering**:
  - Combined text features (`title`, `company_profile`, `description`, `requirements`, `benefits`) into a single feature called `combined_text`.
  - Vectorized text using `TfidfVectorizer` (max features = 5000, stop words = English).
- **Training**:
  - Dataset was split into training and testing sets (80:20 split).
  - Applied SMOTE (Synthetic Minority Oversampling Technique) to handle the class imbalance in the training set.
- **Performance**:
  - Achieved an F1-score of **0.83** for the minority class (`Fake`) on the test set.

---

## **Setup Instructions**

### **Local Deployment**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your_username>/<your_repository_name>.git
   cd <your_repository_name>
   ```

2. **Set Up Virtual Environment (not required)**:  
   ```bash
   python -m venv env 
   source env/bin/activate
   ```
 

3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**:  
   ```bash
   streamlit run app.py
   ```  

   Open the local URL provided in the terminal (e.g., `http://localhost:8501`) to access the app.

---

### **Streamlit Cloud Deployment**
1. Push your project to a GitHub repository.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app by linking your GitHub repository.
4. Specify `app.py` as the entry point and deploy the app.
5. Once deployed, access the app using the public URL provided by Streamlit Cloud.

---

### **Usage**
1. Enter a job description in the provided text box.
2. Click the **"Predict"** button.
3. The app will display whether the job posting is **Real** or **Fake**.

---

### **Dependencies**
The following Python libraries are required to run this project:

- `streamlit`  
- `scikit-learn`  
- `joblib`  
- `numpy`  
- `pandas`  

Install them using:  
```bash
pip install -r requirements.txt
```

---
### Live App

Check out the live app here: [Fake Job Prediction App](https://fakejobprediction.streamlit.app/)

---

### **Example Job Description for Testing**
You can use the following example to test the app:  

`"We are currently seeking highly motivated individuals to join our remote team as Administrative Data Entry Specialists. In this role, you will assist our clients by managing and inputting critical data into various systems, ensuring accuracy and efficiency. No prior experience is required, as we provide all necessary training!Title: Remote Administrative Data Entry Specialist"`

---

### **Future Enhancements**
- Add support for batch predictions by uploading CSV files.
- Implement visualization of feature importance for better explainability.
- Expand the app to include more insights about fake job postings.

