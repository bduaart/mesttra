from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

print(f'Chave = {key} - {len(key)}')

msg = input('Digite a mensagem a ser criptografada: ')

print(f'Mensagem original = {msg}')

msgCript = f.encrypt(msg.encode('utf-8'))

print(f'Mensagem criptografada = {msgCript}')

msgDescript = f.decrypt(msgCript)

print(f'Mensagem descriptografada = {msgDescript}')
