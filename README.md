# Resume Parser

A Python script that parses resume text and converts it into JSON format. This tool is designed to streamline the process of extracting structured data from plain text resumes, making it easier to analyze and utilize resume information programmatically.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
The Resume Parser is a simple yet powerful tool designed to convert unstructured resume text into a structured JSON format. This tool is especially useful for developers working on HR tech solutions, such as applicant tracking systems (ATS), job boards, or resume databases.

## Features
- Extracts key information from resumes including personal details, education, skills, projects, experience, interests, and requirements.
- Outputs structured JSON data for easy integration with other systems and applications.
- Simple and easy-to-use Python script.

## Requirements
- Python 3.6 or higher
- Pandas (for any additional data handling if needed)

## Installation
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Jaishree2310/resume-parser.git
   cd resume-parser
   ```

2. **Create and Activate a Virtual Environment**:
   - On Windows:
     ```sh
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```sh
   pip install pandas
   ```

## Usage
1. **Edit the `resume_parser.py` File**:
   Replace the sample resume text with the resume text you want to parse.

2. **Run the Script**:
   ```sh
   python resume_parser.py
   ```

3. **View the Output**:
   The parsed resume will be printed in JSON format in the terminal.

## Example Output
Here's an example of the JSON output generated by the script:

```json
{
  "name": "Jaishree Singh",
  "email": "jaishree.singh@example.com",
  "phone": "+91-12345-67890",
  "linkedin": "linkedin.com/in/jaishree-singh",
  "github": "github.com/jaishreesingh",
  "education": [
    {
      "Bachelor of Engineering in Computer Engineering": "Mumbai University, 2023"
    }
  ],
  "skills": [
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Next.js",
    "Node.js",
    "Angular",
    "MongoDB",
    "API Development",
    "React.js",
    "Git",
    "GitHub"
  ],
  "projects": [
    {
      "Social Media Resizer Tool": "Developed a tool to resize images for social media platforms."
    },
    {
      "Automated Note Maker": "Created a project that converts audio/video into downloadable PDF/Word documents."
    }
  ],
  "experience": [
    {
      "Frontend Developer Intern at XYZ Corp": "Jan 2022 - Dec 2022"
    }
  ],
  "interests": [
    "Open-source technology",
    "UI/UX design",
    "Software engineering",
    "Conversational AI"
  ],
  "requirements": [
    "Candidates graduating in 2024 or 2025 can apply. Candidates should commit for at least 6 months of internship.",
    "Candidates should have strong Python skills, have built ML/NLP solutions before. Candidates should have experience working with LLMs mainly in Prompt Engineering or LLM tools i.e LangChain, LLamaIndex."
  ]
}
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or suggestions, feel free to reach out to the project maintainer:
- Jaishree Singh
- Email: jaishree.singh@example.com
- LinkedIn: [linkedin.com/in/jaishree-singh](https://linkedin.com/in/jaishree-singh)
