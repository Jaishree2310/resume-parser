import json

resume_text = """
Name: Jaishree Singh
Email: jaishree.singh@gmail.com
Phone: +91-12345-67890
LinkedIn: linkedin.com/in/jaishree-singh
Github: github.com/jaishreesingh

Education:
- Bachelor of Engineering in Computer Engineering, Mumbai University, 2024

Skills:
- HTML, CSS, JavaScript, React, Next.js, Node.js, Angular
- MongoDB, API Development, React.js, Git, GitHub

Projects:
- Social Media Resizer Tool: Developed a tool to resize images for social media platforms.
- Automated Note Maker: Created a project that converts audio/video into downloadable PDF/Word documents.

Experience:
- Frontend Developer Intern at XYZ Corp, Jan 2022 - Dec 2022

Requirements:
- Candidates graduating in 2024 or 2025 can apply. Candidates should commit for at least 6 months of internship.
- Candidates should have strong Python skills, have built ML/NLP solutions before. Candidates should have experience working with LLMs mainly in Prompt Engineering or LLM tools i.e LangChain, LLamaIndex.

Interests:
- Open-source technology
- UI/UX design
- Software engineering
- Conversational AI
"""

def parse_resume(text):
    lines = text.strip().split('\n')
    resume = {}
    current_section = None
    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            current_section = line[:-1].lower()
            resume[current_section] = []
        elif current_section:
            if '- ' in line:
                item = line.split('- ', 1)[1]
                if current_section in ['education', 'projects', 'experience']:
                    if ': ' in item:
                        key, value = item.split(': ', 1)
                        resume[current_section].append({key: value})
                    else:
                        resume[current_section].append(item)
                else:
                    resume[current_section].append(item)
            else:
                resume[current_section].append(line)
    return resume

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=4))
