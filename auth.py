import bcrypt

from database import get_connection


def register_user(username, password):
    """
    Registers a new user.
    """

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:

        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES(?, ?)
            """,
            (
                username,
                hashed_password
            )
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login_user(username, password):
    """
    Checks login credentials.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT id, password
        FROM users
        WHERE username=?
        """,

        (username,)

    )

    user = cursor.fetchone()

    conn.close()

    if user is None:

        return None

    user_id = user[0]

    stored_password = user[1]

    if bcrypt.checkpw(
        password.encode(),
        stored_password
    ):

        return user_id

    return None