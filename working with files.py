stream = open('./demo.txt', 'wt')

print(f"Can I write to this file? {stream.writable()}")
stream.write('H')
stream.writelines(["ello", "world"])
stream.write("\n")

names = ['Ahmed', 'Amira']
stream.writelines(names)
stream.writelines("\n".join(names))

stream.flush()
stream.close()