#!/usr/bin/env python3
"""
Flask Application for Career Skills Analysis using Groq API
A demonstration of prompt engineering with Groq Cloud API
"""

import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
def get_groq_client():
    """Initialize and return Groq client"""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    return Groq(api_key=api_key)


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/career-skills', methods=['POST'])
def get_career_skills():
    """API endpoint to get top 10 skills for a selected career"""
    try:
        data = request.get_json()
        career = data.get('career', '').strip()
        
        if not career:
            return jsonify({'error': 'Career is required'}), 400
        
        # Create prompt for Groq API
        prompt = f"""List the top 10 essential skills required for a career in {career}. 
For each skill, provide a brief one-sentence explanation of why it's important. 
Format the response as a numbered list (1-10) with clear, concise descriptions."""
        
        # Call Groq API
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
        
        response = chat_completion.choices[0].message.content
        
        return jsonify({
            'success': True,
            'career': career,
            'skills': response
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'Error calling Groq API: {str(e)}'}), 500


if __name__ == '__main__':
    # Check if API key is set
    if not os.environ.get("GROQ_API_KEY"):
        print("Warning: GROQ_API_KEY environment variable is not set.")
        print("Please set it using: export GROQ_API_KEY='your-api-key'")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
