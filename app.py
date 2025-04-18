from flask import Flask, jsonify
import random
import os
import socket

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_numbers():
    # Generate 100 random numbers
    random_numbers = [random.randint(1, 1000) for _ in range(100)]
    
    # Add the pod and node information
    pod_name = os.environ.get('HOSTNAME', 'unknown')
    node_name = socket.gethostname()
    
    return jsonify({
        'numbers': random_numbers,
        'pod': pod_name,
        'node': node_name
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)