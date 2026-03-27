# Last time modified: 03/04/26
# Author: y44k0v

html_base = ""

# Read template HTML
with open("garbage.html", "r") as website:
    html_base = website.read()


# Page title
page_title = "MY Art Work Website"

html_modified = html_base.replace("<title>Document", f"<title>{page_title}")


# DaisyUI libraries
daisy_ui = """

<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>

<!-- Daisy UI themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

"""

html_modified = html_modified.replace("</head>", daisy_ui + "\n</head>")


# Theme
theme = "aqua"

html_modified = html_modified.replace(
    '<html lang="en">',
    f'<html lang="en" data-theme="{theme}">'
)


# Navbar
nav_bar = """
<div class="navbar bg-base-100 shadow-sm">
  <a class="btn btn-ghost text-xl">Hala Art Gallery</a>
</div>
"""

html_modified = html_modified.replace('<body>', '<body>\n' + nav_bar)


# Background section
background = """
<div class="min-h-screen bg-sky-200 flex justify-center items-center">
"""


# Artwork card
art_1_card = """
<div class="card bg-base-100 w-96 shadow-xl m-5">
  <figure>
    <img src="07-mar04/art_1.jpg" alt="Artwork">
  </figure>

  <div class="card-body">
    <h2 class="card-title"> Blance </h2>
    <p>Original artwork by Hala</p>

    <div class="card-actions justify-end">
      <span class="text-lg font-bold">$120</span>
      <button class="btn bg-blue-900 text-white hover:bg-blue-800">Purchase</button>
    </div>

  </div>
</div>
"""
art_2_card = """
<div class="card bg-base-100 w-96 shadow-xl m-5">
  <figure>
    <img src="07-mar04/art_2.jpg" alt="Artwork">
  </figure>

  <div class="card-body">
    <h2 class="card-title">Chaos</h2>
    <p>Original artwork by Hala</p>

    <div class="card-actions justify-end">
      <span class="text-lg font-bold">$80</span>
      <button class="btn bg-blue-900 text-white hover:bg-blue-800">Purchase</button>
    </div>

  </div>
</div>
"""
art_3_card = """
<div class="card bg-base-100 w-96 shadow-xl m-5">
  <figure>
    <img src="07-mar04/art_3.jpg" alt="Artwork">
  </figure>

  <div class="card-body">
    <h2 class="card-title">Hands</h2>
    <p>Original artwork by Hala</p>

    <div class="card-actions justify-end">
      <span class="text-lg font-bold">$140</span>
      <button class="btn bg-blue-900 text-white hover:bg-blue-800">Purchase</button>
    </div>

  </div>
</div>
"""
# Close background container
background_end = """
</div>
"""


# Combine everything
page_content = background + art_1_card + art_2_card + art_3_card + background_end
html_modified = html_modified.replace("</body>", page_content + "\n</body>")


# Write final HTML
with open("index.html", "w") as file:
    file.write(html_modified)