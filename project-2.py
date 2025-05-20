import random
adjectives = ["Global", "Certified", "Dynamic", "Virtual", "Strategic", "Senior", "Quantum", "Elite"]
roles = ["Meme", "Unicorn", "Synergy", "Innovation", "Vibes", "Cloud", "AI", "Nonsense"]
suffixes = ["Engineer", "Manager", "Consultant", "Specialist", "Strategist", "Evangelist", "Coordinator"]

def generate_job_title():
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    return f"{adj} {role} {suffix}"

while True:
    title = generate_job_title()
    print(f"Your fake job title is: {title}")
    
    again = input("Want another one? (yes/no): ").strip().lower()
    if again != "yes":
        print("Hope you enjoy your new career path!")
        break
    
    
    
 