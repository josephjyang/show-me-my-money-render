from app.models import db, Transaction


def seed_transactions():
    rod_jerry = Transaction(
        payer_id=2,
        payee_id=3,
        creator_id=2,
        amount=96.37,
        details="Dinner and drinks with the fam",
        paid=True
    )

    rod_jerry2 = Transaction(
        payer_id=3,
        payee_id=2,
        creator_id=2,
        amount=42.86,
        details="Chipping in for Marcee's gift",
        paid=False
    )

    rod_tyson = Transaction(
        payer_id=2,
        payee_id=7,
        creator_id=2,
        amount=500.00,
        details="Happy Birthday son! Buy yourself something nice",
        paid=True
    )

    rod_tyson2 = Transaction(
        payer_id=2,
        payee_id=7,
        creator_id=7,
        amount=400.00,
        details="I need some money for textbooks. Thanks for supporting my education, Dad!",
        paid=False
    )

    jerry_rod = Transaction(
        payer_id=2,
        payee_id=3,
        creator_id=3,
        amount=1000.00,
        details="Sorry your Cardinals lost, but hey, more money for me!",
        paid=False
    )

    marcee_dorothy = Transaction(
        payer_id=5,
        payee_id=4,
        creator_id=4,
        amount=34.75,
        details="For drinks last night. It was so fun! We should do it again soon.",
        paid=True
    )

    rod_ray = Transaction(
        payer_id=2,
        payee_id=6,
        creator_id=2,
        amount=250.00,
        details="Merry Christmas Ray! I still remember when you were just a little kid.",
        paid=True
    )

    marcee_jerry = Transaction(
        payer_id=4,
        payee_id=3,
        creator_id=5,
        amount=324.76,
        details="Thanks for getting the food for Rod's party! You're the best!",
        paid=True
    )

    marcee_rod = Transaction(
        payer_id=2,
        payee_id=4,
        creator_id=4,
        amount=359.64,
        details="There was this really beautiful necklace that I just had to buy. Thanks honey!",
        paid=False
    )

    db.session.add(rod_jerry)
    db.session.add(rod_jerry2)
    db.session.add(rod_tyson)
    db.session.add(rod_tyson2)
    db.session.add(jerry_rod)
    db.session.add(marcee_dorothy)
    db.session.add(rod_ray)
    db.session.add(marcee_jerry)
    db.session.add(marcee_rod)

    db.session.commit()


def undo_transactions():
    db.session.execute('TRUNCATE friend_requests RESTART IDENTITY CASCADE;')
    db.session.commit()
