CREATE TABLE IF NOT EXISTS polls (
    polls_id interger [pk, UNIQUE, NOTNULL]
    msg_id interger [UNIQUE, NOTNULL]
);

CREATE TABLE IF NOT EXISTS options(
    option_id interger [NOTNULL]
    poll_id integer [NOTNULL]
    option_num integer [NOTNULL]
    option_value varchar [NOTNULL]
);

CREATE TABLE IF NOT EXISTS votes(
    option_id integer [NOTNULL]
    user_id integer [NOTNULL]
);

Ref: votes.option_id > options.option_id
Ref: options.poll_id > polls.poll_id