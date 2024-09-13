import os
from pathlib import Path

category_path = Path(__file__).parent.parent
subcat_path = Path(__file__).parent
content_path = str(category_path) + str("\content")
content = os.listdir(content_path)

root_path = Path(__file__).parent.parent.parent.parent
root_dir = str(root_path).replace("\\", "/")

str(root_dir)


video_extensions = [".mp4", ".mov", ".ogg", ".mvi"]

def create_video_html():

  for file in content:
    if os.path.splitext(file)[1] in video_extensions:
        file_name = str(os.path.splitext(file)[0])
        html_file_path = os.path.join(category_path, file_name + ".html")
        print(html_file_path)

        with open(html_file_path, "w") as f:
          f.write('''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Baun EduVault</title>

                <link rel="stylesheet" type="text/css" href="'''+root_dir+ '''/css/bootstrap.css">
                <link rel="icon" type="image/x-icon" href="'''+root_dir+'''/images/header/favicon.ico">

                <script type="text/javascript" src="'''+root_dir+'''/js/bootstrap.js"></script>

            </head>
            
            <body>

              <!-- Navbar -->
                <nav class="navbar navbar-dark bg-dark navbar-expand-lg bg-body-tertiary">
                  <div class="mx-auto " style="width: 80rem;">
                    
                      <a class="navbar-brand" href="'''+root_dir+'''/libray_home.html">
                          <img src="'''+root_dir+'''/images/header/logo.png" width="30" height="30" class="d-inline-block align-top" alt="logo">
                          Baun Library
                        </a>

                      <div class="navbar-nav">
                        <a class="nav-link" href="'''+root_dir+'''/libray_home.html">Home</a>
                        <a class="nav-link" href="'''+root_dir+'''/library-about.html">About</a>
                        <a class="nav-link active" aria-current="page" href="'''+root_dir+'''/library-categories.html">Categories</a>
                        <a class="nav-link" href="#">Log in</a>
                      </div>
                    </div>
                  </div>
                </nav>
              <!-- End navbar -->

              <div class="container-fluid mb-3">

                <div class="mx-auto" style="width: 80rem;">

                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb bg-dark">
                      <li class="breadcrumb-item"><a href="/library-categories.html">Categories</a></li>
                      <li class="breadcrumb-item"><a href="/library-categories.html">Arts</a></li>
                      <li class="breadcrumb-item active" aria-current="page">'''+file_name+'''</li>
                    </ol>
                  </nav>

                  <video width="1280" height="720" controls>
                    <source src="'''+content_path+"/" +file+ '''" type="video/mp4">
                            Your browser does not support the video tag.
                  </video>

                  <p class="h3 text-white">'''+file_name+'''</p></div>
                            
                </div>
              </div>

              </body>
              </html>'''
          
          )


if __name__ == "__main__":

  create_video_html()
