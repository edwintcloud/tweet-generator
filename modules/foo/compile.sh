g++ -c -fPIC foo.cpp -o foo.o
g++ -shared -Wl,-install_name,libfoo.so -o libfoo.so  foo.o