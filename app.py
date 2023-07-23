from flask import Flask, render_template, request

import openai

# Load your API key from an environment variable or secret management service
openai.api_key = '' #abstracted

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    email = request.form['email']

    prompt = "Generate only Strict one Word i.e. 'Accepted' or 'Rejected' for the following Emails applying for Job based on their tone and length of email in terms of professionalism (short mails do not get considered).\n Email: "
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt + email, temperature=0, max_tokens=20)
    text = response['choices'][0]['text']

    if (text.find("Rejected") != -1):
        result = "Rejected"
    else:
        result = "Accepted"

    return render_template('result.html', email=email, result=result)

if __name__ == '__main__':
    app.run()
