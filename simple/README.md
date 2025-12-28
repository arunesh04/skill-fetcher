# Career Skills Analyzer

A simple command-line tool to get the top 10 essential skills for various careers using the Groq API.

## Prerequisites

- Python 3.7 or higher
- Groq API key

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Groq API key as an environment variable:
```bash
export GROQ_API_KEY='your-api-key'
```

## Usage

Run the script:
```bash
python career_skills.py
```

The script will:
1. Display a list of available careers
2. Prompt you to select a career by entering its number
3. Fetch and display the top 10 essential skills for that career

## Example

```
==================================================
Career Skills Analyzer
==================================================

==================================================
Available Careers:
==================================================
1. Software Engineer
2. Data Scientist
3. Product Manager
4. UX Designer
5. DevOps Engineer
6. Machine Learning Engineer
7. Full Stack Developer
8. Cybersecurity Analyst
9. Cloud Architect
10. Data Analyst
==================================================

Select a career (1-10): 1

Fetching skills for: Software Engineer
Please wait...

==================================================
Top 10 Essential Skills for Software Engineer:
==================================================
[Skills will be displayed here]
==================================================
```

