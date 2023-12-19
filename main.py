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


def gen_rand_OPR():
    return num_gen(1, 100)

def gen_rand_bufferValue():
    return num_gen(0, 25)
def gen_rand_ProductionGoodPartCount():
     return num_gen(0, 150)

def gen_rand_systemMessage():
    random_num1 = num_gen(1, 10)
    random_num2 = num_gen(1, 10)
    rand_string = "Line"

    rand_string = rand_string + " " + str(random_num1) + " " + str(random_num2)

    return rand_string

def create_json_file(fileName):
    json_file_name = "JSON_template" + str(num_gen(22,567)) + ".json"
    with open(json_file_name, "w") as outfile:
        # Dump dict to JSON
        json.dump(fileName, outfile)

def create_multiple_zones(zone_list):
    zone_object = json_template['EventArgs']['ZoneInformation'][0]
    zoneArray = []
    counter = 1
    for zoneName in zone_list:
       # Create new zone obj
       zone_obj = dict(zone_object)

       # Update Name
       zone_obj['ZoneName'] = zoneName

       zone_obj['SystemMessage'] = gen_rand_systemMessage()

       zone_obj['OPR'] = gen_rand_OPR()

       zone_obj['ProductionGoodPartCount'] = gen_rand_ProductionGoodPartCount()


       # Add to array
       zoneArray.append(zone_obj)




    return zoneArray









def create_multiple_buffers(bufferNum):
    buffer_object = json_template['EventArgs']['BufferInformation'][0]
    bufferArray = []

    for i in range(1,bufferNum+1):
        # Create new zone obj
        buffer_obj = dict(buffer_object)

        # Update BUffer NAme
        buffer_obj['BufferName'] = "Buffer " + str(i)

        # update buffer value
        buffer_obj['BufferValue'] = gen_rand_bufferValue()

        # Add to array
        bufferArray.append(buffer_obj)


    return bufferArray


    return 0
def main():

    ## update the zoneNames list
    zoneNames = ["ZOneA", "ZOneB", "ZOneC","ZOneD"]

    ## update the bufffer Size
    bufferSize = 5

    all_zones_objs = create_multiple_zones(zoneNames)

    json_template['EventArgs']['ZoneInformation'] = all_zones_objs # appended all the created zone objects

    all_buffer_objs = create_multiple_buffers(bufferSize)

    json_template['EventArgs']['BufferInformation']= all_buffer_objs


    create_json_file(json_template)




main()