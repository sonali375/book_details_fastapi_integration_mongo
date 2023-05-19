import configparser

config_obj = configparser.ConfigParser()
config_obj.read("configuration/application.conf")

# SERVICE DETAILS
SERVICE_HOST = config_obj.get("SERVICE", "HOST")
SERVICE_PORT = config_obj.get("SERVICE", "PORT")


# MONGO DETAILS
# MONGO_DB_URI = config_obj.get("MONGO_DB", "URI")
