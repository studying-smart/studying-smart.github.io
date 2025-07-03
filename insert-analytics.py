import os

# Your actual Google Analytics Measurement ID
MEASUREMENT_ID = "G-YLXDBH6CLE"

TAG_CODE = f"""
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{MEASUREMENT_ID}');
</script>
"""

def insert_analytics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    if "googletagmanager.com/gtag/js" in contents:
        print(f"Already tagged: {file_path}")
        return

    if "</head>" in contents:
        new_contents = contents.replace("</head>", TAG_CODE + "\n</head>")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_contents)
        print(f"✅ Tag added to: {file_path}")
    else:
        print(f"⚠️ No </head> found in: {file_path} — Skipped")

# Go through every HTML file in the folder
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            insert_analytics(os.path.join(root, file))


