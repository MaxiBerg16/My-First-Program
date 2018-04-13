
pokemon_elegido = input('Contra que Pokemon quieres combatir? (Squirtle / Charmander / Bulbasur)')
vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == 'Squirtle':
    vida_enemigo = 90
    ataque_pokemon = 9
    nombre_pokemon = 'Squirtle'

elif pokemon_elegido == 'Charmander':
    vida_enemigo = 80
    ataque_pokemon = 10
    nombre_pokemon = 'Charmander'

elif pokemon_elegido == 'Bulbasur':
    vida_enemigo = 100
    ataque_pokemon = 8
    nombre_pokemon = 'Bulbasur'

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input('Que ataque vas a usar? (Impactrueno / Onda de Choque)')

    if ataque_elegido == 'Impactrueno':
        impac = 10
        print('Usáste Impactrueno')
        if pokemon_elegido == 'Squirtle':
            vida_enemigo -= impac * 2
            print('Has hecho {} de daño a {}, le quedan {} de vida'.format(impac * 2, nombre_pokemon, vida_enemigo))
        elif pokemon_elegido == 'Charmander':
            vida_enemigo -= impac / 2
            print('Has hecho {} de daño a {}, le quedan {} de vida'.format(impac / 2, nombre_pokemon, vida_enemigo))
        elif pokemon_elegido == 'Bulbasur':
            vida_enemigo -= impac
            print('Has hecho {} de daño a {}, le quedan {} de vida'.format(impac, nombre_pokemon, vida_enemigo))

    elif ataque_elegido == 'Onda de Choque':
        onda_choque = 12
        print('Usáste Onda de Choque')
        if pokemon_elegido == 'Squirtle':
            vida_enemigo -= onda_choque * 2
            print('Has hecho {} de daño a {}, le quedan {} de vida'.format(onda_choque * 2, nombre_pokemon, vida_enemigo))
        elif pokemon_elegido == 'Charmander':
            vida_enemigo -= onda_choque / 2
            print('Has hecho {} de daño a {}, le quedan {} de vida'.format(onda_choque / 2, nombre_pokemon, vida_enemigo))
        elif pokemon_elegido == 'Bulbasur':
            vida_enemigo -= onda_choque
            print('Has hecho {} de daño a {}, le quedan {} de vida'.format(onda_choque, nombre_pokemon, vida_enemigo))

    if pokemon_elegido == 'Squirtle' and vida_enemigo > 0:
        print('{} te ha atacado por {} de daño'.format(nombre_pokemon, ataque_pokemon))
        vida_pikachu -= ataque_pokemon
        print('Tienes {} de vida restante'.format(vida_pikachu))

    elif pokemon_elegido == 'Charmander' and vida_enemigo > 0:
        print('{} te ha atacado por {} de daño'.format(nombre_pokemon, ataque_pokemon))
        vida_pikachu -= ataque_pokemon
        print('Tienes {} de vida restante'.format(vida_pikachu))

    elif pokemon_elegido == 'Bulbasur' and vida_enemigo > 0:
        print('{} te ha atacado por {} de daño'.format(nombre_pokemon, ataque_pokemon))
        vida_pikachu -= ataque_pokemon
        print('Tienes {} de vida restante'.format(vida_pikachu))


if vida_enemigo <= 0:
    print('Felicidades... ¡Has ganado!')
elif vida_pikachu <= 0:
    print ('Oh no... ¡Has perdido!')







