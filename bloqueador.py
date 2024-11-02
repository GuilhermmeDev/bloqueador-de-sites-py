import os
OS = os.name
if (OS == 'posix'):
    hosts = "/etc/hosts"
elif (OS == 'nt'):
    pass

def bloquearSite(site):
    if (OS == 'posix'):
        coment = '\n# SITES BLOQUEADOS'
        with open(hosts, 'r+') as arquivo:
            content = arquivo.read()
            if (site in content):
                return "O site já foi bloqueado"
            else:
                if (coment not in content):
                    arquivo.write(coment)
                arquivo.write(f'\n0.0.0.0   {site.lower()}')
                return "Site bloqueado com sucesso"
    else:
        return "Windows"

def listarBloqueados():
    with open(hosts, 'r+') as arquivo:
        linhas = arquivo.readlines()
        
        for i, linha in enumerate(linhas):
            if ('# SITES BLOQUEADOS' in linha):
                for l in range(i, len(linhas)):
                    print(linhas[l])

def desbloquearSite(site):
    with open(hosts, 'r') as arquivo:
        linhas = arquivo.readlines()
    linhas.pop(linhas.index(f'0.0.0.0   {site.lower()}'))
    with open(hosts, 'w') as arquivo:
        arquivo.writelines(linhas)
    return 'Site desbloqueado com sucesso'
# bloquearSite('www.google.com')
# desbloquearSite('www.google.com')
# listarBloqueados()