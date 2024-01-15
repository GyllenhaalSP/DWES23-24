# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    string = smb_path.replace('//', '').strip().split('/')
    host = string[0]
    path = '/' + '/'.join(string[1:])
    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')
