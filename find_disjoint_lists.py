def find_disjoint_lists(list_of_lists):
    disjoint_lists = []
    intersect=False
    
    for list_s in tqdm(list_of_lists):
        for list_d in list_of_lists:
            for item in list_s:
                if len([i for i in list_s if i in list_d])>0:
                    intersect=True
                    break
                else:
                    intersect=False
                    break
            if intersect==False:
                break
        if intersect== False:
            intersect2=False
            for item2 in disjoint_lists:
                if len([i for i in list_s if i in item2])>0:
                    intersect2=True
                    break
            if intersect2==False:
                disjoint_lists.append(list_s)

    return disjoint_lists
