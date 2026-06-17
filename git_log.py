import zlib
import os
import hashlib

def read_commit(commit_hash):
    obj_path = os.path.join(
        ".git",
        "objects",
        commit_hash[:2],
        commit_hash[2:]
    )
    with open(obj_path,"rb") as f:
        data=f.read()
    raw=zlib.decompress(data)
    header,content=raw.split(b"\0",1)
    content=content.decode()
    lines=content.splitlines()
    parent_hash=None
    message=""
    for i,line in enumerate(lines):
        if line.startswith("parent "):
            parent_hash=line.split()[1]
        if line=="":
            message="\n".join(lines[i+1:])
            break
    return parent_hash,message
    
with open(".git/HEAD") as f:
    head=f.read().strip()
ref_path=head.split()[1]

with open(os.path.join(".git",ref_path)) as f:
    current_hash=f.read().strip()

while current_hash:
    parent_hash,message=read_commit(current_hash)
    print(f"{current_hash[:7]} {message}")
    current_hash = parent_hash