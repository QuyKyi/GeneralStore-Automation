# General Store Mobile Automation Testing

This repository contains a suite of automated tests for the General Store mobile application. These tests focus on end-to-end test automation using Python, demonstrating how to automate UI testing for mobile applications. The project utilizes tools like Pytest for executing tests and generating reports with Allure.

## Project Structure

The project is organized into several key directories and files:

- **allureReport**: Directory designated for storing test reports generated by Allure, providing insightful and visually appealing reports on test execution outcomes.
- **ConfigurationData**: Stores configuration files or scripts providing necessary settings for test execution, such as device configurations, app details, or test environment specifics.
- **Consts**: Contains Python scripts or modules defining constants used throughout the test suite, such as URLs, timeouts, or error messages.
- **Logs**: Stores log files generated during test execution, crucial for troubleshooting and understanding test flow.
- **Page_Actions**: Contains Python scripts defining actions that can be performed on the mobile application's pages, encapsulating logic for interacting with UI elements.
- **Screenshots**: Stores screenshots captured during test executions, useful for debugging and documentation.
- **TestCases**: Includes Python scripts or modules defining individual test cases, containing logic for executing specific test scenarios against the mobile application.
- **Utilities**: Collection of utility scripts providing common functionalities that support test scripts, such as logging, data parsing, or environment setup.
- **requirements.txt**: Lists Python packages required for the project, facilitating easy installation via pip.
- **.idea**: A directory related to JetBrains' IntelliJ IDEA or PyCharm IDEs, containing project-specific settings and preferences. This directory is generally not included in version control as it pertains to personal development environment settings.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.12
- Android Studio (if running tests on an Android emulator) or ADB setup for real device testing
- PyCharm
- Appium 1.22.3

## Installation

1. **Clone the repository:**

```
git clone https://github.com/QuyKyi/mobile_automation_python_GeneralStore.git

```
2. **Setup:**
   
   2.1 **Python Intepreter**
   Make sure you have Python installed on your system. The project is compatible with Python 3.x.

   <img width="982" alt="Screen Shot 2024-02-18 at 8 07 09 AM" src="https://github.com/QuyKyi/GeneralStore-Automation/assets/7692721/2c0f9d10-a42e-431b-99f8-b8470fa9f1a2">

   2.2 **Updating Your Environment Variables**
   
   ```
      # Setting PATH for Python 3.12
      # The original version is saved in .zprofile.pysave
      PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:${PATH}"
      export PATH
      export PATH=/usr/local/bin:$PATH
      export PATH=/usr/local/bin:$PATH
      export ANDROID_HOME=/Users/quy.kyi/Library/Android/sdk
      export PATH="$JAVA_HOME/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH:/Users/quy.kyi/Library/Android/sdk/tools/bin"
      export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_202.jdk/Contents/Home
      export PATH=$PATH:$JAVA_HOME/bin
      export PATH=$PATH:$JAVA_HOME/lib
      export PATH=$PATH:$ANDROID_HOME/emulator
      export PATH=$PATH:$ANDROID_HOME/platform-tools
      export PATH=$PATH:$ANDROID_HOME/tools
      export PATH=$PATH:$ANDROID_HOME/build-tools
      export PATH=$PATH:$ANDROID_HOME/tools/bin
      export PATH=$PATH:$ANDROID_HOME/tools/lib/x86_64
      # Setting PATH for Python 3.11
      # The original version is saved in .zprofile.pysave
      PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:${PATH}"
      export PATH
   ```

4. **Run Allure Report:**

Ensure you are in the project directory before running these commands. Generate the Allure report by executing the following command:

```
  allure serve /path/to/allureReport


```

Once the tests have completed and the Allure results are generated, you can serve the Allure report locally using:

```
   allure serve /Users/quy.kyi/Documents/GitHub/mobile_automation_python_GeneralStore/allureReport

```

This will start a local web server and open the generated Allure report in your default web browser.

### Notes:
- Replace `/path/to/allureReport` with the actual path to your Allure report directory if it differs.
- Ensure Allure is installed on your machine. You can typically install it via package managers like brew for macOS (brew install allure) or by following the installation instructions on the Allure Framework website.
- This instruction assumes that the user has `pytest` and `allure-pytest` already set up in their environment. 

<img width="1437" alt="Screen Shot 2024-02-18 at 8 48 50 AM" src="https://github.com/QuyKyi/GeneralStore-Automation/assets/7692721/d1105693-af4c-422b-90a9-31fd76a1df8d">
<img width="1630" alt="Screen Shot 2024-02-18 at 8 49 57 AM" src="https://github.com/QuyKyi/GeneralStore-Automation/assets/7692721/47d0f80c-a73a-4bf5-9542-00ae8b737817">

4. **Run without Allure Report:**
   Ensure you are in the project directory before running these commands.
   ```
   pytest /path/to/test_checkout_demo.py

   ```
   ### Notes:
   - Replace `/path/to/test_checkout_demo.py` with the actual path to your test script if it differs.
