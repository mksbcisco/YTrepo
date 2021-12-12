# This is a sample Python script.
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('hostname.myrouter.com', username='api', password='MyPassword', key_filename='D:\folder\id_rsa')
commands_4_MT = ['interface bridge add name=testing123', 'ip address add address=1.1.1.2 interface=testing123']
for line in commands_4_MT:
    stdin, stdout, stderr = client.exec_command(line)
print_command = ['interface print', 'ip address print']
for line in print_command:
    stdin, stdout, stderr = client.exec_command(line)
    print(stdout.read().decode('ascii'))
client.close()
