# 🧮 Advanced Calculator - Web App

A beautiful, modern web application built with Streamlit that provides all the functionality of the Python calculator with an intuitive web interface.

## ✨ Features

### 🎨 **Beautiful UI**
- Modern gradient design with glassmorphism effects
- Responsive layout that works on desktop and mobile
- Interactive charts and visualizations
- Real-time calculation history

### 🔢 **Mathematical Operations**
- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Operations**: Power, Square Root, Modulo, Factorial
- **Trigonometric Functions**: Sine, Cosine, Tangent (with angle converter)
- **Logarithmic Functions**: Logarithm (any base), Natural Logarithm
- **Other Functions**: Absolute Value

### 📊 **Analytics & History**
- Real-time calculation statistics
- Operations distribution charts
- Downloadable calculation history (CSV)
- Recent calculations display
- Most used operations tracking

### 🎛️ **User Experience**
- Sidebar navigation for different operation types
- One-click calculations
- Error handling with user-friendly messages
- Session state management
- Clear history functionality

## 🚀 Quick Start

### Option 1: Using the Launcher Script
```bash
./run_calculator.sh
```

### Option 2: Manual Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_calculator.py
```

### Option 3: Network Access
```bash
# Run with network access (accessible from other devices)
streamlit run streamlit_calculator.py --server.port 8501 --server.address 0.0.0.0
```

## 🌐 Access the App

Once running, the calculator will be available at:
- **Local**: http://localhost:8501
- **Network**: http://your-ip:8501 (if using network access)

## 📱 Mobile Friendly

The calculator is fully responsive and works great on:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Desktop computers
- 🖥️ Large screens

## 🎨 UI Components

### Main Interface
- **Operation Type Selector**: Choose between different mathematical operation categories
- **Input Fields**: Number inputs with proper validation
- **Action Buttons**: One-click calculation buttons with hover effects
- **Result Display**: Immediate feedback with success messages

### Sidebar Features
- **Navigation**: Easy switching between operation types
- **History Management**: Clear history and download options
- **Statistics**: Real-time calculation metrics

### Analytics Dashboard
- **Pie Charts**: Visual representation of operation usage
- **Metrics**: Total calculations and most used operations
- **Recent History**: Last 5 calculations with timestamps

## 🔧 Technical Details

### Built With
- **Streamlit**: Web framework for Python
- **Plotly**: Interactive charts and visualizations
- **Pandas**: Data manipulation and CSV export
- **Custom CSS**: Beautiful styling and animations

### File Structure
```
calculator-project/
├── calculator.py              # Core calculator logic
├── streamlit_calculator.py    # Web application
├── requirements.txt           # Python dependencies
├── run_calculator.sh         # Launcher script
└── README.md                 # Documentation
```

### Dependencies
- `streamlit>=1.28.0` - Web framework
- `pandas>=2.0.0` - Data handling
- `plotly>=5.15.0` - Charts and graphs
- `numpy>=1.24.0` - Numerical operations

## 🎯 Usage Examples

### Basic Operations
1. Select "Basic Operations" from the sidebar
2. Enter two numbers
3. Click the operation button (Add, Subtract, Multiply, Divide)
4. See the result instantly

### Advanced Operations
1. Select "Advanced Operations" from the sidebar
2. Choose your operation (Power, Square Root, etc.)
3. Enter the required numbers
4. Click calculate

### Trigonometric Functions
1. Select "Trigonometric" from the sidebar
2. Enter an angle in radians (or use the converter)
3. Click sin, cos, or tan
4. View the result

## 📊 Analytics Features

The app automatically tracks:
- Total number of calculations
- Most frequently used operations
- Operation distribution (pie chart)
- Recent calculation history
- Timestamps for all calculations

## 💾 Data Export

- Download your complete calculation history as CSV
- Includes operation type, input, result, and timestamp
- Perfect for analysis or record keeping

## 🎨 Customization

The app uses custom CSS for styling. You can modify:
- Color schemes in the CSS section
- Button styles and hover effects
- Layout and spacing
- Font sizes and weights

## 🔒 Error Handling

The app includes comprehensive error handling for:
- Division by zero
- Invalid inputs
- Mathematical domain errors
- User input validation

## 🌟 Future Enhancements

Potential additions:
- Scientific notation support
- Unit conversions
- Graphing capabilities
- Custom function definitions
- Multi-language support
- Dark/light theme toggle

---

**Enjoy calculating with style! 🧮✨**