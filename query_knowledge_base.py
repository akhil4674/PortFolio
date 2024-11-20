import json

def load_knowledge_base(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error in {file_path}: {e}")
        return {}  # or handle appropriately for your applicatio
def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def query_knowledge_base(knowledge_base, query):
    query = query.lower()
    if "name" in query:
        return knowledge_base["name"]
    elif "bio" in query:
        return knowledge_base["bio"]
    elif "education" in query:
        return "\n".join([f"{edu['institution']} - {edu['degree']} ({edu['duration']})" for edu in knowledge_base["education"]])
    elif "work experience" in query or "job" in query:
        return "\n".join([f"{exp['company']} as {exp['position']} ({exp['duration']}) - {exp['brief_description']}" for exp in knowledge_base["work_experience"]])
    elif "skills" in query:
        return ", ".join(knowledge_base["skills"])
    elif "interests" in query:
        return ", ".join(knowledge_base["interests"])
    elif "contact" in query or "email" in query or "linkedin" in query or "github" in query:
        if "email" in query:
            return knowledge_base["contact"]["email"]
        elif "linkedin" in query:
            return knowledge_base["contact"]["linkedin"]
        elif "github" in query:
            return knowledge_base["contact"]["github"]
        else:
            return "\n".join([f"{key}: {value}" for key, value in knowledge_base["contact"].items()])
    else:
        return "Sorry, couldn't find a match for your query in my knowledge base."

def main():
    knowledge_base = load_knowledge_base('personal_knowledge_base.json')
    while True:
        user_query = input("Ask me something about myself (or 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break
        print(query_knowledge_base(knowledge_base, user_query))

if __name__ == "__main__":
    main()
