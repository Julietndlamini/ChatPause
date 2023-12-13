def join_click(e):
    if not user_name.value:
        user_name.error_text = "Name cannot be blank!"
        user_name.update()
    else:
        page.session.set("user_name", user_name.value)

        page.dialog.open = False

        login_message = Message(
            user=user_name.value,
            text=f"{user_name.value} has joined the chat.",
            message_type="login_message"
        )
        page.pubsub.send_all(login_message)

        page.update()
