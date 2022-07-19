def isBoolean(data):
    try:
        filter = str(data).lower()

        if filter in ["true", "false"]:
            return True
    except:
        return False

