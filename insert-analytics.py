import os

# Your official Google Analytics tag
analytics_tag = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YLXDBH6CLE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YLXDBH6CLE');
</script>
"""

# Path to your GitHub project folder (change this if needed)
project_root = "."

# Loop through every file in the project
for root, dirs, files in os.walk(project_root):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Only add the tag if it’s not already there
            if "gtag('config', 'G-YLXDBH6CLE')" not in content:
                # Insert the tag before </head>
                if "</head>" in content:
                    content = content.replace("</head>", analytics_tag + "\n</head>")

                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)

                    print(f"✅ Google Analytics tag added to: {filepath}")
                else:
                    print(f"⚠️ No </head> tag found in: {filepath} — skipped")
            else:
                print(f"⏭ Already contains Google tag: {filepath}")

