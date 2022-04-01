emails = {}
#Adicionando itens no dicionário
emails['juca'] = 'juca@gmail.com'
emails['ana'] = 'ana@gmail.com'
emails['pedro'] = 'pedro@gmail.com'
emails['ana'] = 'ana@yahoo.com'
emails['codigo'] =123
emails[5] = False


#listar email da ana
# print(emails['ana'])

#listar todos os emails
# for email in emails:
#   print(emails[email])

if 'ana' in emails:
    print('existe')
    emails['Ana'] = 'EmailAtualizado@gmail.com'
else:
    print('não existe')
    emails['Ana'] = 'novoEmail@gmail.com'

# remover um item de email
# emails.pop('pedro')

print(emails)

#tratando o caso

try:
    emails.pop('anas')
except: print('Ocorreu algu erro ao tentar excluir o email')