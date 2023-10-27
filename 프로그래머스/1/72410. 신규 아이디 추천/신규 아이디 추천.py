def solution(new_id):
    
    new_id = ''.join([s.lower() for s in new_id])
    
    for x in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(x,"")
        
    while (".." in new_id):
        new_id = new_id.replace("..",".")
        
    if (new_id=="."):
        new_id = ""
    else:
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
    if (new_id==""):
        new_id = "a"
        
    if (len(new_id)>=16):
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:14]
            
    while (len(new_id)<3):
        new_id += new_id[-1]
        
    return new_id