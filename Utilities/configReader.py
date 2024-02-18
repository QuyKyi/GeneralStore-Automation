from configparser import ConfigParser
from Consts.consts import Consts
# Setup path to read the configuration
config = ConfigParser()
config.read(Consts.DATA_CONFIG_DIR)
#
def readConfig(section, key):
    return config.get(section, key)

def writeConfig(sesction,key,newvalue):
    config.set(sesction, key, newvalue)
    with open(Consts.PROJECT_ROOT+'/ConfigurationData/conf.ini', 'w') as configfile:
        config.write(configfile)


a = readConfig("GeneralStore","customer_name")
print(a)

