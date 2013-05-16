CODEX = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"hello world\n"
bytes_out = hello_out.encode(CODEX)

f = open(FILE,'w')
f.write(bytes_out)
f.close()

f = open(FILE);
bytes_in = f.read()
f.close()
print bytes_in
hello_in = bytes_in.decode(CODEX)
print hello_in
