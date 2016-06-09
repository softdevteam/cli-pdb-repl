from remote_pdb import RemotePdb
RemotePdb("localhost", 4444).set_trace()

i = 0
while True:
    i += 1
