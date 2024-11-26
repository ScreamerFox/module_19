# дополнение про написаные запросы прочитал в концe
# где оно и написанно поэтому не добавил все команды. Команды с созданием объектов думаю понятны и так))


buyer1 = Buyer.objects.get(id=1) #мелкий
buyer2 = Buyer.objects.get(id=2)
buyer3 = Buyer.objects.get(id=3) #Женя

game1 = Game.objects.get(id=1) # с огр
game2 = Game.objects.get(id=2)
game3 = Game.objects.get(id=4) # с огр


game1.buyer.set([buyer2, buyer3])
game2.buyer.set([buyer1, buyer3])
game3.buyer.set([buyer3])