# Resume Scanning Application

This repository hosts a Resume Scanning Application that utilizes the Grmini API to analyze resumes against job descriptions. The application provides a selection percentage and suggests improvements to enhance the alignment between the resume and the desired job profile.

## Project Overview

In today's competitive job market, having a well-tailored resume can make all the difference. This application aims to simplify the job application process by scanning resumes and comparing them to job descriptions, helping users identify key areas for improvement.

## Key Features

- **Grmini API Integration**: Leverages the Grmini API for robust resume scanning, ensuring accurate analysis of qualifications and skills.
- **Job Description Matching**: Compares the scanned resume with the provided job description to calculate a selection percentage.
- **Actionable Suggestions**: Generates tailored recommendations on modifications to improve resume alignment with the job requirements.
- **User-Friendly Interface**: Designed for ease of use, allowing users to upload resumes and job descriptions seamlessly.

## Technologies Used

- Python
- Grmini API
- Flask (or relevant framework for the web interface)
- HTML/CSS (for the front end)

## Getting Started

To get started with this project, clone the repository and follow the installation instructions. Detailed guidelines are provided for setting up the application and using its features.

## Contributing

Contributions are welcome! If you have ideas for enhancements or new features, please open an issue or submit a pull request.

---


# How to run?
### STEPS:

Clone the repository

```bash / CMD
Project repo: https://github.com/Manav446/Source-Code_Analysis_Using_Gen_AI.git
```
### STEP 01- Create a conda environment after opening the repository

```bash / CMD
conda create -n llmapp python=3.8 -y
or you below command
python -m venv <envirnoment_name>
```

```bash / CMD
conda activate <envirnoment_name>
or
<envirnoment_name>\Scripts\activate 
```


### STEP 02- install the requirements
```bash / CMD
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your GEMINI_API_KEY credentials as follows:

```ini
GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash / CMD
# Finally run the following command
python app.py
```

Now,
```bash / CMD
open up localhost:
```

### I have utilized the Google Gemini Open Source API for this project. However, you can choose to use any API that suits your needs, including the OpenAI API or Hugging Face models.
