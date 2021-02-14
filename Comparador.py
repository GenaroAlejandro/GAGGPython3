def PPT(usuario,maquina):
    if ((usuario=='pi')&(maquina=='ti')):
        return 1

    elif ((usuario=='pi')&(maquina=='pa')):
        return 2

    elif ((usuario=='pi')&(maquina=='pi')):
        return 3

    elif ((usuario == 'pa') & (maquina == 'ti')):
        return 2

    elif ((usuario == 'pa') & (maquina == 'pa')):
        return 3

    elif ((usuario == 'pa') & (maquina == 'pi')):
        return 1

    elif ((usuario == 'ti') & (maquina == 'ti')):
        return 3

    elif ((usuario == 'ti') & (maquina == 'pa')):
        return 1

    elif ((usuario == 'ti') & (maquina == 'pi')):
        return 2

    else:
        print('Hubo un error')