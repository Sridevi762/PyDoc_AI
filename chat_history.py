from database import get_connection


def create_chat(user_id, title):
    """
    Creates a new chat.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats(user_id, title)
        VALUES(?, ?)
        """,
        (user_id, title)
    )

    conn.commit()

    chat_id = cursor.lastrowid

    conn.close()

    return chat_id


def save_message(chat_id, role, content):
    """
    Saves a message.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages(chat_id, role, content)
        VALUES(?, ?, ?)
        """,
        (chat_id, role, content)
    )

    conn.commit()
    conn.close()


def get_user_chats(user_id):
    """
    Returns all chats for a user.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title
        FROM chats
        WHERE user_id=?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    chats = cursor.fetchall()

    conn.close()

    return chats


def get_chat_messages(chat_id):
    """
    Returns all messages for a chat.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        WHERE chat_id=?
        ORDER BY id
        """,
        (chat_id,)
    )

    messages = cursor.fetchall()

    conn.close()

    return messages
def delete_chat(chat_id):
    """
    Deletes a chat and all its messages.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM messages
        WHERE chat_id = ?
        """,
        (chat_id,)
    )

    cursor.execute(
        """
        DELETE FROM chats
        WHERE id = ?
        """,
        (chat_id,)
    )

    conn.commit()
    conn.close()


