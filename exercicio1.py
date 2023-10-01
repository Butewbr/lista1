import os

pid = os.getpid()
print("PID processo pai %d:"%(pid))

command = input("Entre seu comando: ")

command = command.split()

print(command)

pidFilho = os.fork()
pid = os.getpid()

if pidFilho == 0:
    print("Processo filho %d:"%(pidFilho))

    if len(command) > 2:
        os.execlp(command[0], command[1], command[2])
    else:
        os.execlp(command[0], command[1])
    
else:
    print("PID do processo filho visto pelo pai %d:"%(pidFilho))
    os.wait()
    