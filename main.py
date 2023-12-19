import json
import random
template = """
{
    "EventName": "InitialLoadEvent",
    "EventOccured": "2023-12-15T16:15:50.4158319+00:00",
    "EventArgs": {
        "ZoneInformation": [
            {
                "ExState": 4, 
                "SystemMessage": "Line 1 0", 
                "ZoneName": "LN01", 
                "StationNumber": 1,
                "LineDownTime": 0,
                "FaultTime": 0,
                "Starved": 0,
                "Blocked": 0,
                "FTT": 0,
                "OPR": 0, 
                "JPH": 0,
                "SIP": 0,
                "RunRate": 0,
                "TAKT": 0,
                "PlannedVolume": 0,
                "ProductionGoodPartCount": 20,
                "Forecast": 0,
                "EOLProductionGoodPartCount": 210
            }
        ],
        "BufferInformation": [
            {
                "BufferName": "Buffer 1",
                "BufferType": false,
                "BufferDescription": null,
                "BufferSize": 0,
                "BufferValue": 0,
                "BufferWarning": 0,
                "BufferAlarm": 0
            }
        ],
        "SafetyAreaInformation": [],
        "AndonStationInformation": [
            {
                "MasterZone": "zzZone_01",
                "StationName": "STN101",
                "AndonType": 0,
                "Active": false,
                "SystemMessage": "LN01 ",
                "AndonPulls": 0,
                "AndonDowntime": 0,
                "ToolStops": 2,
                "ToolStopsDowntime": 15.14
            },
            {
                "MasterZone": "zzZone_01",
                "StationName": "STN102",
                "AndonType": 0,
                "Active": false,
                "SystemMessage": "LN01 ",
                "AndonPulls": 0,
                "AndonDowntime": 0,
                "ToolStops": 2,
                "ToolStopsDowntime": 15.14
            },
            {
                "MasterZone": "zzZone_01",
                "StationName": "STN103",
                "AndonType": 0,
                "Active": false,
                "SystemMessage": "LN01 ",
                "AndonPulls": 0,
                "AndonDowntime": 0,
                "ToolStops": 2,
                "ToolStopsDowntime": 15.14
            },
            {
                "MasterZone": "zzZone_01",
                "StationName": "STN104",
                "AndonType": 0,
                "Active": false,
                "SystemMessage": "LN01 ",
                "AndonPulls": 0,
                "AndonDowntime": 0,
                "ToolStops": 2,
                "ToolStopsDowntime": 15.14
            },
            {
                "MasterZone": "zzZone_01",
                "StationName": "STN105",
                "AndonType": 0,
                "Active": false,
                "SystemMessage": "LN01 ",
                "AndonPulls": 0,
                "AndonDowntime": 0,
                "ToolStops": 2,
                "ToolStopsDowntime": 15.14
            }
        ],
        "FacilityName": "FA2"
    },
    "Type": "CommonEvents.InitialLoadEvent"
}
"""

json_template = json.loads(template)



#######################################################################################

def num_gen(min,max):
    rand_int = random.randint(min, max)
    return rand_int



def generate_random_ints():
    # generating random integer values
    json_template['EventArgs']['ZoneInformation'][0]['ExState'] = num_gen(1, 12)
    json_template['EventArgs']['ZoneInformation'][0]['OPR'] = num_gen(1, 100)
    json_template['EventArgs']['ZoneInformation'][0]['ProductionGoodPartCount'] = num_gen(0, 150)
    json_template['EventArgs']['BufferInformation'][0]['BufferValue'] = num_gen(0, 25)


def generate_random_strs():

    ## generating random string for SystemMessage
    random_num1= num_gen(1,10)
    random_num2= num_gen(1, 10)
    rand_string = "Line"

    rand_string = rand_string + " " + str(random_num1) + " " +str(random_num2)

    json_template['EventArgs']['ZoneInformation'][0]['SystemMessage'] = rand_string

    ## generating random string for ZONe message

    random_num3 = num_gen(1, 200)
    rand_string2 = "LN"

    rand_string2 = rand_string2 + str(random_num3)

    json_template['EventArgs']['ZoneInformation'][0]['ZoneName'] = rand_string2


    ##generating random string for BUffer Name
    random_num4 = num_gen(1, 200)
    rand_string3 = "Buffer "
    rand_string3 = rand_string3 + str(random_num4)

    json_template['EventArgs']['BufferInformation'][0]['BufferName'] = rand_string3

def create_json_file(fileName):
    json_file_name = "JSON_template" + str(num_gen(22,567)) + ".json"
    with open(json_file_name, "w") as outfile:
        # Dump dict to JSON
        json.dump(fileName, outfile)

def main():
    generate_random_ints()
    generate_random_strs()

    create_json_file(json_template)




main()