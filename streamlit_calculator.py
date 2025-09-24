#!/usr/bin/env python3
"""
Streamlit Calculator Web App
A beautiful web interface for the Advanced Calculator
"""

import streamlit as st
import math
import pandas as pd
from calculator import Calculator
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .calculator-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 1rem 0;
    }
    
    .result-box {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid rgba(255,255,255,0.2);
        margin: 1rem 0;
        text-align: center;
    }
    
    .operation-button {
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-weight: bold;
        margin: 0.2rem;
        transition: all 0.3s ease;
    }
    
    .operation-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .history-item {
        background: rgba(255,255,255,0.05);
        padding: 0.5rem;
        margin: 0.2rem 0;
        border-radius: 5px;
        border-left: 4px solid #667eea;
    }
    
    .metric-card {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize calculator
if 'calculator' not in st.session_state:
    st.session_state.calculator = Calculator()

if 'calculation_history' not in st.session_state:
    st.session_state.calculation_history = []

# Main header
st.markdown('<h1 class="main-header">🧮 Advanced Calculator</h1>', unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.markdown("## 🎛️ Calculator Controls")
    
    # Operation type selector
    operation_type = st.selectbox(
        "Select Operation Type",
        ["Basic Operations", "Advanced Operations", "Trigonometric", "Logarithmic", "Other Functions"]
    )
    
    # Clear history button
    if st.button("🗑️ Clear History", type="secondary"):
        st.session_state.calculator.clear_history()
        st.session_state.calculation_history = []
        st.success("History cleared!")
    
    # Download history
    if st.session_state.calculation_history:
        history_df = pd.DataFrame(st.session_state.calculation_history)
        csv = history_df.to_csv(index=False)
        st.download_button(
            label="📥 Download History",
            data=csv,
            file_name="calculator_history.csv",
            mime="text/csv"
        )

# Main calculator interface
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
    
    # Display current operation type
    st.markdown(f"### {operation_type}")
    
    if operation_type == "Basic Operations":
        st.markdown("#### ➕ Basic Arithmetic Operations")
        
        col_a, col_b = st.columns(2)
        with col_a:
            a = st.number_input("First Number", value=0.0, step=0.1)
        with col_b:
            b = st.number_input("Second Number", value=0.0, step=0.1)
        
        col_add, col_sub, col_mul, col_div = st.columns(4)
        
        with col_add:
            if st.button("➕ Add", key="add"):
                result = st.session_state.calculator.add(a, b)
                st.session_state.calculation_history.append({
                    "Operation": "Addition",
                    "Input": f"{a} + {b}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        with col_sub:
            if st.button("➖ Subtract", key="sub"):
                result = st.session_state.calculator.subtract(a, b)
                st.session_state.calculation_history.append({
                    "Operation": "Subtraction",
                    "Input": f"{a} - {b}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        with col_mul:
            if st.button("✖️ Multiply", key="mul"):
                result = st.session_state.calculator.multiply(a, b)
                st.session_state.calculation_history.append({
                    "Operation": "Multiplication",
                    "Input": f"{a} × {b}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        with col_div:
            if st.button("➗ Divide", key="div"):
                result = st.session_state.calculator.divide(a, b)
                st.session_state.calculation_history.append({
                    "Operation": "Division",
                    "Input": f"{a} ÷ {b}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
    
    elif operation_type == "Advanced Operations":
        st.markdown("#### 🔢 Advanced Mathematical Operations")
        
        operation = st.selectbox("Select Operation", [
            "Power (a^b)", "Square Root", "Modulo", "Factorial"
        ])
        
        if operation == "Power (a^b)":
            col_a, col_b = st.columns(2)
            with col_a:
                a = st.number_input("Base", value=2.0, step=0.1)
            with col_b:
                b = st.number_input("Exponent", value=2.0, step=0.1)
            
            if st.button("🔢 Calculate Power", key="power"):
                result = st.session_state.calculator.power(a, b)
                st.session_state.calculation_history.append({
                    "Operation": "Power",
                    "Input": f"{a}^{b}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        elif operation == "Square Root":
            a = st.number_input("Number", value=16.0, step=0.1)
            if st.button("√ Calculate Square Root", key="sqrt"):
                result = st.session_state.calculator.square_root(a)
                st.session_state.calculation_history.append({
                    "Operation": "Square Root",
                    "Input": f"√{a}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        elif operation == "Modulo":
            col_a, col_b = st.columns(2)
            with col_a:
                a = st.number_input("Dividend", value=10.0, step=0.1)
            with col_b:
                b = st.number_input("Divisor", value=3.0, step=0.1)
            
            if st.button("% Calculate Modulo", key="mod"):
                result = st.session_state.calculator.modulo(a, b)
                st.session_state.calculation_history.append({
                    "Operation": "Modulo",
                    "Input": f"{a} % {b}",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        elif operation == "Factorial":
            a = st.number_input("Integer", value=5, step=1, min_value=0, max_value=170)
            if st.button("! Calculate Factorial", key="fact"):
                result = st.session_state.calculator.factorial(int(a))
                st.session_state.calculation_history.append({
                    "Operation": "Factorial",
                    "Input": f"{int(a)}!",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
    
    elif operation_type == "Trigonometric":
        st.markdown("#### 📐 Trigonometric Functions")
        
        trig_function = st.selectbox("Select Function", ["Sine", "Cosine", "Tangent"])
        angle = st.number_input("Angle (in radians)", value=math.pi/2, step=0.1)
        
        col_sin, col_cos, col_tan = st.columns(3)
        
        with col_sin:
            if st.button("sin", key="sin"):
                result = st.session_state.calculator.sine(angle)
                st.session_state.calculation_history.append({
                    "Operation": "Sine",
                    "Input": f"sin({angle})",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        with col_cos:
            if st.button("cos", key="cos"):
                result = st.session_state.calculator.cosine(angle)
                st.session_state.calculation_history.append({
                    "Operation": "Cosine",
                    "Input": f"cos({angle})",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        with col_tan:
            if st.button("tan", key="tan"):
                result = st.session_state.calculator.tangent(angle)
                st.session_state.calculation_history.append({
                    "Operation": "Tangent",
                    "Input": f"tan({angle})",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        # Angle converter
        st.markdown("#### 🔄 Angle Converter")
        col_deg, col_rad = st.columns(2)
        with col_deg:
            degrees = st.number_input("Degrees", value=90.0, step=1.0)
            radians = degrees * math.pi / 180
            st.write(f"Radians: {radians:.4f}")
        with col_rad:
            radians_input = st.number_input("Radians", value=math.pi/2, step=0.1)
            degrees_output = radians_input * 180 / math.pi
            st.write(f"Degrees: {degrees_output:.2f}°")
    
    elif operation_type == "Logarithmic":
        st.markdown("#### 📊 Logarithmic Functions")
        
        log_type = st.selectbox("Select Log Type", ["Logarithm (any base)", "Natural Logarithm"])
        
        if log_type == "Logarithm (any base)":
            col_num, col_base = st.columns(2)
            with col_num:
                number = st.number_input("Number", value=100.0, step=0.1)
            with col_base:
                base = st.number_input("Base", value=10.0, step=0.1)
            
            if st.button("log Calculate Logarithm", key="log"):
                result = st.session_state.calculator.logarithm(number, base)
                st.session_state.calculation_history.append({
                    "Operation": "Logarithm",
                    "Input": f"log_{base}({number})",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
        
        else:  # Natural Logarithm
            number = st.number_input("Number", value=math.e, step=0.1)
            if st.button("ln Calculate Natural Log", key="ln"):
                result = st.session_state.calculator.natural_log(number)
                st.session_state.calculation_history.append({
                    "Operation": "Natural Log",
                    "Input": f"ln({number})",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
    
    else:  # Other Functions
        st.markdown("#### 🔧 Other Functions")
        
        other_function = st.selectbox("Select Function", ["Absolute Value"])
        
        if other_function == "Absolute Value":
            number = st.number_input("Number", value=-5.0, step=0.1)
            if st.button("|x| Calculate Absolute Value", key="abs"):
                result = st.session_state.calculator.absolute(number)
                st.session_state.calculation_history.append({
                    "Operation": "Absolute Value",
                    "Input": f"|{number}|",
                    "Result": result,
                    "Timestamp": pd.Timestamp.now()
                })
                st.success(f"Result: {result}")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Statistics and History
    st.markdown("### 📊 Statistics")
    
    if st.session_state.calculation_history:
        # Calculate statistics
        total_calculations = len(st.session_state.calculation_history)
        operations_count = {}
        for calc in st.session_state.calculation_history:
            op = calc["Operation"]
            operations_count[op] = operations_count.get(op, 0) + 1
        
        # Display metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Calculations", total_calculations)
        with col2:
            most_used = max(operations_count, key=operations_count.get) if operations_count else "None"
            st.metric("Most Used", most_used)
        
        # Operations distribution chart
        if operations_count:
            operations_df = pd.DataFrame(list(operations_count.items()), columns=['Operation', 'Count'])
            fig = px.pie(operations_df, values='Count', names='Operation', 
                        title="Operations Distribution")
            st.plotly_chart(fig, use_container_width=True)
        
        # Recent calculations
        st.markdown("### 📝 Recent Calculations")
        recent_calcs = st.session_state.calculation_history[-5:]  # Last 5 calculations
        for calc in reversed(recent_calcs):
            st.markdown(f"""
            <div class="history-item">
                <strong>{calc['Operation']}</strong><br>
                {calc['Input']} = <strong>{calc['Result']}</strong><br>
                <small>{calc['Timestamp'].strftime('%H:%M:%S')}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No calculations yet. Start calculating to see your history!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🧮 Advanced Calculator - Built with Streamlit</p>
    <p>Supports all mathematical operations with beautiful UI</p>
</div>
""", unsafe_allow_html=True)