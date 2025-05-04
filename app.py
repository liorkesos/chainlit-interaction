import chainlit as cl

@cl.on_chat_start
async def start():
    # Create a text element and send it
    test_text_element = cl.Text(
        content="Welcome to the ChainLit app! How can I help you today?",
        display="side",
        name="test_text_element",
    )
    await cl.Message(content="Welcome to the ChainLit app!", elements=[test_text_element]).send()

    # Create a custom welcome card element
    welcome_card = cl.CustomElement(
        name="WelcomeCard",
        display="side",
        props={
            "title": "Welcome to ChainLit!",
            "subtitle": "Your AI Assistant",
            "message": "I'm here to help you with your questions."
        }
    )

    # Store the element in the user session for potential updates later
    cl.user_session.set("welcome_card", welcome_card)

    # Send the welcome card element
    await cl.Message(
        content="Welcome to the ChainLit app! Click WelcomeCard to see more information.",
        elements=[cl.user_session.get("welcome_card")]
    ).send()
