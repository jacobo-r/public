import os
import time

# Define the base directory (the folder that contains exam types and the URGENTE folder)
base_dir = "HOSPITAL"

def get_exam_types():
    """
    Returns a list of exam type folders in the base_dir, excluding the 'URGENTE' folder.
    """
    all_entries = [entry for entry in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, entry))]
    # Exclude URGENTE (case insensitive, if you need to adjust, modify this condition)
    exam_types = [entry for entry in all_entries if entry.upper() != "URGENTE"]
    return exam_types

def generate_html():
    """
    Scans the folder structure and builds an HTML string.
    The HTML is structured as:
      - Each exam type is a section with a header.
      - Under each exam type, each doctor's subfolder is shown with the list of audio files.
      - URGENTE files are handled in a separate section.
    """
    html_parts = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta http-equiv='refresh' content='60'>",  # Refresh the page every 60 seconds
        "    <title>Hospital Audio Files</title>",
        "    <style>",
        "        body { font-family: Arial, sans-serif; }",
        "        .exam-type {",
        "            color: #2a52be;",  # Blue for exam type titles
        "            border-bottom: 2px solid #2a52be;",
        "            padding-bottom: 5px;",
        "            margin-top: 20px;",
        "        }",
        "        .doctor {",
        "            color: #006400;",  # Dark green for doctor names",
        "            margin-left: 20px;",
        "            font-size: 1.1em;",
        "        }",
        "        .files {",
        "            margin-left: 40px;",
        "            font-family: monospace;",
        "        }",
        "    </style>",
        "</head>",
        "<body>"
    ]
    
    # Process each exam type folder
    for exam in get_exam_types():
        exam_path = os.path.join(base_dir, exam)
        html_parts.append(f"<div class='exam-section'>")
        html_parts.append(f"  <h2 class='exam-type'>Exam Type: {exam}</h2>")
        
        # Get doctor folders under each exam type folder
        try:
            doctor_folders = [entry for entry in os.listdir(exam_path) if os.path.isdir(os.path.join(exam_path, entry))]
        except Exception as e:
            doctor_folders = []
            print(f"Error reading subdirectories of {exam_path}: {e}")
        
        # Process each doctor folder
        for doctor in doctor_folders:
            doctor_path = os.path.join(exam_path, doctor)
            html_parts.append(f"  <h3 class='doctor'>Doctor: {doctor}</h3>")
            html_parts.append("  <ul class='files'>")
            try:
                files = [f for f in os.listdir(doctor_path) if os.path.isfile(os.path.join(doctor_path, f))]
            except Exception as e:
                files = []
                print(f"Error reading files in {doctor_path}: {e}")
            for file in files:
                html_parts.append(f"    <li>{file}</li>")
            html_parts.append("  </ul>")
        html_parts.append("</div>")
    
    # Handle the special URGENTE folder
    urgente_path = os.path.join(base_dir, "URGENTE")
    if os.path.exists(urgente_path):
        html_parts.append("<div class='exam-section'>")
        html_parts.append("  <h2 class='exam-type'>URGENTE</h2>")
        html_parts.append("  <ul class='files'>")
        try:
            urgent_files = [f for f in os.listdir(urgente_path) if os.path.isfile(os.path.join(urgente_path, f))]
        except Exception as e:
            urgent_files = []
            print(f"Error reading files in {urgente_path}: {e}")
        for file in urgent_files:
            html_parts.append(f"    <li>{file}</li>")
        html_parts.append("  </ul>")
        html_parts.append("</div>")
    
    html_parts.append("</body>")
    html_parts.append("</html>")
    
    return "\n".join(html_parts)

def write_html_file():
    """
    Writes the generated HTML content to the output file in the base_dir.
    """
    html_content = generate_html()
    output_file = os.path.join(base_dir, "index.html")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Updated {output_file}")
    except Exception as e:
        print(f"Error writing file {output_file}: {e}")

if __name__ == "__main__":
    while True:
        write_html_file()
        # Update every 60 seconds
        time.sleep(60)