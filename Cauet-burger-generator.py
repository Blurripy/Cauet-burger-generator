import time
preparation = 'y'
nombre = 0

while(preparation == 'y'):
    #wtf r u doin dan?
    print('\nPreparation et toastage des pains', end = ' : ')
    #the aniimation wasn't funny bitch
    time.sleep(9)
    print('✓')
    print('\nPréparation de la sauce du Giant', end = ' : ')
    #he was affraid of water
    time.sleep(5)
    print('✓')
    print('\nAjout de la sauce du Giant', end = ' : ')
    time.sleep(2)
    print('✓')
    print('\nPréparation des tomates', end = ' : ')
    time.sleep(3)
    print('✓')
    print('\nAjout des tomates', end = ' : ')
    time.sleep(2)
    print('✓')
    print('\nPréparation du fromage', end = ' : ')
    time.sleep(2)
    print('✓')
    print('\nAjout du fromage', end = ' : ')
    time.sleep(2)
    print('✓')
    print('\nCuisson et assaisonnement des steaks', end = ' : ')
    time.sleep(40)
    print('✓')
    print('\nAjout des steaks', end = ' : ')
    time.sleep(4)
    print('✓')
    print('\nCuisson du bacon', end = ' : ')
    time.sleep(2)
    print('✓')
    print('\nAjout du bacon', end = ' : ')
    time.sleep(2)
    print('✓')
    print('\nDécoupe de la salade', end = ' : ')
    time.sleep(4)
    print('✓')
    print('\nAjout de la salade', end = ' : ')
    time.sleep(2)
    print('✓')
    nombre = nombre + 1
    
    preparation = input(f'Vous avez fait {nombre} Cauet burger, voulez-vous en refaire ? (y/n) : ')
print('Cauet burger generator à bien été stoppé')
