class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        lst_map  =[]
        for string in strs:
            mp2 = {}
            sorteds = sorted(string)
            sorted_string =""
            for s in sorteds:
                sorted_string+=s
            if sorted_string in mp2.keys():
                mp2[sorted_string].update(mp2[sorted_string].append(string))
                
            else:
                mp2[sorted_string] =[string]
            lst_map.append(mp2)

            # for s in sorteds:
            #     if s in mp2:
            #         mp2[s]+=1
            #     else:
            #         mp2[s]=1
            # mp3 = {}
            # mp3[string] = mp2
            # lst_map.append(mp3)
        
        final_dict = {}
        for item in lst_map:
           
            for key,val in item.items():
                
                if key in final_dict.keys():
                    
                    final_dict[key].append(val)
                    # pass
                else:
                   
                    final_dict[key] = [val]
        final_list = []
        for key,value in final_dict.items():
            f = []
            for v in value:
                f.append(v[0])
            final_list.append(f)
        # print(final_list)

        return final_list    
                
    