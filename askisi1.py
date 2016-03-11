def createGame():
    import random
    Matrix = [[0 for x in range(10)] for y in range(10)];
    for i in range(10):
        print(Matrix[i]);
    print('se ena apo ola ta 0 vriskesai esy kai se ena allo o thisauros..prosekse mh vgeis ektos tou pinaka giati tha xaseis..vres ton!!')
    playerx = random.randint(0,9);
    playery = random.randint(0,9);
    tresurex = random.randint(0,9);
    tresurey = random.randint(0,9);
    Matrix[playerx][playery] = 'P';
    Matrix[tresurex][tresurey] = 'T';
    distx=tresurex-playerx;
    disty=tresurey-playery;
    while(distx != 0) or (disty != 0):
        k = str(raw_input("dialekse tin kinisi sou gia na vreis ton thisauro..left,right,up or down?"))
        if k=="left":
            Matrix[playerx][playery] = 0;
            playery -= 1
            Matrix[playerx][playery] = 'P';
            if disty >=0:
                print('apomakrynesai apo to thisauro')
            if disty < 0 and abs(disty) != 1:
                print('i apostash sou apo to thisauro orizontia einai %s' % (abs(disty+1)))
            if disty == -1:
                print('vriskesai stin idia sthlh me to thisauro')
        if k=="right":
            if disty <= 0:
                print('apomakrynesai apo to thisauro')
            if disty > 0 and abs(disty) != 1:
                print('i apostash sou apo to thisauro orizontia einai %s' % (abs(disty-1)))
            if disty == 1:
                print('vriskesai stin idia sthlh me to thisauro')
            Matrix[playerx][playery] = 0;
            playery += 1
            Matrix[playerx][playery] = 'P';
        if k=="down":
            if distx <=0:
                print('apomakrynesai apo to thisauro')
            if distx > 0 and abs(distx) != 1:
                print('i apostash sou apo to thisauro katakoryfa einai %s' % (abs(distx-1)))
            if distx == 1:
                print('vriskesai stin idia grammh me to thisauro')
            Matrix[playerx][playery] = 0;
            playerx += 1
            Matrix[playerx][playery] = 'P';
        if k=="up":
            if distx >= 0:
                print('apomakrynesai apo to thisauro')
            if distx < 0 and abs(distx) != 1:
                print('i apostash sou apo to thisauro katakoryfa einai %s' % (abs(distx+1)))
            if distx == -1:
                print('vriskesai stin idia grammh me to thisauro')
            Matrix[playerx][playery] = 0;
            playerx -= 1;
            Matrix[playerx][playery] = 'P';
        distx=tresurex-playerx;
        disty=tresurey-playery;
        if (playerx < 0):
            print('exases');
            break;
        if (playerx > 9):
            print('exases');
            break;
        if (playery < 0):
            print('exases');
            break;
        if (playery > 9):
            print('exases');
            breaek;
        if (distx == 0) and (disty == 0):
            print("nikhses vrikes ton thisauro");
    




    
