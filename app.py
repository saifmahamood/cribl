from flask import Flask, jsonify, request
from log_reader import fetch_logs

app = Flask(__name__)

@app.route('/logs', methods=['GET'])
def get_logs():
    filename = request.args.get('filename')
    keyword = request.args.get('keyword', '')  # Optional keyword filtering
    num_lines = int(request.args.get('n', 10))  # Default to 10 lines

    try:
        logs = fetch_logs(filename, keyword, num_lines)
        return jsonify({'logs': logs}), 200
    except FileNotFoundError:
        return jsonify({'error': 'Log file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
