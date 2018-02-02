1. install Jenkins plugins:
 - shining-panda
 - selenium

2. Manage Jenkins -> Configure System:
 - Workspace Root Directory:C:/Jenkins/workspace
 - Global properties: ShiningPanda workspace directory -> C:/Jenkins/workspace

3. Configure jenkins build:
- This project is parameterized -> Choice Parameter:
Chrome
Firefox
Edge
IE
 - Build Environment: Delete workspace before build starts
 - Set Build Name: #${BUILD_NUMBER} - ${PROJECT_DISPLAY_NAME} - ${ENV,var="Browser"}
 - Build: Virtualenv builder
  Command:
        !#/bin/bash
        git clone https://github.com/dromazan/test_pytest.git .\\repo
        pip install -r repo\requirements.txt
        pytest -s  repo\FieldsValidation.py --variables repo\%Browser%.json --html=c:\Jenkins\Reports\report-%date%-%Browser%-%RANDOM%.html