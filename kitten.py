import requests
import time
import traceback

def getKittenByGen(gen_id,stype,good_array,virgin = False):
    remaining = True
    offset = 0
    #place your attribute here
    
    while remaining:
        limit = 100
        try:
            json_data = requests.get("https://api.cryptokitties.co/auctions?offset="+str(offset)+"&limit=100&type="+stype+"&status=open&sorting=cheap&orderBy=current_price&orderDirection=asc").json()
            for each in json_data['auctions']:
                gen = each['kitty']['generation']
                kitty_id = each['kitty']['id']
                cooldown = each['kitty']['status']['cooldown_index']
                if gen <= gen_id:
                    #try check cattribute
                    cattribute = requests.get("https://api.cryptokitties.co/kitties/"+str(kitty_id) ).json()
                    
                    #fix for api change
                    cattribute_list = []
                    for attr in cattribute['cattributes']:
                        cattribute_list.append(attr['description'])
                    for attribute in cattribute_list:
                        if attribute in good_array and (len(cattribute['children']) == 0 or not virgin):
                            print("Gen : ",gen)
                            print("ID : ",kitty_id)
                            print("Price : ",int(each['current_price'])/1000000000000000000)
                            print(",".join(cattribute_list) )
                            print("No. of childs: ",len(cattribute['children']))
                            print("=====================================================")
                            break
            offset = offset + 100
            print(offset,stype,"kitties bening scanned")
            #no more kitties left in API 
            if len(json_data['auctions']) <= 0:
                remaining = False
        except:
            traceback.print_exc()
            time.sleep(10)


####
#getKittenByGen(generation_no,sales or sire,True or False for virgin) 
###
good_array = ["spock","beard","mauveover","cymric","gold","otaku","saycheese","googly","mainecoon","whixtensions","wingtips","chestnut","jaguar"]
#getKittenByGen(7,"sale",good_array,False)
getKittenByGen(6,"sire",good_array)
