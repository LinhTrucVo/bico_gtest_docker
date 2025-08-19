#!/usr/bin/env python3
"""
Google Test XML Results Summary Generator with Coverage Integration
Parses all XML test result files and generates an HTML summary report with embedded coverage.
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
import glob
import argparse
import sys

def parse_xml_files(directory):
    """Parse all XML files in the directory and extract test information."""
    test_results = []
    summary = {
        'total_tests': 0,
        'total_failures': 0,
        'total_errors': 0,
        'total_disabled': 0,
        'total_time': 0.0,
        'test_suites': {}
    }
    
    xml_files = glob.glob(os.path.join(directory, "*.xml"))
    
    for xml_file in xml_files:
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Extract testsuite information
            for testsuite in root.findall('testsuite'):
                suite_name = testsuite.get('name', 'Unknown')
                tests = int(testsuite.get('tests', 0))
                failures = int(testsuite.get('failures', 0))
                errors = int(testsuite.get('errors', 0))
                disabled = int(testsuite.get('disabled', 0))
                time_taken = float(testsuite.get('time', 0))
                
                # Update summary
                summary['total_tests'] += tests
                summary['total_failures'] += failures
                summary['total_errors'] += errors
                summary['total_disabled'] += disabled
                summary['total_time'] += time_taken
                
                if suite_name not in summary['test_suites']:
                    summary['test_suites'][suite_name] = {
                        'tests': 0, 'failures': 0, 'errors': 0, 'disabled': 0, 'time': 0.0, 'testcases': []
                    }
                
                summary['test_suites'][suite_name]['tests'] += tests
                summary['test_suites'][suite_name]['failures'] += failures
                summary['test_suites'][suite_name]['errors'] += errors
                summary['test_suites'][suite_name]['disabled'] += disabled
                summary['test_suites'][suite_name]['time'] += time_taken
                
                # Extract individual test cases
                for testcase in testsuite.findall('testcase'):
                    test_info = {
                        'name': testcase.get('name', 'Unknown'),
                        'classname': testcase.get('classname', 'Unknown'),
                        'time': float(testcase.get('time', 0)),
                        'status': testcase.get('status', 'unknown'),
                        'result': testcase.get('result', 'unknown'),
                        'file': testcase.get('file', ''),
                        'line': testcase.get('line', ''),
                        'failure': None,
                        'error': None
                    }
                    
                    # Check for failures
                    failure = testcase.find('failure')
                    if failure is not None:
                        test_info['failure'] = {
                            'message': failure.get('message', ''),
                            'text': failure.text or ''
                        }
                    
                    # Check for errors
                    error = testcase.find('error')
                    if error is not None:
                        test_info['error'] = {
                            'message': error.get('message', ''),
                            'text': error.text or ''
                        }
                    
                    summary['test_suites'][suite_name]['testcases'].append(test_info)
                    
        except ET.ParseError as e:
            print(f"Error parsing {xml_file}: {e}")
        except Exception as e:
            print(f"Unexpected error processing {xml_file}: {e}")
    
    return summary

def read_coverage_report(coverage_html_path):
    """Read the coverage HTML report and extract the body content with embedded CSS."""
    if not os.path.exists(coverage_html_path):
        print(f"Warning: Coverage report not found at {coverage_html_path}")
        return None, None
    
    try:
        with open(coverage_html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Get the coverage directory for relative path resolution
        coverage_dir = os.path.dirname(coverage_html_path)
        
        # Read the CSS file
        css_content = ""
        css_path = os.path.join(coverage_dir, "gcov.css")
        if os.path.exists(css_path):
            with open(css_path, 'r', encoding='utf-8') as css_file:
                css_content = css_file.read()
        
        # Extract the body content from the coverage HTML
        body_start = content.find('<body')
        body_end = content.find('</body>')
        if body_start != -1 and body_end != -1:
            body_start = content.find('>', body_start) + 1
            body_content = content[body_start:body_end]
        else:
            body_content = content
        
        # Fix relative paths for images
        import re
        
        # Fix image src paths to use relative paths or data URLs
        def fix_image_path(match):
            img_file = match.group(1)
            if not img_file.startswith('http') and not img_file.startswith('data:'):
                img_path = os.path.join(coverage_dir, img_file)
                if os.path.exists(img_path):
                    # Use relative path from the output report to coverage directory
                    relative_path = f"coverage/{img_file}"
                    return f'src="{relative_path}"'
                else:
                    # Create a simple colored div as fallback using data URLs
                    if 'ruby' in img_file:
                        return 'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'4\' height=\'10\'%3E%3Crect width=\'4\' height=\'10\' fill=\'%23dc3545\'/%3E%3C/svg%3E"'
                    elif 'emerald' in img_file:
                        return 'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'100\' height=\'10\'%3E%3Crect width=\'100\' height=\'10\' fill=\'%2328a745\'/%3E%3C/svg%3E"'
                    elif 'snow' in img_file:
                        return 'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'96\' height=\'10\'%3E%3Crect width=\'96\' height=\'10\' fill=\'%23f8f9fa\'/%3E%3C/svg%3E"'
                    elif 'amber' in img_file:
                        return 'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'50\' height=\'10\'%3E%3Crect width=\'50\' height=\'10\' fill=\'%23ffc107\'/%3E%3C/svg%3E"'
                    elif 'glass' in img_file:
                        return 'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'3\' height=\'3\'%3E%3Crect width=\'3\' height=\'3\' fill=\'%23dee2e6\'/%3E%3C/svg%3E"'
                    else:
                        return 'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'10\' height=\'14\'%3E%3Ctext x=\'5\' y=\'10\' text-anchor=\'middle\' font-size=\'8\' fill=\'%23333\'%3E↕%3C/text%3E%3C/svg%3E"'
            return match.group(0)
        
        body_content = re.sub(r'src="([^"]*\.png)"', fix_image_path, body_content)
        
        # Fix href paths for HTML files - make them relative to the output report
        def fix_href_path(match):
            href_file = match.group(1)
            if href_file.endswith('.html') and not href_file.startswith('http'):
                # Make the path relative to the output report location
                # The output report is in _build/, coverage files are in _build/coverage/
                relative_path = f"coverage/{href_file}"
                return f'href="{relative_path}" target="_blank"'
            return match.group(0)
        
        body_content = re.sub(r'href="([^"]*\.html)"', fix_href_path, body_content)
        
        return body_content, css_content
        
    except Exception as e:
        print(f"Error reading coverage report: {e}")
        return None, None

def generate_html_report(summary, output_file, coverage_data=None):
    """Generate an HTML report from the test summary with optional coverage integration."""
    
    # Calculate success rate
    total_tests = summary['total_tests']
    total_failed = summary['total_failures'] + summary['total_errors']
    success_rate = ((total_tests - total_failed) / total_tests * 100) if total_tests > 0 else 0
    
    # Coverage tab HTML
    coverage_tab_html = ""
    coverage_content_html = ""
    coverage_css = ""
    
    if coverage_data and coverage_data[0]:  # coverage_data is (content, css)
        coverage_content, coverage_css = coverage_data
        coverage_tab_html = '''
                <button id="coverage-tab" class="tab" onclick="showTab('coverage')">Coverage Report</button>'''
        coverage_content_html = f'''
            <div id="coverage-content" class="tab-content">
                <div class="coverage-container">
                    <h2>Code Coverage Report</h2>
                    <div class="coverage-report">
                        {coverage_content}
                    </div>
                </div>
            </div>'''
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Test Summary Report with Coverage</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5rem;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background-color: #fafafa;
        }}
        .card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .card h3 {{
            margin: 0 0 10px 0;
            color: #333;
        }}
        .card .number {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .success {{ color: #28a745; }}
        .failure {{ color: #dc3545; }}
        .warning {{ color: #ffc107; }}
        .info {{ color: #17a2b8; }}
        
        /* Tab styles */
        .tab-container {{
            margin: 0;
        }}
        .tabs {{
            display: flex;
            border-bottom: 2px solid #e0e0e0;
            background-color: #f8f9fa;
        }}
        .tab {{
            padding: 15px 30px;
            cursor: pointer;
            background-color: transparent;
            border: none;
            font-size: 1rem;
            font-weight: 500;
            color: #666;
            transition: all 0.3s ease;
        }}
        .tab:hover {{
            background-color: #e9ecef;
            color: #333;
        }}
        .tab.active {{
            background-color: #667eea;
            color: white;
            border-bottom: 3px solid #4c63d2;
        }}
        .tab-content {{
            display: none;
            padding: 30px;
        }}
        .tab-content.active {{
            display: block;
        }}
        
        .test-suite {{
            margin-bottom: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
        }}
        .suite-header {{
            background-color: #f8f9fa;
            padding: 15px 20px;
            border-bottom: 1px solid #e0e0e0;
        }}
        .suite-header h3 {{
            margin: 0;
            color: #333;
        }}
        .suite-stats {{
            display: flex;
            gap: 20px;
            margin-top: 10px;
            font-size: 0.9rem;
        }}
        .test-cases {{
            max-height: 400px;
            overflow-y: auto;
        }}
        .test-case {{
            padding: 12px 20px;
            border-bottom: 1px solid #f0f0f0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .test-case:last-child {{
            border-bottom: none;
        }}
        .test-case:hover {{
            background-color: #f8f9fa;
        }}
        .test-name {{
            font-weight: 500;
            flex: 1;
        }}
        .test-status {{
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: bold;
        }}
        .status-passed {{
            background-color: #d4edda;
            color: #155724;
        }}
        .status-failed {{
            background-color: #f8d7da;
            color: #721c24;
        }}
        .status-error {{
            background-color: #fff3cd;
            color: #856404;
        }}
        .progress-bar {{
            width: 100%;
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745 0%, #20c997 100%);
            transition: width 0.3s ease;
        }}
        .timestamp {{
            text-align: center;
            color: #666;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }}
        .coverage-container {{
            background-color: white;
            border-radius: 8px;
            padding: 0;
            overflow: auto;
        }}
        .coverage-container h2 {{
            margin: 0 0 20px 0;
            padding: 20px 20px 0 20px;
            color: #333;
        }}
        .coverage-report {{
            padding: 0 20px 20px 20px;
        }}
        /* Coverage-specific styles */
        {coverage_css}
    </style>
    <script>
        function showTab(tabName) {{
            // Hide all tab contents
            var tabContents = document.getElementsByClassName('tab-content');
            for (var i = 0; i < tabContents.length; i++) {{
                tabContents[i].classList.remove('active');
            }}
            
            // Remove active class from all tabs
            var tabs = document.getElementsByClassName('tab');
            for (var i = 0; i < tabs.length; i++) {{
                tabs[i].classList.remove('active');
            }}
            
            // Show selected tab content and mark tab as active
            document.getElementById(tabName + '-content').classList.add('active');
            document.getElementById(tabName + '-tab').classList.add('active');
        }}
        
        // Initialize tabs when page loads
        document.addEventListener('DOMContentLoaded', function() {{
            showTab('tests');
        }});
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Google Test Summary Report</h1>
            <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <div class="summary-cards">
            <div class="card">
                <h3>Total Tests</h3>
                <div class="number info">{total_tests}</div>
            </div>
            <div class="card">
                <h3>Passed</h3>
                <div class="number success">{total_tests - total_failed}</div>
            </div>
            <div class="card">
                <h3>Failed</h3>
                <div class="number failure">{summary['total_failures']}</div>
            </div>
            <div class="card">
                <h3>Errors</h3>
                <div class="number warning">{summary['total_errors']}</div>
            </div>
            <div class="card">
                <h3>Success Rate</h3>
                <div class="number success">{success_rate:.1f}%</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {success_rate}%"></div>
                </div>
            </div>
            <div class="card">
                <h3>Total Time</h3>
                <div class="number info">{summary['total_time']:.3f}s</div>
            </div>
        </div>
        
        <div class="tab-container">
            <div class="tabs">
                <button id="tests-tab" class="tab active" onclick="showTab('tests')">Test Results</button>{coverage_tab_html}
            </div>
            
            <div id="tests-content" class="tab-content active">
                <h2>Test Suites Details</h2>'''

    # Add test suite details
    for suite_name, suite_data in summary['test_suites'].items():
        suite_tests = suite_data['tests']
        suite_failures = suite_data['failures']
        suite_errors = suite_data['errors']
        suite_passed = suite_tests - suite_failures - suite_errors
        suite_success_rate = (suite_passed / suite_tests * 100) if suite_tests > 0 else 0
        
        html_content += f'''
                <div class="test-suite">
                    <div class="suite-header">
                        <h3>{suite_name}</h3>
                        <div class="suite-stats">
                            <span><strong>Tests:</strong> {suite_tests}</span>
                            <span><strong>Passed:</strong> <span class="success">{suite_passed}</span></span>
                            <span><strong>Failed:</strong> <span class="failure">{suite_failures}</span></span>
                            <span><strong>Errors:</strong> <span class="warning">{suite_errors}</span></span>
                            <span><strong>Success Rate:</strong> <span class="success">{suite_success_rate:.1f}%</span></span>
                            <span><strong>Time:</strong> {suite_data['time']:.3f}s</span>
                        </div>
                    </div>
                    <div class="test-cases">'''
        
        # Add individual test cases
        for test_case in suite_data['testcases']:
            status_class = "status-passed"
            status_text = "PASSED"
            
            if test_case['failure']:
                status_class = "status-failed"
                status_text = "FAILED"
            elif test_case['error']:
                status_class = "status-error"
                status_text = "ERROR"
            
            html_content += f'''
                        <div class="test-case">
                            <div class="test-name">{test_case['name']}</div>
                            <div class="test-status {status_class}">{status_text}</div>
                        </div>'''
        
        html_content += '''
                    </div>
                </div>'''
    
    html_content += f'''
            </div>
            {coverage_content_html}
        </div>
        
        <div class="timestamp">
            <p>Report generated from test results and coverage data</p>
        </div>
    </div>
</body>
</html>'''
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    """Main function to generate the test summary report."""
    parser = argparse.ArgumentParser(description='Generate Google Test summary report with optional coverage')
    parser.add_argument('--test-results-dir', '-t', 
                       help='Directory containing XML test result files')
    parser.add_argument('--coverage-report', '-c', 
                       help='Path to coverage HTML report (index.html)')
    parser.add_argument('--output', '-o', 
                       help='Output HTML file path')
    
    args = parser.parse_args()
    
    # Default paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    test_results_dir = args.test_results_dir or os.path.join(project_root, '_build', 'output', 'gtest')
    coverage_report_path = args.coverage_report or os.path.join(project_root, '_build', 'coverage', 'index.html')
    output_file = args.output or os.path.join(project_root, '_build', 'test_summary_report.html')
    
    print(f"Test results directory: {test_results_dir} or _build/Testing/Temporary")
    print(f"Coverage report: {coverage_report_path}")
    # print(f"Output file: {output_file}")
    
    if not os.path.exists(test_results_dir):
        print(f"Error: Test results directory not found: {test_results_dir}")
        sys.exit(1)
    
    # print("Parsing XML test result files...")
    summary = parse_xml_files(test_results_dir)
    
    # Read coverage report if it exists
    coverage_data = read_coverage_report(coverage_report_path)
    if coverage_data and coverage_data[0]:
        # print("Coverage report found and will be included.")
        pass
    else:
        print("No coverage report found or failed to read.")
        coverage_data = None
    
    # print("Generating HTML report...")
    generate_html_report(summary, output_file, coverage_data)
    
    print(f"Total tests: {summary['total_tests']}")
    print(f"\033[38;5;208mTotal failures: {summary['total_failures']}\033[0m")
    print(f"\033[31mTotal errors: {summary['total_errors']}\033[0m")
    success_rate = ((summary['total_tests'] - summary['total_failures'] - summary['total_errors']) / summary['total_tests'] * 100) if summary['total_tests'] > 0 else 0
    print(f"\033[32mSuccess rate: {success_rate:.1f}%\033[0m")
    print()
    print(f"\033[1mSummary report generated:\033[0m {output_file}")
    print()

if __name__ == "__main__":
    main()
