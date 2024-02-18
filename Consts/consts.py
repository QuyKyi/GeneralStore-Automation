from pathlib import Path


class Consts:
    # Project structure
    PROJECT_ROOT = str(Path(__file__).parent.parent)
    PROJECT_NAME = PROJECT_ROOT.split("/")[-1]
    LOG_FILE = PROJECT_ROOT + "/Logs/"
    DATA_CONFIG_DIR = PROJECT_ROOT + "/ConfigurationData/conf.ini"
    SCREENSHOT_DIR = PROJECT_ROOT + "/Screenshots/"

#print(Consts.PROJECT_ROOT)
#pytest test_01_Onboard_Screen.py --alluredir="/Users/phdvqc/Documents/GitHub/mobile_automation_python_GeneralStore/allureReport"
#pytest --alluredir="/Users/phdvqc/Documents/GitHub/mobile_automation_python_GeneralStore/allureReport"
#allure serve /Users/phdvqc/Documents/GitHub/mobile_automation_python_GeneralStore/allureReport