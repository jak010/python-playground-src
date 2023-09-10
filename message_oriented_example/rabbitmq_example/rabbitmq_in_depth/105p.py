import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        tx = rabbitpy.Tx(channel)
        tx.select()  # Transactions Start

        message = rabbitpy.Message(
            channel,
            "This is an important Message",
            {
                "content_type": "text/plain",
                "delivery_mode": 2,
                "message_type": "important"
            })
        message.publish("chapter4-example", "important.message")
        try:
            if tx.commit():
                print("Transaction Committed")
        except rabbitpy.exceptions.NoActiveTransactionError:
            print("Tried to commit without exchange transaction")
