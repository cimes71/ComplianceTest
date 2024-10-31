import os
import configparser

RM_PORTAL = os.getenv("RM_PORTAL")
PORTAL_USER = os.getenv("PORTAL_USER")
PORTAL_PASS = os.getenv("PORTAL_PASS")

def read_config():
    config = configparser.ConfigParser()
    with open('utils/config_props.ini', 'r') as f:
        config.read_file(f)

        user = config.get('Login', 'user')
        pw = config.get('Login', 'pass' )
        step_one = config.get('Navigation', 'step_one')
        step_two = config.get('Navigation', 'step_two')
        search_criteria = config.get('Search', 'search_criteria')
        compliance_perc = config.get('Data', 'compliance_perc')
        compliance_status = config.get('Data','compliance_status' )



    config_values = {
        'user': user,
        'pass': pw,
        'step_one': step_one,
        'step_two' : step_two,
        'search_criteria': search_criteria,
        'compliance_perc': compliance_perc,
        'compliance_status': compliance_status
    }

    return config_values
