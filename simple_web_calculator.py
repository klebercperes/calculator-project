#!/usr/bin/env python3
"""
Simple Calculator Web App (No Dependencies)
A basic web interface for the Advanced Calculator using only built-in modules
"""

import http.server
import socketserver
import json
import urllib.parse
from calculator import Calculator
import datetime

class CalculatorHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.calculator = Calculator()
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = self.get_calculator_html()
            self.wfile.write(html_content.encode())
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/calculate':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode())
            
            operation = data.get('operation', [''])[0]
            num1 = float(data.get('num1', ['0'])[0])
            num2 = float(data.get('num2', ['0'])[0])
            
            result = self.perform_calculation(operation, num1, num2)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {'result': str(result)}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def perform_calculation(self, operation, num1, num2):
        try:
            if operation == 'add':
                return self.calculator.add(num1, num2)
            elif operation == 'subtract':
                return self.calculator.subtract(num1, num2)
            elif operation == 'multiply':
                return self.calculator.multiply(num1, num2)
            elif operation == 'divide':
                return self.calculator.divide(num1, num2)
            elif operation == 'power':
                return self.calculator.power(num1, num2)
            elif operation == 'sqrt':
                return self.calculator.square_root(num1)
            elif operation == 'modulo':
                return self.calculator.modulo(num1, num2)
            elif operation == 'factorial':
                return self.calculator.factorial(int(num1))
            elif operation == 'sin':
                return self.calculator.sine(num1)
            elif operation == 'cos':
                return self.calculator.cosine(num1)
            elif operation == 'tan':
                return self.calculator.tangent(num1)
            elif operation == 'log':
                return self.calculator.logarithm(num1, num2)
            elif operation == 'ln':
                return self.calculator.natural_log(num1)
            elif operation == 'abs':
                return self.calculator.absolute(num1)
            else:
                return "Invalid operation"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_calculator_html(self):
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .calculator-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            width: 100%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .header h1 {
            color: white;
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .header p {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1.1rem;
        }
        
        .operation-section {
            margin-bottom: 25px;
        }
        
        .operation-section h3 {
            color: white;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        
        .input-group input {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.9);
            min-width: 120px;
        }
        
        .button-group {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .calc-button {
            padding: 12px 20px;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            color: white;
        }
        
        .calc-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .result-display {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .result-display h4 {
            color: white;
            margin-bottom: 10px;
        }
        
        .result-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #ffd700;
        }
        
        .history-section {
            margin-top: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        
        .history-section h4 {
            color: white;
            margin-bottom: 15px;
        }
        
        .history-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            color: white;
            border-left: 4px solid #667eea;
        }
        
        @media (max-width: 600px) {
            .calculator-container {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .input-group {
                flex-direction: column;
            }
            
            .button-group {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="calculator-container">
        <div class="header">
            <h1>🧮 Advanced Calculator</h1>
            <p>Comprehensive mathematical operations with beautiful UI</p>
        </div>
        
        <!-- Basic Operations -->
        <div class="operation-section">
            <h3>➕ Basic Operations</h3>
            <div class="input-group">
                <input type="number" id="num1" placeholder="First number" step="any">
                <input type="number" id="num2" placeholder="Second number" step="any">
            </div>
            <div class="button-group">
                <button class="calc-button" onclick="calculate('add')">➕ Add</button>
                <button class="calc-button" onclick="calculate('subtract')">➖ Subtract</button>
                <button class="calc-button" onclick="calculate('multiply')">✖️ Multiply</button>
                <button class="calc-button" onclick="calculate('divide')">➗ Divide</button>
            </div>
        </div>
        
        <!-- Advanced Operations -->
        <div class="operation-section">
            <h3>🔢 Advanced Operations</h3>
            <div class="button-group">
                <button class="calc-button" onclick="calculate('power')">🔢 Power (a^b)</button>
                <button class="calc-button" onclick="calculate('sqrt')">√ Square Root</button>
                <button class="calc-button" onclick="calculate('modulo')">% Modulo</button>
                <button class="calc-button" onclick="calculate('factorial')">! Factorial</button>
            </div>
        </div>
        
        <!-- Trigonometric Functions -->
        <div class="operation-section">
            <h3>📐 Trigonometric Functions</h3>
            <div class="button-group">
                <button class="calc-button" onclick="calculate('sin')">sin</button>
                <button class="calc-button" onclick="calculate('cos')">cos</button>
                <button class="calc-button" onclick="calculate('tan')">tan</button>
            </div>
        </div>
        
        <!-- Logarithmic Functions -->
        <div class="operation-section">
            <h3>📊 Logarithmic Functions</h3>
            <div class="button-group">
                <button class="calc-button" onclick="calculate('log')">log</button>
                <button class="calc-button" onclick="calculate('ln')">ln</button>
                <button class="calc-button" onclick="calculate('abs')">|x| Absolute</button>
            </div>
        </div>
        
        <!-- Result Display -->
        <div class="result-display">
            <h4>Result:</h4>
            <div class="result-value" id="result">Ready to calculate!</div>
        </div>
        
        <!-- History -->
        <div class="history-section">
            <h4>📝 Recent Calculations</h4>
            <div id="history"></div>
        </div>
    </div>
    
    <script>
        let calculationHistory = [];
        
        async function calculate(operation) {
            const num1 = parseFloat(document.getElementById('num1').value) || 0;
            const num2 = parseFloat(document.getElementById('num2').value) || 0;
            
            const formData = new FormData();
            formData.append('operation', operation);
            formData.append('num1', num1);
            formData.append('num2', num2);
            
            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                document.getElementById('result').textContent = data.result;
                
                // Add to history
                const timestamp = new Date().toLocaleTimeString();
                const historyItem = {
                    operation: operation,
                    num1: num1,
                    num2: num2,
                    result: data.result,
                    timestamp: timestamp
                };
                
                calculationHistory.unshift(historyItem);
                if (calculationHistory.length > 10) {
                    calculationHistory.pop();
                }
                
                updateHistory();
                
            } catch (error) {
                document.getElementById('result').textContent = 'Error: ' + error.message;
            }
        }
        
        function updateHistory() {
            const historyDiv = document.getElementById('history');
            historyDiv.innerHTML = '';
            
            calculationHistory.forEach(item => {
                const historyItem = document.createElement('div');
                historyItem.className = 'history-item';
                historyItem.innerHTML = `
                    <strong>${item.operation}</strong>: ${item.num1}, ${item.num2} = <strong>${item.result}</strong><br>
                    <small>${item.timestamp}</small>
                `;
                historyDiv.appendChild(historyItem);
            });
        }
        
        // Clear inputs on page load
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('num1').value = '';
            document.getElementById('num2').value = '';
        });
    </script>
</body>
</html>
        """

def run_server(port=8000):
    """Run the calculator web server"""
    handler = CalculatorHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🧮 Advanced Calculator Web App")
        print(f"🌐 Server running at http://localhost:{port}")
        print(f"📱 Access from other devices: http://your-ip:{port}")
        print(f"🛑 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Calculator server stopped. Goodbye!")

if __name__ == "__main__":
    run_server()