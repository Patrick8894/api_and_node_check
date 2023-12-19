stages:
  - test

variables:
  # Add your environment variables here
  # EMAIL_USERNAME: your_email@gmail.com
  # EMAIL_PASSWORD: $EMAIL_PASSWORD

# before_script:
#   - python3 -m pip install -r requirements.txt

test:
  stage: test
  script:
    - python3 API_check.py