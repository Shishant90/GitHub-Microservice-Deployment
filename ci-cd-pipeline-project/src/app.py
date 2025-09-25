from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return jsonify({
        "name": "Shishant Kanojia",
        "project": "CI/CD Pipeline Demo",
        "description": "A complete DevOps pipeline with Flask, Docker, Kubernetes, Terraform, and Ansible",
        "features": ["Automated Testing", "Containerization", "Infrastructure as Code", "Configuration Management"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "message": "Application is running successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)