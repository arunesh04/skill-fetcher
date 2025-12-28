#!/usr/bin/env python3
"""
Simple CLI script for Career Skills Analysis using Groq API
A terminal-based version of the Flask app
"""

import os
from groq import Groq

# List of careers to choose from
CAREERS = [
    "Software Engineer",
    "Data Scientist",
    "Product Manager",
    "UX Designer",
    "DevOps Engineer",
    "Machine Learning Engineer",
    "Full Stack Developer",
    "Cybersecurity Analyst",
    "Cloud Architect",
    "Data Analyst"
]


def get_groq_client():
    """Initialize and return Groq client"""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    return Groq(api_key=api_key)


def display_career_list():
    """Display the list of available careers"""
    print("\n" + "="*50)
    print("Available Careers:")
    print("="*50)
    for idx, career in enumerate(CAREERS, start=1):
        print(f"{idx}. {career}")
    print("="*50 + "\n")


def get_user_selection():
    """Get career selection from user"""
    while True:
        try:
            choice = input(f"Select a career (1-{len(CAREERS)}): ").strip()
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(CAREERS):
                return CAREERS[choice_num - 1]
            else:
                print(f"Please enter a number between 1 and {len(CAREERS)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            exit(0)


def get_career_skills(career):
    """Get top 10 skills for the selected career using Groq API"""
    prompt = f"""List the top 10 essential skills required for a career in {career}. 
For each skill, provide a brief one-sentence explanation of why it's important. 
Format the response as a numbered list (1-10) with clear, concise descriptions."""
    
    client = get_groq_client()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=800
    )
    
    return chat_completion.choices[0].message.content


def main():
    """Main function"""
    print("\n" + "="*50)
    print("Career Skills Analyzer")
    print("="*50)
    
    # Check if API key is set
    if not os.environ.get("GROQ_API_KEY"):
        print("\nError: GROQ_API_KEY environment variable is not set.")
        print("Please set it using: export GROQ_API_KEY='your-api-key'")
        return
    
    try:
        # Display career list and get user selection
        display_career_list()
        selected_career = get_user_selection()
        
        print(f"\nFetching skills for: {selected_career}")
        print("Please wait...\n")
        
        # Get skills from Groq API
        skills = get_career_skills(selected_career)
        
        # Display results
        print("="*50)
        print(f"Top 10 Essential Skills for {selected_career}:")
        print("="*50)
        print(skills)
        print("="*50 + "\n")
        
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nError calling Groq API: {str(e)}")


if __name__ == '__main__':
    main()

