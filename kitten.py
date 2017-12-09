import requests
import time
import traceback

def getKittenByGen(gen_id,stype,good_array,virgin = False, no_of_cattribute_math = 0):
    remaining = True
    offset = 0
    #place your attribute here
    fz = {"violet":{"count":0.01},"googly":{"count":0.03},"wingtips":{"count":0.18},"jaguar":{"count":0.18},"mainecoon":{"count":0.19},"whixtensions":{"count":0.27},"cerulian":{"count":0.45},"chartreux":{"count":0.54},"fabulous":{"count":0.96},"gold":{"count":1.08},"peach":{"count":1.1},"bubblegum":{"count":2.11},"scarlet":{"count":2.26},"otaku":{"count":2.38},"dali":{"count":2.45},"bloodred":{"count":2.48},"skyblue":{"count":3},"emeraldgreen":{"count":3.25},"spock":{"count":3.35},"limegreen":{"count":3.67},"tigerpunk":{"count":3.76},"beard":{"count":4.31},"mauveover":{"count":4.39},"laperm":{"count":4.86},"cloudwhite":{"count":4.89},"calicool":{"count":4.92},"barkbrown":{"count":4.93},"cymric":{"count":5.44},"chestnut":{"count":5.55},"tongue":{"count":6.42},"saycheese":{"count":6.56},"shadowgrey":{"count":8.68},"coffee":{"count":8.7},"salmon":{"count":9.09},"royalpurple":{"count":9.42},"chocolate":{"count":10.34},"mintgreen":{"count":10.58},"swampgreen":{"count":10.6},"topaz":{"count":10.69},"orangesoda":{"count":10.73},"simple":{"count":10.74},"lemonade":{"count":10.76},"aquamarine":{"count":11.02},"raisedbrow":{"count":11.03},"munchkin":{"count":11.06},"sphynx":{"count":11.13},"greymatter":{"count":11.67},"happygokitty":{"count":13.08},"strawberry":{"count":13.09},"ragamuffin":{"count":13.34},"soserious":{"count":13.46},"sizzurp":{"count":13.69},"pouty":{"count":13.9},"himalayan":{"count":13.91},"crazy":{"count":17.51},"thicccbrowz":{"count":17.62},"luckystripe":{"count":19.65},"granitegrey":{"count":26.36},"kittencream":{"count":27.25},"totesbasic":{"count":28.59}};
    cooldown_dict = {
                        1:"fast",
                        2:"fast",
                        3:"fast,swift",
                        4:"fast,swift",
                        5:"fast,swift",
                        6:"fast,swift,snappy",
                        7:"fast,swift,snappy",
                    }
    while remaining:
        limit = 100
        try:
            #https://api.cryptokitties.co/auctions?offset=0&limit=12&type=sale&status=open&search=gen:3+gen:2&sorting=cheap&orderBy=current_price&orderDirection=asc&parents=false
            gen_string =""
            
            for i in range(0,gen_id):
                gen_string += str(i+1)+","
            #add cooldown 
            gen_string += "+cooldown:"+cooldown_dict[gen_id]
            
            url = "https://api.cryptokitties.co/auctions?search=gen:"+gen_string+"&offset="+str(offset)+"&limit=100&type="+stype+"&status=open&sorting=cheap&orderBy=current_price&orderDirection=asc"
            print(url)
            json_data = requests.get(url).json()
            
            for each in json_data['auctions']:
                gen = each['kitty']['generation']
                kitty_id = each['kitty']['id']
                cooldown = each['kitty']['status']['cooldown_index']
                
                #try check cattribute
                cattribute = requests.get("https://api.cryptokitties.co/kitties/"+str(kitty_id) ).json()
                
                #fix for api change
                cattribute_list = []
                match_count = 0
                for attr in cattribute['cattributes']:
                    description = attr['description']
                    if description in good_array:
                        description = "*"+description+"*"
                        match_count += 1
                    cattribute_list.append(description+" ("+str(fz[attr['description']]['count'])+"%)")
                    if match_count >= no_of_cattribute_math and (len(cattribute['children']) == 0 or not virgin):
                        print("Gen : ",gen)
                        print("ID : ",kitty_id)
                        print("Price : ",int(each['current_price'])/1000000000000000000)
                        print(",".join(cattribute_list) )
                        print("No. of childs: ",len(cattribute['children']))
                        print("=====================================================")
                        break
            offset = offset + 100
            print("=====================================================")
            print(offset,stype,"kitties bening scanned")
            print("=====================================================")
            #no more kitties left in API 
            if len(json_data['auctions']) <= 0:
                remaining = False
        except:
            traceback.print_exc()
            time.sleep(10)


####
#getKittenByGen(generation_no,sales or sire,[list of cattributes],True or False for virgin,no_of_cattribute_math) 
####https://api.cryptokitties.co/auctions?offset=0&limit=12&type=sale&status=open&search=gen:3&sorting=cheap&orderBy=current_price&orderDirection=asc&parents=false
            
good_array = ["spock","cymric","violet","bloodred","scarlet","calicool","tigerpunk","beard","gold","otaku","saycheese","googly","whixtensions","wingtips","jaguar"]
no_of_cattribute_math = 3
getKittenByGen(3,"sale",good_array,True,no_of_cattribute_math)
#getKittenByGen(6,"sire",good_array)
