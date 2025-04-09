import os
import time

###############################
# Functions for HOSPITAL folder #
###############################

def get_hospital_exam_types():
    """
    Returns a list of exam type folders in the HOSPITAL folder,
    excluding the 'URGENTE' folder.
    """
    base_dir = "HOSPITAL"
    all_entries = [entry for entry in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, entry))]
    exam_types = [entry for entry in all_entries if entry.upper() != "URGENTE"]
    return exam_types

def generate_html_hospital():
    """
    Generates an HTML string for the HOSPITAL folder.
    The URGENTE folder is placed at the very top, followed by exam type sections.
    Each exam type section contains doctor subdirectories along with their audio files.
    """
    base_dir = "HOSPITAL"
    
    html_parts = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta http-equiv='refresh' content='60'>",  # Refresh every 60 seconds
        "    <title>Hospital Audio Files</title>",
        "    <style>",
        "        body { font-family: Arial, sans-serif; }",
        "        .section { margin-bottom: 30px; }",
        "        .title { color: #2a52be; border-bottom: 2px solid #2a52be; padding-bottom: 5px; }",
        "        .subtitle { color: #006400; margin-left: 20px; font-size: 1.1em; }",
        "        .files { margin-left: 40px; font-family: monospace; }",
        "    </style>",
        "</head>",
        "<body>"
    ]
    
    # 1. Process the URGENTE folder first.
    urgente_path = os.path.join(base_dir, "URGENTE")
    if os.path.exists(urgente_path):
        html_parts.append("<div class='section'>")
        html_parts.append("  <h2 class='title'>URGENTE</h2>")
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
    
    # 2. Process each exam type folder.
    exam_types = get_hospital_exam_types()
    for exam in exam_types:
        exam_path = os.path.join(base_dir, exam)
        html_parts.append("<div class='section'>")
        html_parts.append(f"  <h2 class='title'>Exam Type: {exam}</h2>")
        
        # For each exam type, list doctor folders.
        try:
            doctor_folders = [entry for entry in os.listdir(exam_path) if os.path.isdir(os.path.join(exam_path, entry))]
        except Exception as e:
            doctor_folders = []
            print(f"Error reading subdirectories of {exam_path}: {e}")
        
        for doctor in doctor_folders:
            doctor_path = os.path.join(exam_path, doctor)
            html_parts.append(f"  <h3 class='subtitle'>Doctor: {doctor}</h3>")
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
    
    html_parts.append("</body>")
    html_parts.append("</html>")
    return "\n".join(html_parts)

def write_html_hospital():
    """
    Writes the generated HTML content to HOSPITAL/index.html.
    """
    base_dir = "HOSPITAL"
    html_content = generate_html_hospital()
    output_file = os.path.join(base_dir, "index.html")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Updated {output_file}")
    except Exception as e:
        print(f"Error writing file {output_file}: {e}")

#########################
# Functions for CER folder#
#########################

def generate_html_cer():
    """
    Generates an HTML string for the CER folder.
    First displays the URGENT folder (which is always present),
    then lists each doctor folder and its audio files.
    """
    base_dir = "CER"
    
    html_parts = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta http-equiv='refresh' content='60'>",  # Refresh every 60 seconds
        "    <title>CER Audio Files</title>",
        "    <style>",
        "        body { font-family: Arial, sans-serif; }",
        "        .section { margin-bottom: 30px; }",
        "        .title { color: #2a52be; border-bottom: 2px solid #2a52be; padding-bottom: 5px; }",
        "        .files { margin-left: 20px; font-family: monospace; }",
        "    </style>",
        "</head>",
        "<body>"
    ]
    
    # 1. Process the URGENT folder inside CER.
    urgent_path = os.path.join(base_dir, "URGENT")
    if os.path.exists(urgent_path):
        html_parts.append("<div class='section'>")
        html_parts.append("  <h2 class='title'>URGENT</h2>")
        html_parts.append("  <ul class='files'>")
        try:
            urgent_files = [f for f in os.listdir(urgent_path) if os.path.isfile(os.path.join(urgent_path, f))]
        except Exception as e:
            urgent_files = []
            print(f"Error reading files in {urgent_path}: {e}")
        for file in urgent_files:
            html_parts.append(f"    <li>{file}</li>")
        html_parts.append("  </ul>")
        html_parts.append("</div>")
    
    # 2. Process the doctor folders inside CER (excluding the URGENT folder).
    try:
        all_entries = [entry for entry in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, entry))]
    except Exception as e:
        all_entries = []
        print(f"Error listing directories in {base_dir}: {e}")
    
    # Exclude the URGENT folder (case insensitive)
    doctor_folders = [entry for entry in all_entries if entry.upper() != "URGENT"]
    
    for doctor in doctor_folders:
        doctor_path = os.path.join(base_dir, doctor)
        html_parts.append("<div class='section'>")
        html_parts.append(f"  <h2 class='title'>Doctor: {doctor}</h2>")
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
    
    html_parts.append("</body>")
    html_parts.append("</html>")
    return "\n".join(html_parts)

def write_html_cer():
    """
    Writes the generated HTML content to CER/index.html.
    """
    base_dir = "CER"
    html_content = generate_html_cer()
    output_file = os.path.join(base_dir, "index.html")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Updated {output_file}")
    except Exception as e:
        print(f"Error writing file {output_file}: {e}")

##########################
# Main loop - update both#
##########################

if __name__ == "__main__":
    while True:
        write_html_hospital()
        write_html_cer()
        # Update every 60 seconds
        time.sleep(60)
