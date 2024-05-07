Graded Assignment on CI/CD Pipeline

1. Setup:

   - Install Jenkins on a virtual machine or use a cloud-based Jenkins service.
   - Configure Jenkins with Python and any necessary libraries.
     ![image](https://github.com/igSpanser/Jenkins_python_assignment/assets/156592187/78ee20d0-247f-45f8-942c-6a8bb940b208)

2. Source Code:

  - Fork the provided Python web application repository on GitHub (provide a link to a sample Python web application repository).
  - Clone the forked repository into your Jenkins server.
  - calculator.py and test_calculator.py

3. Jenkins Pipeline:

   - Create a Jenkinsfile in the root of your Python application repository.
   - Define a pipeline with the following stages:
   
    - Build: Install dependencies using pip.
    - Test: Run unit tests using a testing framework like pytest.
    - Deploy: If tests pass, deploy the application to a staging environment.
  
    - Jenkins_conf_file

4. Triggers:

   - Configure the pipeline to trigger a new build whenever changes are pushed to the main branch of the repository.

5. Notifications:

   - Set up a notification system to alert via email when the build process fails or succeeds.

6. Documentation:

   - Document the pipeline process and any prerequisites needed for the setup in a README.md file in the repository.

7. Submission:

   - Provide the URL to the GitHub repository with the Jenkinsfile and updated README.md.

   - Include screenshots of the Jenkins pipeline showing the build, test, and deployment stages.
