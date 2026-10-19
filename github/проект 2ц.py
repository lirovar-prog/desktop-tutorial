import random
playr={
    'name':'',
    'hp':100,
    'water':50,
    'food':50,
    'invertory':[]
}
events=[
    {'desc': '💧вы нашли водоем (+20 воды)','type': 'water', 'hp':-5, 'water':20, 'food':-5,'item':"бутылка воды"},
    {'desc': '🎒вы нашли еду (+20 еды)','type':'food','hp':-5,'water':-5, 'food':20,'item':"ягоды"},
    {'desc': '⛺вы отдыхаете (+15 здоровья)','type':'rest', 'hp':15,'water':-5,'food':-5},
    {'desc': '🐾вы попались к хищника (-30 здоровья)','type':'enemy','hp':-30, 'water':-5,'food':-5},
    {'desc': '🍂 вы ничего не нашли (-5 ко всему статов что имеется)','type':'emty','hp':-5,'water':-5,'food':-5},
]
print('🌲===ИГРА ВЫЖИВАНИЕ В ЛЕСУУ===🌲')
playr['name']= input('👤ведите имя:')
print(f'\n{playr["name"]},у вас есть 10 дней что бы выжить в лесу❗❗❗')
for day in range(1,11):
    if playr['hp'] <=0 or playr['food']<=0 or playr['water']<=0:
        print('💀вы здохли💀')
        break
    print(f'📅---день{day}/10---📅')
    print(f'❤️здоровья{playr["hp"]} | 🍖еда {playr["food"]} | 💧вода {playr["water"]} | 🎒инвертарь{playr["invertory"]}')
    current_event=random.choice(events)
    print(f"🎯событие:{current_event['desc']}")
    if current_event['type']=='water':
        print('💦1-попить\n💧2-набрать в бутылку')
        choice=int(input('🚼ваш выбор:\n'))
        if choice==1:
            playr['water'] +=current_event['water']
            playr['hp']+=current_event['hp']
            playr['food']+=current_event['food']
            print('🤤вы выпиваете')
        elif choice==2:
            playr['hp']+=current_event['hp']
            playr['food']+=current_event['food']
            if current_event['item'] not in playr['invertory']:
                playr['invertory'].append(current_event['item'])
                print('💧вы набрали бутылка воды')
            else:
                print('⚠️у вас уже есть бутылка воды')
    elif current_event['type']=='food':
        print('1-сьесть\n2-забрать собой')
        choice1=int(input('🚼ваши действия:'))
        if choice1==1:
            playr['water'] +=current_event['water']
            playr['hp']+=current_event['hp']
            playr['food']+=current_event['food']
            print('😋вы кушаете')
        elif choice1==2:
            playr['hp']+=current_event['hp']
            playr['water']+=current_event['water']
            if current_event['item'] not in playr['invertory']:
                playr['invertory'].append(current_event['item'])
                print('🧺вы собрали ягод🍓')
            else:
                print('⚠️у вас уже есть ягоды')
    elif current_event['type']=='rest':
        playr['hp']+=current_event['hp']
        playr['food']+=current_event['food']
        playr['water']+=current_event['water']
        print('💤вы отдыхаете')
        if 'бутылка воды' in playr['invertory']:
            print('🔎Хотите попить из запасов❓')
            print('1 - ✅да (+20💧)')
            print('2 - ❌нет')
            choice2= input('Ваш выбор? (1,2): ')
            if choice2== '1':
                playr['water']+=20
                playr['invertory'].remove('бутылка воды')
                print('🤤Вы утолили жажду во время отдыха.')
        if 'ягоды' in playr['invertory']:
            print('🔎Хотите перекусить ягодами❓🍓🍓🍓')
            print('1 - ✅да (+20🍖)')
            print('2 - ❌нет')
            choice3= input('Ваш выбор? (1,2): ')
            if choice3== '1':
                playr['food']+=20
                playr['invertory'].remove('ягоды')
                print('😋Вы перекусили на привале.')
    elif current_event['type']=='enemy':
        playr['hp']+=current_event['hp']
        playr['food']+=current_event['food']
        playr['water']+=current_event['water']
        print('⚠️⚠️⚠️вы получили урон от хищника⚠️⚠️⚠️')
    elif current_event['type']=='emty':
        used_water = False
        used_food = False
        if 'бутылка воды' in playr['invertory']:
            print('🔎У вас есть бутылка воды, хотите выпить❓')
            print('1 - ✅да (+20 💧)')
            print('2 - ❌нет')
            choice4= input('Ваш выбор? (1,2): ')
            if choice4 == '1':
                playr['water'] += 20
                playr['invertory'].remove('бутылка воды')
                print('🤤вы выпили воду')
                used_water = True
        if 'ягоды' in playr['invertory']:
            print('🔎У вас есть ягоды, хотите съесть❓🍓🍓🍓')
            print('1 - ✅да (+20🍖)')
            print('2 - ❌нет')
            choice5 = input('Ваш выбор❓')
            if choice5 == '1':
                playr['food'] += 20
                playr['invertory'].remove('ягоды')
                print('😋вы съели ягоды')
                used_food = True
        if not used_water and not used_food:
            playr['hp']+=current_event['hp']
            playr['food']+=current_event['food']
            playr['water']+=current_event['water']
            print('🍂вы ничего ненаходите')
    playr['hp'] = min(100, playr['hp'])
    playr['water'] = min(100, playr['water'])
    playr['food'] = min(100, playr['food'])
if playr['hp'] <=0 or playr['food'] <= 0 or playr['water'] <= 0:
    print('\n💀GAME OVER💀')
    print(f'Финальный счет - характеристик: вода 💧{playr["water"]} | ❤️Здоровье{playr["hp"]} | 🍖еда{playr["food"]} | 🎒инвентарь{playr["invertory"]}')
else:
    print('\n🎉YOU WIN👑!!!🏆')
    print(f'Финальный счет - характеристик: вода 💧{playr["water"]} | ❤️Здоровье{playr["hp"]} | 🍖еда{playr["food"]} | 🎒инвентарь{playr["invertory"]}')